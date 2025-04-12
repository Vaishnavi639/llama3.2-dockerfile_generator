import streamlit as st
from generate_dockerfile import generate_dockerfile

st.set_page_config(page_title="Dockerfile Generator", page_icon="🐳", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .stTextInput>div>div>input, .stTextArea>div>textarea {
            border-radius: 8px;
            border: 1px solid #ccc;
            padding: 0.5rem;
        }
        .stButton>button {
            background-color: #0066cc;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            margin-top: 1rem;
        }
        .copy-button {
            background-color: #4CAF50;
            color: white;
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🐳 Dockerfile Generator")
st.write("Generate a best-practice multi-stage Dockerfile by entering your application's language and framework.")

language = st.text_input("Programming Language", placeholder="e.g. Python, Java, Node.js")
framework = st.text_input("Framework (optional)", placeholder="e.g. Flask, Spring Boot, Express")

if st.button("Generate Dockerfile"):
    with st.spinner("Generating your Dockerfile..."):
        dockerfile = generate_dockerfile(language, framework)
        st.success("Dockerfile generated successfully!")
                                                                                                                                                                      1,22          Top

