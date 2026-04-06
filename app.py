if st.button("Analyze"):
    if user_input:
        with st.spinner("Analyzing your workflow..."):
            result = analyze_workflow(user_input)

        st.success("Analysis Complete!")
        st.markdown("## 📋 Results")

        sections = result.split("\n\n")

        for section in sections:
            if "Inefficiencies" in section:
                st.markdown("### 🔴 Inefficiencies")
                st.markdown(section)
            elif "Improvements" in section:
                st.markdown("### 🟢 Improvements")
                st.markdown(section)
            elif "Optimized" in section:
                st.markdown("### ⚡ Optimized Workflow")
                st.markdown(section)
            elif "Score" in section:
                st.markdown("### 💡 Productivity Score")
                st.markdown(section)
            else:
                st.markdown(section)

        st.info("💡 Small improvements daily = massive results over time.")

    else:
        st.warning("Please enter your workflow first.")    