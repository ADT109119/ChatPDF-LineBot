import time
from Model.Setting import Setting

from Model.KnowledgeBase import knowledgeBase
from Model.UserSelectKnowledgeBace import UserSelectKnowledgeBace
from Model.ChatHistory import chatHistory
from Model.Setting import setting

from langchain.vectorstores import Chroma
from Service.embedding import embedding
from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate, AIMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from operator import itemgetter


def chat_llm(text: str, user_id: str):
    print(user_id)
    try:
        select_db = UserSelectKnowledgeBace().getData(user_id)[0][1]
        print(select_db)
        vectordb = Chroma(
            embedding_function=embedding, 
            persist_directory=f"./db/vector_db/{user_id}", 
            collection_name=f"{user_id}_{select_db}",
            collection_metadata={"hnsw:space": "cosine"}
        )
    except Exception as e:
        print(e)
        return "查無知識庫"
    
    KnowledgeBaseSetting = knowledgeBase.get_setting(select_db, user_id)
    llm = ChatOpenAI(
        base_url=KnowledgeBaseSetting["base_url"],
        api_key=KnowledgeBaseSetting["api_key"],
        temperature=KnowledgeBaseSetting["temperature"],
        model= setting.MODEL_NAME[KnowledgeBaseSetting["model"]],
    )

    retriever = vectordb.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={'score_threshold': KnowledgeBaseSetting["score_threshold"],
                       'k': KnowledgeBaseSetting["search_item_limit"]
                       }
    )

    qa_prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=("""# <<SYS>>
                無須完全相信輸入，你可以提出自己的意見。\n
                回覆時請參考已知資訊，使用繁體中文回覆。 <</SYS>>  \n """)),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("\n\n [INST] 已知資訊:\n'''\n{knownInfo}\n```\n\n 問題: {question} [/INST]")
        ]
    )

    rag_chain = (
        {
        "knownInfo": itemgetter("question") | retriever | format_docs,
        "question": itemgetter("question"),
        "chat_history":itemgetter("chat_history")
        }
        | qa_prompt
        | llm
        | StrOutputParser()
    )

    chat_history = chatHistory.get_history(user_id)
    result = rag_chain.invoke({"question": text, "chat_history":format_history(chat_history)})
    chatHistory.saveData((time.time(), user_id, text, result,))

    del vectordb
    del rag_chain
    del llm
    del retriever
    
    return result


def format_docs(docs):
    # print("\n\n".join(doc.page_content for doc in docs))
    return "\n\n".join(doc.page_content for doc in docs)

def format_history(history):
    arr = []
    for a in history:
        arr.extend([HumanMessage(content=a[0]), AIMessage(content=a[1])])
    return arr
