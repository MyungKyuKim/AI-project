import os
import pandas as pd
import time

from langchain import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings

passage_data = pd.read_csv("./indexing_faiss/merged_crawling_data.csv")
embedding_fn = SentenceTransformerEmbeddings(model_name="jhgan/ko-sroberta-multitask")

start_time = time.time()
metadatas = []
for index, row in passage_data.iterrows():
    meta_data = {"news_type":row['news_type'],"title": row['title'], "link": row['news_url'], "date":row['date'] }
    metadatas.append(meta_data)

faiss = FAISS.from_texts(passage_data['contents'].tolist(),embedding_fn, metadatas)
print(time.time()-start_time)

faiss.save_local("./indexing_faiss", "2023-12-25") # index파일 세이브


