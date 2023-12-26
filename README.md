# AI-project
<img src="https://capsule-render.vercel.app/api?type=wave&color=BDBDC8&height=150&section=header&text=RAG를 이용한 뉴스기사 챗봇&fontSize=20" />
Retreval Augmented Generation을 이용한 네이버 뉴스기사 챗봇

1. 데모실행파일 main.py
   Streamlit을 이용한 로컬환경에서 연결하여 데모하였음 정상작동시 다음과 같은 화면이 나오게 됨.
2. 해당 데모를 실행하기 위해서 필요한 것.
   2-1 : chat GPT를 사용 할 수 있는 OpenAI API key
   2-2 : 로컬에서 네이버뉴스를 Crawl_data.py를 이용하여 크롤링
   2-3 : 크롤링한 네이버 뉴스 데이터가 들어있는 폴더를 경로 설정하고, 데이터를 하나의 csv파일로 Merge(data_merge.py)
   2-4 : Merge한 csv파일을 FAISS로 indexing
3. Open AI API Key를 main.py파일에 입력하고, 저장한후 실행
4.   
<img src="https://capsule-render.vercel.app/api?type=wave&color=BDBDC8&height=150&section=footer&text=RAG를 이용한 뉴스기사 챗봇&fontSize=20" />
