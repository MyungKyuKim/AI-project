import streamlit as st
import pandas as pd
from streamlit_chat import message

from langchain import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings

recent_data = pd.read_csv("./indexing_faiss/merged_crawling_data.csv")
embedding_fn = SentenceTransformerEmbeddings(model_name="jhgan/ko-sroberta-multitask")
loaded_faiss=FAISS.load_local("./indexing_faiss",embedding_fn,"2023-12-25")

retriever = loaded_faiss.as_retriever(search_kwargs={"k":3})

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def generate_response(query):
    llm = ChatOpenAI(
        temperature=0,
        model_name='gpt-3.5-turbo-16k-0613',
        openai_api_key="API_TOKEN"
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True)

    llm_response = qa_chain(query)
    return {"result": llm_response['result'], "news_link": llm_response['source_documents']}

top_10 = []
top_10_link = []

for i, d in recent_data.iterrows():
    top_10.append(d['title'])
    top_10_link.append(d['news_url'])
    if i == 10:
        break


st.header("News Chatbot Demo")
for i, j in zip(top_10, top_10_link):
    st.write(i)
    st.markdown(j)



if 'generation' not in st.session_state:
    st.session_state['generation'] = []
    print(1)

if 'query' not in st.session_state:
    st.session_state['query'] = []
    print(1)

with st.form('form', clear_on_submit=True):
    user_input = st.text_input("혹시 위 기사에서 궁금한 것이 있나요?", key='input')
    #dic 반환
    submit = st.form_submit_button("보내기")

print(st.session_state['query'])

if submit and user_input:
    output = generate_response(user_input) # gen
    st.session_state.query.append(user_input)
    st.session_state.generation.append(output)
    
print(st.session_state)

if st.session_state['generation']:
    for i in range(len(st.session_state['generation'])-1, -1, -1):
        message(st.session_state['query'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generation"][i]["result"], key=str(i))
