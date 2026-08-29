from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


data = PyPDFLoader("document loaders/GRU.pdf")#has 14 pages

docs = data.load() #docs 0 1 2 .. 14 docs full array or the list
#doc[0] one page 

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap=10
)

chunks = splitter.split_documents(docs)

print(chunks[0].page_content)

#PyPDFLoader this will store the page 1 page is oone document so stores
# this thing print(docs[14]) prints the last page#