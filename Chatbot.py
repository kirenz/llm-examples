# Import the necessary libraries
from openai import OpenAI  # OpenAI's Python client library
import streamlit as st  # Streamlit library for creating web apps

# Creating a sidebar in the Streamlit app
with st.sidebar:
    # Text input for OpenAI API Key, masked as a password for security
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

    # Dropdown for selecting the model
    model_choice = st.selectbox("Choose the Model", ["gpt-4-1106-preview", "gpt-3.5-turbo"])

    # Slider for adjusting the temperature of the model
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    # Links for additional resources and information
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/kirenz/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/kirenz/llm-examples?quickstart=1)"

# Define a system prompt with a specific persona and task description
system_prompt = "I am a sarcastic and mean AI with the name Sherlock. I am know-it-all and like to make fun of users' questions. I like to answer in riddles."

# Setting the title of the Streamlit web app
st.title("💬 Chatbot")
# Caption under the title explaining the app
st.caption("🚀 Sherlock: A streamlit chatbot powered by OpenAI LLM")

# Initialize the chat history if it doesn't exist in the session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": system_prompt}, {"role": "assistant", "content": "🤨 How can I help you?"}]

# Displaying each message in the chat history, except the hidden system prompt
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# Input field for user to enter their message
if prompt := st.chat_input():
    # Check if the OpenAI API key is entered, if not, prompt the user
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    # Initialize the OpenAI client with the API key
    client = OpenAI(api_key=openai_api_key)

    # Add the user's message to the session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display the user's message in the chat
    st.chat_message("user").write(prompt)

    # Generate a response from the selected OpenAI model with the specified temperature
    response = client.chat.completions.create(model=model_choice, messages=st.session_state.messages, temperature=temperature)
    # Extract the response content
    msg = response.choices[0].message.content

    # Add the assistant's response to the session state
    st.session_state.messages.append({"role": "assistant", "content": msg})
    # Display the assistant's response in the chat
    st.chat_message("assistant").write(msg)
