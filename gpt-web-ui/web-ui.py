import openai
import gradio as gr


openai.api_key = "YOUR_API_KEY_HERE" 

def chatgpt(message, history):
    messages = [{"role": "system", "content": "You are an expert in cybersecurity and software."}]
    
    for msg in history:
        messages.append({"role": "user", "content": msg["content"]}) if msg["role"] == "user" else messages.append({"role": "assistant", "content": msg["content"]})
    
    messages.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response["choices"][0]["message"]["content"]
    return reply

chat_ui = gr.ChatInterface(
    fn=chatgpt,
    title="GPT - WEB UI ASSISTANCE",
    description="Instantly ask gpt when you are stuck in the terminal or get an error.",
    theme="soft", 
    type="messages" 
)

chat_ui.launch()
