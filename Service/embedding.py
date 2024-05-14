from Model.Setting import Setting
setting = Setting()
from langchain.embeddings import HuggingFaceEmbeddings
model_name = setting.EMBEDDING_MODEL
model_kwargs = {'device': setting.EMBEDDING_DEVICE}
embedding = HuggingFaceEmbeddings(model_name=model_name,
                                  model_kwargs=model_kwargs)

import asyncio
from typing import Dict
from datetime import datetime, timedelta
import threading

# 存儲每個id的重新嵌入任務和最後呼叫時間
re_embedding_tasks: Dict[int, asyncio.Task] = {}
last_call_times: Dict[int, datetime] = {}

async def re_embedding(line_id: str, id: int, delay: int = 5):
    """
    Re-embedding function with a delay for a specific id.

    Args:
        id (int): The id for which the re-embedding process is being performed.
        delay (int, optional): The delay in seconds before executing the re-embedding process. Defaults to 5.
    """
    global re_embedding_tasks, last_call_times

    # 獲取當前時間
    now = datetime.now()

    # 檢查是否已經有任務在執行,以及是否在延遲時間內被再次呼叫
    if id in re_embedding_tasks and (now - last_call_times[id]) < timedelta(seconds=delay):
        # 取消之前的任務
        re_embedding_tasks[id].cancel()

    # 更新最後呼叫時間
    last_call_times[id] = now

    # 定義實際的重新嵌入協程
    async def re_embedding_coroutine():
        # 等待指定的延遲時間
        await asyncio.sleep(delay)

        # 檢查在延遲時間內是否有重複呼叫
        if id in re_embedding_tasks and (datetime.now() - last_call_times[id]) < timedelta(seconds=delay):
            # 如果有重複呼叫,則重新計時
            return

        # 執行重新生成向量資料庫的過程
        files = knowledgeBaseFile.get_all_files(line_id, id)
        print(len(files))
        if len(files) > 0:
            # 建立一個子執行緒
            t = threading.Thread(target = generate_vectordb, args = (line_id, id, files))
            # 執行該子執行緒
            t.start()

        # 從字典中移除任務和最後呼叫時間
        del re_embedding_tasks[id]
        del last_call_times[id]

    # 創建新的任務
    re_embedding_tasks[id] = asyncio.create_task(re_embedding_coroutine())


from langchain.document_loaders import PyMuPDFLoader, TextLoader
import glob
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
import os
from Model.KnowledgeBaseFile import knowledgeBaseFile

def generate_vectordb(line_id, id, files):
    datas = []

    # files = knowledgeBaseFile.get_all_files(line_id, id)
    for i in files:
        path = i[2]
        active = i[3]
        if active == 0:
            continue

        if path.endswith(".pdf"):
            loader = PyMuPDFLoader(path)
            datas.extend(loader.load())
        elif path.endswith(".csv"):
            loader = CSVLoader(file_path=path, encoding="utf-8")
            datas.extend(loader.load())
        elif path.endswith(".txt"):
            loader = TextLoader(file_path=path, encoding="utf-8")
            datas.extend(loader.load())

    if len(datas) == 0:
        return

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=5)
    all_splits = text_splitter.split_documents(datas)

    persist_directory = f"./db/vector_db/{line_id}"
    if not os.path.exists(persist_directory):
            try:
                os.makedirs(persist_directory)
            except:
                raise

    print("embedding... ...")
    db = Chroma(
        embedding_function=embedding, 
        persist_directory=persist_directory, 
        collection_name = f"{line_id}_{id}",
        collection_metadata={"hnsw:space": "cosine"}
    )
    db.delete_collection()

    Chroma.from_documents(
        documents=all_splits, 
        embedding=embedding, 
        persist_directory=persist_directory, 
        collection_name = f"{line_id}_{id}",
        collection_metadata={"hnsw:space": "cosine"})
    print("embedding finish!")
