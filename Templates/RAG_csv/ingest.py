from langchain.indexes import VectorstoreIndexCreator
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import FAISS

loader = CSVLoader("./titanic.csv")

docs = loader.load()
index_creator = VectorstoreIndexCreator(vectorstore_cls=FAISS)

index = index_creator.from_documents(docs)

index.vectorstore.save_local("titanic_data")
