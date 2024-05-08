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
MODEL_NAME = "mistral"


def load_documents_from_urls(urls):
    urls_list = urls.split("\n")
    docs = [WebBaseLoader(url).load() for url in urls_list]
    return [item for sublist in docs for item in sublist]

def create_doc_splits(docs_list, chunk_size, overlap):
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=chunk_size, chunk_overlap=overlap)
    return text_splitter.split_documents(docs_list)

def initialize_vectorstore(doc_splits):
    return Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=OllamaEmbeddings(model='nomic-embed-text'),
    )

def perform_rag(retriever, question, local_model):
    after_rag_template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)
    after_rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | after_rag_prompt
        | local_model
        | StrOutputParser()
    )
    return after_rag_chain.invoke(question)

def process_input(urls, question):
    local_model = Ollama(model=MODEL_NAME)
    docs_list = load_documents_from_urls(urls)
    doc_splits = create_doc_splits(docs_list, chunk_size=CHUNCK_SIZE, overlap=OVERLAP)
    vectorstore = initialize_vectorstore(doc_splits)
    retriever = vectorstore.as_retriever()
    return perform_rag(retriever, question, local_model)


        


