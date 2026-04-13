import streamlit as st
import requests

st.title("🌾 AI Decision Support Assistant")

region = st.text_input("Enter Region")
query = st.text_area("Ask your question")

if st.button("Get Advice"):
    response = requests.get(
        "http://127.0.0.1:8000/ask",
        params={"region": region, "query": query}
    )
    
    st.write(response.json())