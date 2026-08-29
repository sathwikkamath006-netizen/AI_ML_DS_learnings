#load pdf 
#split into chunks 
#create the embeddings 
#store into chroma 
#this main.py and createdb are the 2 files related to each other
#here deep learning book is loaded inside the file then db chromadb created
#then using that chromadb and creating the rest of the thing
#app.py is the ui
# chroma_documents creating new vecotor db only chroma means adding the existing one#
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings 
from langchain_community.vectorstores import Chroma 
from dotenv import load_dotenv

load_dotenv()

data = PyPDFLoader("document loaders/deeplearning.pdf")
docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = splitter.split_documents(docs)

embedding_model = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(
    documents= chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)
