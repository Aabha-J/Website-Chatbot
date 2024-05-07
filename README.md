# Chat with Websites

A chatbot that will parse website information and anwser questions only
based of the info from those websites. 

To run on your local computer clone the repo or download the files and 
follow the instructions in the [setup.txt files](https://github.com/Aabha-J/Website-Chatbot/blob/802b85ab524a88204644a9f52a043d7504f82501/setup.txt). The set up instructions are
also copied below for convenience

## Demo

### 1. Input Info
<img width="556" alt="image" src="https://github.com/Aabha-J/Website-Chatbot/assets/121515351/03ca8463-204c-4409-b94e-a73b293fd801">


### 2. Get Results


## Set Up

  1. Create a virtual enviorment (Optional but reccomended)
      In the command terminal (Don't use powershell)
      a. python -m venv name
      b.  source name/bin/activate -MacOS
          .\name\Scripts\activate  -Windows
  
  
  2. Install these packages with pip in your virtual enviorment
  
      pip install langchain
      pip install chromadb tiktoken
      pip install streamlit
      pip install beautifulsoup4
  
  
  3. Download ollama from https://ollama.com/
  
      Type this into your command terminal to get acess to these models
      ollama pull mistral
      ollama pull nomic-embed-text
