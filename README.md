# 🎈 Streamlit + LLM Examples App

Starter example for building a LLM app with Streamlit.

## Run it locally

- Download the ZIP-file `llm-examples` to your local `Downloads` folder
- Extract the ZIP file inside your `Downloads` folder
- Open your terminal (macOS) or your Anaconda Command Prompt (Win)
- Navigate into the Downloads folder:

```sh
cd Downloads
```
- Navigate into the llm-examples folder:

```sh
cd llm-examples
```

- Create a new Anaconda environment:

```sh
conda create -n llm-app python=3.11 pip
```

- Activate the environment

```sh
conda activate llm-app
```

- Install Python packages (this may take a while)

```sh
pip install streamlit openai ipykernel jupyter
```

- 🚀 Start the app

```sh
streamlit run Chatbot.py
```

## Run it in GitHub

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/kirenz/llm-examples?quickstart=1)