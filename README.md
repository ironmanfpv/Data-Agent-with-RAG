# Data agent with RAG
 Sieve through structured and unstructured Data. Respond to Query. AI
 This repository is an exercise walkthrough, a proof of concept of information sieveing with prompts.
 Data Agent with Python coding. LLM (leverages llama_index), Pylance, Pandas.
 Use cases : Data ingestion Q&A, Augmented Chatbots, Knowledge agents, analytics. 

# Setup
1. Vs code/Terminal Command Prompt, To create the ai environment: For win: type: python -m venv ai 
2. To To activate the ai environment:
    -For win : type in command prompt: .\ai\Scripts\activate.bat ; Deactivate : replace activate -> deactivate
    -For mac : type: source ai/bin/activate

3. type in command prompt : pip3 install llama-index pypdf python-dotenv pandas (install python packages and dependencies)
4. create .env file with OPENAI_API_KEY , get API key and insert

# Create Agent
5. Gather data. Source type, csv, pdf, notes.
6. Write the main.py file 
    -Write imports.

7. Ctrl+Shift+P : Select Python interpreter --> choose Global, then run.
8. To activate ai environment, In command prompt, type : .\ai\Scripts\activate
9. Create note_engine.py
