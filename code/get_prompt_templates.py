from langchain.prompts import PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate


movies_review_system_message_template_str = """Your job is to use movie reviews to answer questions about the movies.
Use the following context to answer questions.
Be as detailed as possible, but don't make up any information that's not from the context.
If you don't know an answer, say you don't know.

context = {context}
"""


movies_review_human_message_template_str = """question = {question}"""




movies_review_system_prompt = SystemMessagePromptTemplate(
    prompt = PromptTemplate(
        input_variables = ["context"],
        template = movies_review_system_message_template_str
    )
)





movies_review_human_prompt = HumanMessagePromptTemplate(
    prompt = PromptTemplate(
        input_variables = ["question"],
        template = movies_review_human_message_template_str
    )
)


messages = [movies_review_system_prompt, movies_review_human_prompt]


movies_review_final_prompt = ChatPromptTemplate(
    input_variables = ["context", "question"],
    messages = messages
)

