from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain_community.llms import Ollama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings.ollama import OllamaEmbeddings

CHUNCK_SIZE = 7500
OVERLAP = 100

def process_input(urls, question):
    local_model = Ollama(model = "mistral")

    #Geting info from url
    urls_list = urls.split("\n")
    docs = [WebBaseLoader(url).load() for url in urls_list]
    docs_list = [item for sublist in docs for item in sublist] 

    # docs_list = [] 

    # for sublist in docs:
    #     for item in sublist:
    #         docs_list.append(item)


    #Making chunks
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=CHUNCK_SIZE, chunk_overlap=OVERLAP)
    doc_splits = text_splitter.split_documents(docs_list)

    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=embeddings.ollama.OllamaEmbeddings(model='nomic-embed-text'),
    )
    retriever = vectorstore.as_retriever()

    #Perform RAG
    after_rag_template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    """

    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)

    after_rag_chain = (
        {"context":retriever, "question":RunnablePassthrough()}
        | after_rag_prompt
        | local_model
        | StrOutputParser()
    )

    return after_rag_chain.invoke(question)


        


