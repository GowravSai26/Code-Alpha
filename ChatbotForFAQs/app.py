import streamlit as st
from chatbot import get_answer

st.set_page_config(page_title="FAQ Chatbot", layout="centered")

st.title("🤖 FAQ Chatbot")
st.write("Ask any question related to the product/service:")

user_input = st.text_input("Your Question")

if st.button("Get Answer"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = get_answer(user_input)
        st.success(response)
