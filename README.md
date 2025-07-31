# ai-agent

Experimental project to study and test **Large Language Models (LLMs)** using `transformers`, `torch`, `poetry`, and `pyenv`.

---

## Purpose

The goal of this project is to help a data engineer (like me 👋) understand how LLMs work in practice — from local execution to prompt construction, attention masks, and the differences between raw LLM use and conversational agents like ChatGPT.

---

## Project Setup

### Requirements

- Python installed via [`pyenv`](https://github.com/pyenv/pyenv)
- [`Poetry`](https://python-poetry.org/) installed (v2+)
- Git properly configured with your GitHub email

---

### Project Structure

```
ai-agent/
├── pyproject.toml
├── poetry.lock
├── .python-version
├── .gitignore
└── src/
    └── ai_agent/
        └── main.py
```

---

## Installation Steps

### 1. Clone the repository

```bash
git clone git@github.com:your-username/ai-agent.git
cd ai-agent
```

### 2. Set Python version with `pyenv`

```bash
pyenv install 3.11.8
pyenv local 3.11.8
```

### 3. Install dependencies with `poetry`

```bash
poetry install
```

> If the virtual environment is not inside the project, activate it manually:
>
> ```bash
> source $(poetry env info --path)/bin/activate
> ```

---

## main Dependencies

```bash
poetry add transformers torch accelerate
```

---

## ▶️ Running the Project

With the virtual environment active:

```bash
python src/ai_agent/main.py
```

Or using poetry:

```bash
poetry run python src/ai_agent/main.py
```

---

## Technical Explanation

### What is an LLM?

LLMs (**Large Language Models**) are AI models trained on billions of words and capable of understanding and generating natural language. Examples include GPT-2, GPT-3, GPT-4, LLaMA, and Mistral.

In this project, we use GPT-2 via the `transformers` library:

```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
```

This doesn't import billions of words directly, but loads **pretrained weights** that encode the learned knowledge from those words.

---

### LLM vs. ChatGPT (Conversational Agent)

| Feature                       | Raw LLM (as in code)                 | ChatGPT-style Agent                |
|------------------------------|--------------------------------------|------------------------------------|
| Conversation history         | ❌ No                                | ✅ Yes                              |
| Interface                    | Code-based                          | Chat-based                          |
| Context awareness            | Only current prompt                 | Uses full conversation context     |
| External tool access         | ❌ No                                | ✅ Yes (search, tools, plugins)     |

---

## Next Steps (to be implemented)

- [ ] Use Portuguese-trained models (`pierreguillou/gpt2-small-portuguese`)
- [ ] Test more advanced models like Mistral and LLaMA
- [ ] Integrate LangChain to build an agent
- [ ] Add RAG (retrieval-augmented generation)
- [ ] Build a simple web interface with Streamlit or FastAPI

---

## Author

**Gabriel Evangelista** — Data engineer with 7+ years of experience, learning how to apply AI and LLMs to real-world tasks like automation, data analysis, and intelligent systems.
