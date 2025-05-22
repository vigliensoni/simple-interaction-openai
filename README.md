# simple-interaction-openai

(Very) simple chatbot application with OpenAI API.

# Installation

After cloning the repository:

```
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate 

# Install required libraries
pip3 install openai

# Run code
python3 chat.py
```

Your API key should be set in the OPENAI_API_KEY environment variable

Temporary (for current terminal session)

``` bash
# macOS / Linux:
export OPENAI_API_KEY=your-api-key-here

# Windows (Command Prompt):
set OPENAI_API_KEY=your-api-key-here

# Windows (PowerShell):
$env:OPENAI_API_KEY="your-api-key-here"
```