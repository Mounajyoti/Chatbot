Structure of the project:

chatbot_project/
├── config/
│   ├── config.ini
│   └── base_prompt.txt
├── data/
│   └── information.txt
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── chatbot.py
│   └── models.py
├── utils/
│   ├── __init__.py
│   ├── file_reader.py
│   └── get_config.py
├── config.ini.sample
├── .gitignore
├── requirements.txt
└── main.py

Motive:

To build a chatbot that follows user-defined restrictions and answers questions based on information from a provided .txt document.

Files to add:

Add config.ini under config folder
Add information.txt file under data folder