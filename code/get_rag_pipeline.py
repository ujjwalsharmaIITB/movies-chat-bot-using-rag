# ChatModel
from get_chatbot import chat_model
# Prompt Templates for Model and RAG
from get_prompt_templates import movies_review_final_prompt, contextualize_movies_prompt
# retriever for RAG
from get_vector_database import movies_review_vector_database_retreiver

from langchain.schema.runnable import RunnablePassthrough

from langchain_core.output_parsers import StrOutputParser

from langchain.chains import create_history_aware_retriever


from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


# Context will be filled by the retriever and the question will be passed to the next step
# from theat the values of the context and question will be filled in movies_reviews_final_prompt
# that will be passed to the chat_model and the output will be parsed by the output_parser


output_parser  = StrOutputParser()

# This step is when you do not have chat history


# RAG_Chain = {
#     "context": movies_review_vector_database_retreiver,
#     "history": RunnablePassthrough(),
#     "question": RunnablePassthrough()
# } | movies_review_final_prompt | chat_model | output_parser


# For chat history we first create a subchain that will be used to get the chat history


# This chain prepends a rephrasing of the input query to our retriever, so that the retrieval incorporates the context of the conversation.

history_aware_retriever = create_history_aware_retriever(
    chat_model, movies_review_vector_database_retreiver, contextualize_movies_prompt
)


# And now we can build our full chain.

# Here we use create_stuff_documents_chain to generate a question_answer_chain,
# with input keys context, chat_history, and input-- it accepts the retrieved context alongside the conversation history and
#  query to generate an answer.



Movies_answering_chain = create_stuff_documents_chain(chat_model, movies_review_final_prompt)


RAG_Chain = create_retrieval_chain(history_aware_retriever, Movies_answering_chain)




























# # ChatModel
# from get_chatbot import chat_model
# # Prompt Templates for Model and RAG
# from get_prompt_templates import movies_review_final_prompt
# # retriever for RAG
# from get_vector_database import movies_review_vector_database_retreiver

# from langchain.schema.runnable import RunnablePassthrough

# from langchain_core.output_parsers import StrOutputParser



# # Context will be filled by the retriever and the question will be passed to the next step
# # from theat the values of the context and question will be filled in movies_reviews_final_prompt
# # that will be passed to the chat_model and the output will be parsed by the output_parser


# output_parser  = StrOutputParser()

# RAG_Chain = {
#     "context": movies_review_vector_database_retreiver,
#     "question": RunnablePassthrough()
# } | movies_review_final_prompt | chat_model | output_parser







