from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Define the model name

model_name = "mixedbread-ai/mxbai-embed-large-v1"


hf_embeddings = HuggingFaceEmbeddings(model_name=model_name)

chroma_data_path = "chroma_data"


movies_review_vector_database = Chroma(
    persist_directory=chroma_data_path,
    embedding_function=hf_embeddings
)

movies_review_vector_database_retreiver = movies_review_vector_database.as_retriever(k=5)

