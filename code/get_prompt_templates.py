from langchain.prompts import PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate,  MessagesPlaceholder




# from langchain.prompts import PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate


movies_review_system_message_template_str = """Your job is to use movie reviews to answer questions about the movies.
Use the following context to answer questions.
Be as detailed as possible, but don't make up any information that's not from the context.
If you don't know an answer, say you don't know.

context = {context}
"""


movies_review_human_message_template_str = """question = {input}"""




movies_review_system_prompt = SystemMessagePromptTemplate(
    prompt = PromptTemplate(
        input_variables = ["context"],
        template = movies_review_system_message_template_str
    )
)



# we will create a contextualized prompt for the human to ask questions to incorporate chat history

from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

contextualize_movies_prompt_str = """Given a chat history and the latest user question \
which might reference context in the chat history, formulate a standalone question \
which can be understood without the chat history. Do NOT answer the question, \
just reformulate it if needed and otherwise return it as is."""


contextualize_movies_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_movies_prompt_str),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)




movies_review_human_prompt = HumanMessagePromptTemplate(
    prompt = PromptTemplate(
        input_variables = ["input"],
        template = movies_review_human_message_template_str
    )
)


messages = [movies_review_system_prompt, MessagesPlaceholder("chat_history"), movies_review_human_prompt]


movies_review_final_prompt = ChatPromptTemplate(
    input_variables = ["context", "input"],
    messages = messages
)
















































# from langchain.prompts import PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate


# movies_review_system_message_template_str = """Your job is to use movie reviews to answer questions about the movies.
# Use the following context to answer questions.
# Be as detailed as possible, but don't make up any information that's not from the context.
# If you don't know an answer, say you don't know.

# context = {context}
# """


# movies_review_human_message_template_str = """question = {question}"""




# movies_review_system_prompt = SystemMessagePromptTemplate(
#     prompt = PromptTemplate(
#         input_variables = ["context"],
#         template = movies_review_system_message_template_str
#     )
# )





# movies_review_human_prompt = HumanMessagePromptTemplate(
#     prompt = PromptTemplate(
#         input_variables = ["question"],
#         template = movies_review_human_message_template_str
#     )
# )


# messages = [movies_review_system_prompt, movies_review_human_prompt]


# movies_review_final_prompt = ChatPromptTemplate(
#     input_variables = ["context", "question"],
#     messages = messages
# )

