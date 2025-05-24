import streamlit as st
from langchain_community.llms import OpenAI
st.title("Quickstart app")
open_ai_api_key = st.sidebar.text_input("OpenAI API Key")
def generate_response (input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=open_ai_api_key)
    st.info(llm(input_text))
with st.form(key='my_form'):
    text = st.text_area("Enter your text here")
    submitted = st.form_submit_button("Submit")
    if not open_ai_api_key.startswith("sk-"):
        st.warning("Please enter a valid OpenAI API key.")
    if submitted and open_ai_api_key.startswith("sk-"):
     generate_response(text)
    
