# GenAI has APIs, business logic, front end
# GenAI application will have two types of API
    # One for LLM
    # Other for data base
# Streamlit will be used to make front end prototype using pure python
# pip install streamlit (to install streamlit)
# streamlit --version   (to check installed version of streamlit)
# streamlit hello       (to run streamlit server)

import streamlit as st  # imported package streamlt and nicknamed it st

st.text("Hello World")
st.write("Write text")
st.title("Title Text")
st.markdown("# Markdown Heading")

st.latex(r''' e^{i\pi} + 1 = 0 ''') # latex is used by researchers to write research papers

st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

st.video("https://www.youtube.com/watch?v=LDogywz0FTU&list=PL0vKVrkG4hWoulA3tVDU3PoCalDm6I_eh&index=6") # youtube video link


