# ChatModel
from get_chatbot import chat_model
# Prompt Templates for Model and RAG
from get_prompt_templates import movies_review_final_prompt
# retriever for RAG
from get_vector_database import movies_review_vector_database_retreiver

from langchain.schema.runnable import RunnablePassthrough

from langchain_core.output_parsers import StrOutputParser



# Context will be filled by the retriever and the question will be passed to the next step
# from theat the values of the context and question will be filled in movies_reviews_final_prompt
# that will be passed to the chat_model and the output will be parsed by the output_parser


output_parser  = StrOutputParser()

RAG_Chain = {
    "context": movies_review_vector_database_retreiver,
    "question": RunnablePassthrough()
} | movies_review_final_prompt | chat_model | output_parser







