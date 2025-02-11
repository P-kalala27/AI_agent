import gradio as gr
from models.hugging_api import query_hugging_api
from memory.memory import memory

def chatbot(user_input):
    history = memory.get_history()
    full_prompt= f"{history}\nUser: {user_input}\nAI:"
    response = query_hugging_api(full_prompt)
    memory.add_message(user_input, response)
    return response

app = gr.Interface(fn=chatbot, inputs="text", outputs="text", title="Mon Agent AI", description="Ask anything you want")
app.launch()
