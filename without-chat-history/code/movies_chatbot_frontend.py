import streamlit as st

st.set_page_config(page_title="Movies Chatbot", page_icon="🎬", layout="centered")

st.title("Movies Chatbot")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

@st.cache_resource
def get_and_cache_chatbot_response_function():
    from movies_chatbot import get_chatbot_response
    return get_chatbot_response


get_chatbot_response = get_and_cache_chatbot_response_function()

# React to user input
if prompt := st.chat_input("Ask me anything about movies"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response, _ = get_chatbot_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


footer_html = """
<div style='text-align: center;'>
  <p>Developed with ❤️ by USharma</p>
</div>
"""

# Render the footer
st.markdown(footer_html, unsafe_allow_html=True)