import streamlit as st
from main import analyze_workflow

st.title("🚀 AI Workflow Optimizer")

user_input = st.text_area("Enter your workflow:")

if st.button("Analyze"):
    if user_input:
        result = analyze_workflow(user_input)
        st.write(result)