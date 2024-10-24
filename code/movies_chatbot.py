from get_rag_pipeline import RAG_Chain

from langchain_core.messages import HumanMessage



def format_response(response: str) -> str:
    return response.split("<|assistant|>\n")[-1].strip()


def get_chatbot_response(question: str, chat_history) -> str:
    response = RAG_Chain.invoke({
        "input": question,
        "chat_history": chat_history
    })

    model_response = response["answer"]

    # chat_history.extend([HumanMessage(content=question) , response["answer"]])

    return format_response(model_response), model_response


def ask_question(question: str) -> str:
    response, _ = get_chatbot_response(question)
    print(response)

def get_chatbot_response_stream(question: str) -> str:
    for chunk in RAG_Chain.stream(question):
        yield chunk




# see this to incorporacte chat history
# https://python.langchain.com/v0.1/docs/use_cases/question_answering/chat_history/#:~:text=We'll%20use%20a%20prompt,message%20containing%20the%20latest%20question.











# from get_rag_pipeline import RAG_Chain

# def format_response(response: str) -> str:
#     return response.split("<|assistant|>\n")[1].strip()


# def get_chatbot_response(question: str) -> str:
#     response = RAG_Chain.invoke(question)
#     return format_response(response), response


# def ask_question(question: str) -> str:
#     response, _ = get_chatbot_response(question)
#     print(response)

# def get_chatbot_response_stream(question: str) -> str:
#     for chunk in RAG_Chain.stream(question):
#         yield chunk

