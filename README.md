# ml_autogen_compulsory
Make an agent that can generate and execute and thereby verifing the python code

## Requirements

- Python 3.10+
- autogen
- ollama
- fix-busted-json

start by clone or download the source code
```bash
git clone https://github.com/Andylaa10/ml_autogen_compulsory
```

## Setup virtual environment
creating env
ex: name = myenv
```bash
python -m venv name
```

## activate env by running the activate script
```bash
name\Scripts\activate
```

## Setup dependencies

Install the Python dependencies.

```bash
pip install -r requirements.txt
```

> [!NOTE]
> Remember to open docker, because our agent is use docker to execute the generated code

## Run the program by giving a prompt

ex: prompt = "Write a Python function that takes a list of numbers and returns the average of the numbers."
```bash
python run main.py prompt 
```

> [!NOTE]
> The model used in this project is mistral:latest so make sure that you have both ollama and mistral:latest downloaded

### download ollama model
https://ollama.com/library/mistral
