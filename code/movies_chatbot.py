from get_rag_pipeline import RAG_Chain

def format_response(response: str) -> str:
    return response.split("<|assistant|>\n")[1].strip()


def get_chatbot_response(question: str) -> str:
    response = RAG_Chain.invoke(question)
    return format_response(response), response


def ask_question(question: str) -> str:
    response, _ = get_chatbot_response(question)
    print(response)

def get_chatbot_response_stream(question: str) -> str:
    for chunk in RAG_Chain.stream(question):
        yield chunk

