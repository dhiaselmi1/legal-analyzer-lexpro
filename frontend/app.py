import streamlit as st
import requests
import fitz  # PyMuPDF
import json
import io

st.set_page_config(page_title="⚖️ Legal Analyzer", layout="wide")

st.markdown("<h1 style='text-align: center;'>⚖️ Legal Document Intelligence Assistant</h1>", unsafe_allow_html=True)
st.markdown("Analyze contracts, extract clauses, named entities, and generate summaries using AI.")

# --- Sidebar Settings ---
st.sidebar.header("⚙️ Settings")
model_choice = st.sidebar.selectbox("Choose Model", ["mistral", "llama2"])

# --- Input Area ---
st.write("### 📥 Upload or Paste Your Legal Document")

input_method = st.radio("Select input type:", ["📋 Paste Text", "📄 Upload .txt", "📕 Upload .pdf"])

text_input = ""

if input_method == "📋 Paste Text":
    text_input = st.text_area("Paste your legal text here:", height=300)

elif input_method == "📄 Upload .txt":
    txt_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if txt_file:
        text_input = txt_file.read().decode("utf-8")

elif input_method == "📕 Upload .pdf":
    pdf_file = st.file_uploader("Upload a .pdf file", type=["pdf"])
    if pdf_file:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text_output = ""
        for page in doc:
            text_output += page.get_text()
        text_input = text_output

# --- Analyze Button ---
if st.button("🧠 Analyze Document"):
    if not text_input.strip():
        st.warning("Please provide or upload a legal document.")
    else:
        with st.spinner("Analyzing..."):
            try:
                response = requests.post(
                    "http://localhost:8000/analyze/",
                    data={
                        "text": text_input,
                        "model": model_choice.lower()  # ensure it's in lowercase for Ollama
                    }
                )

                results = response.json()

                st.success("✅ Analysis Complete!")

                # Display results
                with st.expander("📄 Summary"):
                    st.write(results["summary"])

                with st.expander("📌 Key Clauses"):
                    st.write(results["clauses"])

                with st.expander("🔍 Named Entities"):
                    st.write(results["entities"])

                # Export
                st.download_button(
                    label="⬇️ Download JSON",
                    data=json.dumps(results, indent=2),
                    file_name="legal_analysis.json",
                    mime="application/json"
                )

                st.download_button(
                    label="⬇️ Download Text Summary",
                    data=results["summary"],
                    file_name="legal_summary.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"An error occurred: {e}")
