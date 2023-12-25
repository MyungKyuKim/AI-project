from selenium import webdriver
import time, os
import pandas as pd
import warnings
import re
import pandas as pd
import numpy as np
import pandas as pd
import re
import multiprocessing
import datetime

path='/usr/bin/chromedriver'

warnings.filterwarnings(action='ignore')

BASE_DIR = './'
DATA_DIR = 'result'
web = os.path.join(BASE_DIR, 'chromedriver')
_url = "https://news.naver.com/"
news_type_list = [('today_main_news','100'), ('section_politics','100'), ('section_economy','101'), ('section_society','102'),('section_life','103'),('section_world','104'),('section_it','105')]
def replace_all(text, dic):
    for j in dic.values():
        text = re.sub(j, ' ', text)
    return text

def preprocessing_div_contents(x):
    find_re = {
        "find_icon" : r"©[.]+",
        "find_reporter" : r"[가-힣]{2,4} ([가-힣])*기자",
        "find_email" : r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
        "find_things" : r'\[.+?\]',
        "find_useless_bracket" : r"\( *\)",
        "find_n" : r'\n',
        "find_backslash" : r"\\",
        "find_spaces" : r"  +"
    }

    result = replace_all(x, find_re)    

    return result.strip()

def crawling(news_type, num):
    def get_news_info_df(news_type):
        title = driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div[2]/h2').text
        date = driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div[3]/div[1]/div[1]/span').text
        editor = driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div[3]/div[2]/a/em').text
        press = driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div[1]/a/img[1]').get_attribute('alt')
        p = re.compile(r'[0-9]+.[0-9]+.[0-9]+')
        if p.match(date) is None:
            date = driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div[3]/div[1]/div/span').text
        date = date[:10]
        print("news_type:", news_type )
        date = date.replace('.', '-')

        pre_contents = driver.find_element_by_xpath('//*[@id="dic_area"]').text
        contents = preprocessing_div_contents(pre_contents)
        # image_url = get_poster_url()
        news_url = driver.current_url
        df = pd.DataFrame([news_type, title, date, pre_contents, contents, news_url, editor, press]).T
        df.columns = ['news_type', 'title', 'date', 'all_contents', 'contents', 'news_url', 'editor', 'press']
        return df

    def get_poster_url():
        # get the image source
        try:
                img = driver.find_element_by_xpath('//*[@id="img1"]')
                src = img.get_attribute('src')
        except:
                src = "https://newsimg.sedaily.com/2019/01/23/1VE5F3W5WP_18.png"
        return src

    data_list = []
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('window-size=1920x1080')
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(path, options=options)
    
    _url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1='
    if news_type == 'today_main_news':
        try :
            t_url = _url + '100'
            driver.get(t_url)
            driver.implicitly_wait(2)
        except:
            pass
        for i in range(1,6):
            try:
                driver.find_element_by_xpath('//*[@id="_rankingList0"]/li['+str(i)+']/div/div/div/a[1]').click() 
                driver.implicitly_wait(2)
                data_list.append(get_news_info_df(news_type))
                driver.back()
            except:
                driver.get(t_url)

    else:
        if news_type == 'section_life' or news_type == 'section_it':
            div_n = 8
            div_n2 = 6
        else:
            div_n = 7
            div_n2 = 5
        try :
            t_url = _url + num
            driver.get(t_url)
            driver.implicitly_wait(2)
        except:
            pass
        for k in range(1, 8):
            driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr/td[2]/div/div/div['+str(div_n)+']/a['+str(k)+']').click()
            driver.implicitly_wait(2)
            for i in range(1,5):
                for j in range(1,6):
                    try:
                        driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr/td[2]/div/div/div['+str(div_n2)+']/ul['+str(i)+']/li['+str(j)+']/dl/dt[2]/a').click() 
                        driver.implicitly_wait(2)
                        data_list.append(get_news_info_df(news_type))
                        driver.back()
                    except:
                        driver.get(t_url)
                        print("noooo")
           
    driver.quit()
    return data_list

num_cpu = multiprocessing.cpu_count() - 1
start_time = datetime.datetime.now()
print("Start Time :", start_time)

result = []
for (t,num) in news_type_list:
    result += crawling(t, num)

end_time = datetime.datetime.now()

all_data = pd.concat(result).reset_index(drop=True)
all_data.to_csv(os.path.join(BASE_DIR, DATA_DIR, start_time.strftime("%Y%m%d-%H") + '.csv', ), encoding='utf-8' ,index=False, mode='w')
print("End Date :", end_time)



