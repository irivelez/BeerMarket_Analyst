# Setup Instructions

## Virtual Environment

This project uses `uv` with a virtual environment located at `.venv/`

### Activate the environment

```bash
source .venv/bin/activate
```

### Deactivate the environment

```bash
deactivate
```

### Run the project

```bash
# Make sure environment is activated first
source .venv/bin/activate

# Then run the main script
python main.py
```

## Installed Packages

- crewai (0.201.1)
- crewai-tools (0.75.0)
- langchain-openai (0.3.34)
- python-dotenv (1.1.1)
- Plus 168 dependencies

## Environment Variables

Make sure your `.env` file contains:
```
OPENAI_API_KEY=your_key_here
SERPER_API_KEY=your_key_here
```

## Python Version

Using Python 3.11.9 (via pyenv)
