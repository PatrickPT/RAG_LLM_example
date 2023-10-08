import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
import yaml

with open("config.yaml", "r") as yamlfile:
    config = yaml.load(yamlfile, Loader=yaml.FullLoader)

# import configuration from yaml
name = config[0]['config']['name']
info = config[0]['config']['info']
system_prompt = config[0]['config']['system_prompt']
api = config[0]['config']['api']

# Set Streamlit page configuration
st.set_page_config(page_title=name, page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)

# Set OpenAI API key
openai.api_key = st.secrets.openai_key

# Create main interface
st.title(name)
st.info(info, icon="📃")

# Initialize the chat messages history         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question"}
    ]

# Function to load data
@st.cache_resource(show_spinner=False) # data is cached in memory so limit the knowledge base according to your machine
def load_data():
    with st.spinner(text="Loading and indexing the provided data"):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True) # read recursively all directories 
        docs = reader.load_data() # load data and create docs
        service_context = ServiceContext.from_defaults(llm=OpenAI(model=api, temperature=0.5, system_prompt=system_prompt))# add a permanent service prompt which is added
        index = VectorStoreIndex.from_documents(docs, service_context=service_context) # create your vector database
        return index

# Load data and create the chat engine
index = load_data()
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

# User input and chat history
if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display chat history
for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Generate a response if the last message is not from the assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history