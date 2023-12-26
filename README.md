# AI-project
<img src="https://capsule-render.vercel.app/api?type=wave&color=BDBDC8&height=150&section=header&text=RAG를 이용한 뉴스기사 챗봇&fontSize=20" />
Retreval Augmented Generation을 이용한 네이버 뉴스기사 챗봇
# 0. 환경세팅 : selenium webdriver, langchain, 

# 1. 최종 데모 실행 파일 main.py

   Streamlit을 이용한 로컬환경에서 연결하여 데모를 진행하였음.

# 2. 해당 데모를 실행하기 위해서 필요한 것.

  2-1 : chat GPT를 사용 할 수 있는 OpenAI API key
 ![image](https://github.com/MyungKyuKim/AI-project/assets/71568851/f88c60b8-9d8a-407c-8939-04c0128b4105)


  2-2 : 로컬에서 네이버뉴스를 Crawl_data.py를 이용하여 크롤링


  2-3 : 크롤링한 네이버 뉴스 데이터가 들어있는 폴더를 경로 설정하고, 데이터를 하나의 csv파일로 Merge(data_merge.py)


  2-4 : Merge한 csv파일을 FAISS로 indexing

# 3. Open AI API Key를 main.py파일에 입력하고, 저장한후 실행 
 정상적으로 동작한다면 아래와 같은 초기화면을 볼 수 있다.
 ![image](https://github.com/MyungKyuKim/AI-project/assets/71568851/4788084c-43dc-4094-8399-c774073f3052)
 ![image](https://github.com/MyungKyuKim/AI-project/assets/71568851/30ed412e-137f-4e13-8de3-b45c3453be9f)
 ![image](https://github.com/MyungKyuKim/AI-project/assets/71568851/a4085fe3-8eb2-4b6e-8883-81d945b14c5b)

# 4. Train폴더
 이 노트북은 직접 Korquad데이터를 가지고 Lora와 Neftune을 적용하여 mistral-7b모델을 instruction tuning 시키는 코드이다. 

  
<img src="https://capsule-render.vercel.app/api?type=wave&color=BDBDC8&height=150&section=footer&text=RAG를 이용한 뉴스기사 챗봇&fontSize=20" />
