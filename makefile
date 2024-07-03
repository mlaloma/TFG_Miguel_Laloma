# Makefile para entrenar el modelo y desplegar la aplicación

VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
TRAIN_FILE = chatbot/train_chatbot.py
TEST_FILE = chatbot/test.py
CHATBOT = chatbot/chatbot.py

train: $(VENV)
    $(PYTHON) $(TRAIN_FILE)

test: $(VENV)
    $(PYTHON) $(TEST_FILE)

deploy: $(VENV)
    $(PYTHON) $(CHATBOT)
    $ docker-compose up -d

$(VENV):
    python3 -m venv $(VENV)
