import os

os.environ["HF_HOME"] = "/home/ioeuser/chat/chat-tutorial/hf_cache"

from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

from langchain_huggingface import HuggingFacePipeline


# Define the pipeline for LLM

langchain_llm = HuggingFacePipeline.from_model_id(
    model_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    device=0,
    pipeline_kwargs={
        "max_new_tokens": 512,
        "top_k": 50,
        "temperature": 1,
        "do_sample": True,
    },
)


# define the chat model

chat_model = ChatHuggingFace(llm=langchain_llm)



