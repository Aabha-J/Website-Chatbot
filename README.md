# Chat with Websites :robot:

A chatbot that uses Mistral 7B to parse website information and anwser questions only
based of the info from those websites. However, you can modify 
`after_rag_template` to change this.

To run on your local computer clone the repo or download the files and 
follow the instructions in [setup.txt](https://github.com/Aabha-J/Website-Chatbot/blob/802b85ab524a88204644a9f52a043d7504f82501/setup.txt). 
The set up instructions are also copied below for convenience

## Demo

### 1. Input Info
<img width="556" alt="image" src="https://github.com/Aabha-J/Website-Chatbot/assets/121515351/03ca8463-204c-4409-b94e-a73b293fd801">

### 2. Wait for Results
<img width="562" alt="image" src="https://github.com/Aabha-J/Website-Chatbot/assets/121515351/8920dc7c-9a92-4e8f-a746-cde0a6159937">


### 3. Get Results
<img width="565" alt="image" src="https://github.com/Aabha-J/Website-Chatbot/assets/121515351/49864d24-bafa-4001-a875-1a93dbb4219a">


Note: Depedning on your processor the speed will vary
## Set Up

  1. Create a virtual enviorment (Optional but reccomended)
      In the command terminal (Don't use powershell)
     1. python -m venv name
     2. MAC: source name/bin/activate
     3. Windows: .\name\Scripts\activate  
  
  
  2. Install these packages with pip in your virtual enviorment
  
      pip install langchain
     
      pip install chromadb tiktoken
     
      pip install streamlit
     
      pip install beautifulsoup4
  
  
  3. Download ollama from https://ollama.com/
  
      Type this into your command terminal to get acess to these models
     
      ollama pull mistral
     
      ollama pull nomic-embed-text
4. streamlit run app.py
