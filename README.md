# GPT WEB UI

A minimal, clean, and fast web-based interface to chat with OpenAI's GPT-3.5-Turbo or GPT-4 models. 
Built using [Gradio](https://www.gradio.app/) to simulate the look and feel of ChatGPT in your browser.

# Features

- Responsive and lightweight UI, optimized for speed and minimalism.
- Clean gray background with white text, inspired by ChatGPT's style.
- Uses OpenAI’s GPT-3.5 or GPT-4 via API.
- All messages are stored in-memory for the current session.
- No login, no tracking — just pure chat.

# Requirements

pip3 install openai | pip3 install gradio==4.15.0

# Usage

python3 web-ui.py

Sample output:

└─$ python3 web-ui.py 
* Running on local URL:  http://127.0.0.1:7860

To stop the service press Ctrl + C in terminal

# License 

This project is licensed under the MIT License
