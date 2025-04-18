import streamlit as st
from langchain_openai import ChatOpenAI

st.title("🦜🔗 Ronald's ai chatbot")
# Sidebar met text input box waarin je API kan invoeren
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


# Variabele is nu object wat je vuld met Chatopenai class uit Langchain met API key
def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    response = model.invoke(input_text)
    st.info(response.content)  # Alleen


with st.form("my_form"):
    text = st.text_area(
        "Ask whatever you want to know",
        "Fill in your text",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
