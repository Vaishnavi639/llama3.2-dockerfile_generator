# 🐳 AI-Powered Dockerfile Generator using LLaMA 3.2

This project leverages Meta's LLaMA 3.2 model locally via Ollama to automatically generate efficient **multi-stage Dockerfiles** based on the user's selected programming language or framework. It features a clean and easy-to-use **Streamlit UI** where users can interactively generate Dockerfiles for their applications.

---

## 🚀 Features

- 🤖 Powered by LLaMA 3.2 using Ollama
- 🐍 Python-based backend for prompt formatting and model interaction
- 🌐 Streamlit frontend for user interaction
- 🧱 Multi-stage Dockerfile generation
- 🖥️ Runs fully locally (no external API calls)

---

## 🛠️ Technologies Used

- [LLaMA 3.2](https://ollama.com/library/llama3)
- [Ollama](https://ollama.com/)
- Python
- Streamlit

---

## 🧠 How It Works

1. User selects a **programming language** or **framework** (e.g., Python, Node.js, Go).
2. A formatted prompt is sent to the locally running LLaMA 3.2 model using Ollama.
3. The model responds with a **multi-stage Dockerfile**.
4. The result is displayed in the Streamlit UI.

---

## 🏃 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Vaishnavi639/llama3.2-dockerfile_generator
cd local-setup
