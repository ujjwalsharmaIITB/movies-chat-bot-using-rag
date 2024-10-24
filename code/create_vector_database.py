from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import Chroma

# Define the model name

model_name = "mixedbread-ai/mxbai-embed-large-v1"


hf_embeddings = HuggingFaceEmbeddings(model_name=model_name)

movies_review_dataset_path = "/workspaces/movies-chat-bot-using-rag/data/IMDB-Movie-Dataset(2023-1951).csv"

chroma_data_path = "chroma_data"

loader = CSVLoader(file_path=movies_review_dataset_path, source_column="overview")

movies_reviews = loader.load()

print("Starting")
movies_review_vector_database = Chroma.from_documents(
    movies_reviews , hf_embeddings, persist_directory= chroma_data_path
)

print("Done")






