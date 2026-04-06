import streamlit as st
from main import analyze_workflow

# Page config
st.set_page_config(page_title="AI Workflow Optimizer", page_icon="🚀")

# Title
st.title("🚀 AI Workflow Optimizer")
st.markdown("Optimize your daily routines using AI")

# Input
user_input = st.text_area("Enter your workflow:", height=150)

# Button
if st.button("Analyze"):

    if user_input:
        with st.spinner("Analyzing your workflow..."):
            result = analyze_workflow(user_input)

        st.success("Analysis Complete!")
        st.markdown("## 📋 Results")

        # Split sections from AI output
        sections = result.split("\n\n")

        for section in sections:

            # 🔥 Add clean headers manually
            if "Inefficiencies" in section:
                st.markdown("### 🔴 Inefficiencies")
            elif "Improvements" in section:
                st.markdown("### 🟢 Improvements")
            elif "Optimized Workflow" in section:
                st.markdown("### ⚡ Optimized Workflow")
            elif "Productivity Score" in section:
                st.markdown("### 💡 Productivity Score")

            # 🔥 Remove duplicate headings from AI output
            cleaned = section.replace("Inefficiencies:", "") \
                .replace("Improvements:", "") \
                .replace("Optimized Workflow:", "") \
                .replace("Productivity Score:", "") \
                .strip()

            st.markdown(cleaned)

        # ✅ OUTSIDE LOOP (no repetition)
        st.info("💡 Small improvements daily = massive results over time.")

    else:
        st.warning("Please enter your workflow first.") 