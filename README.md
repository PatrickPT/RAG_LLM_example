[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

# Knowledge Bot with Retrieval Augmented Generation

## Overview

The **Knowledge Bot** is a web-based chatbot that provides information and answers questions related to any data which is given as context based on Retrieval Augmented Generation Architecture. It utilizes the `llama_index` library for data indexing and OpenAI's GPT-3.5-Turbo model for generating responses.

The chatbot is designed to assist users in finding information by answering questions based on indexed documents.

## Features

- Ask questions related to your indexed documents.
- Receive informative responses based on indexed data.
- Convenient web-based interface powered by Streamlit.

## Getting Started

To run the Knowledge Bot locally with docker, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/PatrickPT/RAG_LLM_example.git

2. Create your OpenAI Key

   ```bash
   cd RAG_LLM_example
   cd .streamlit
   nano .streamlit/secrets.toml
   # Insert your API Key as openai_key = "API Key" and save

3. Create your documents or change the input_dir parameter in config.yaml to your folder(which needs to be accessible from the docker container)

   ```bash
   cd data
   # Insert the contextual documents the LLM should use in that folder

4. Change the `config.yaml` file accordingly to your prior changes

5. Run docker compose

   ```bash
   docker compose up -d

PS: content in `/.streamlit` and `/data` is ignored by git.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to reach out.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgments

This project relies on the llama_index library for data indexing and retrieval and streamlit for the frontend.
It uses OpenAI's GPT-3.5-Turbo model for natural language understanding and generation.

## Contact

If you have any questions or feedback, feel free to reach out.
