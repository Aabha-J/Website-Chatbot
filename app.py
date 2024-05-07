import streamlit as st
from model import process_input

st.title("Website Query with Mistral")
st.write("Enter website urls seperated by new lines")
urls = st.text_area("URLs seperated by new lines")

st.write("What's your question")
question = st.text_input("Question")

if st.button("Ask"):
    with st.spinner("Loading"):
        anwser = process_input(urls, question)
        st.text_area("Anwser", value = anwser, disabled=True, height=100)