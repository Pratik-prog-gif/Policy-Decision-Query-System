import streamlit as st
import requests

BACKEND_URL = "https://policy-decision-making-backend-8.onrender.com"

st.set_page_config(page_title="LLM Query Frontend", layout="centered")
st.title("LLM-Powered Policy Decision Query System")

# File Upload Section
uploaded_file = st.file_uploader("Upload a policy, contract, or email", type=["pdf", "docx", "eml", "msg"])

if uploaded_file:
    st.info(f"Selected file: {uploaded_file.name}")
    with st.spinner("Uploading to backend..."):
        try:
            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
            }
            res = requests.post(f"{BACKEND_URL}/upload", files=files)

            if res.status_code == 200:
                st.success(res.json().get("message", "Upload successful!"))
            else:
                try:
                    error_msg = res.json().get("error", "Unknown error")
                except requests.exceptions.JSONDecodeError:
                    error_msg = res.text
                st.error(f"❌ Upload failed: {error_msg}")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Connection error: {e}")

# Query Input Section
st.subheader("Ask a question")
user_query = st.text_input("What would you like to ask about this document?")

if st.button("Submit Query") and user_query:
    with st.spinner("Querying LLM..."):
        try:
            res = requests.post(
                f"{BACKEND_URL}/query",
                json={"question": user_query}
            )

            if res.status_code == 200:
                result = res.json()
                st.success("Response received!")

                st.subheader("Structured Response")
                st.json(result["response"])

                with st.expander("Matched Clauses"):
                    matched_clauses = result.get("matched_clauses", [])
                    for i, clause in enumerate(matched_clauses[:3], 1):
                        st.markdown(f"**Clause {i}:**\n```\n{clause}\n```")

            else:
                try:
                    error_msg = res.json().get("error", "Unknown error")
                except requests.exceptions.JSONDecodeError:
                    error_msg = res.text
                st.error(f"❌ Query failed: {error_msg}")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Connection error: {e}")






