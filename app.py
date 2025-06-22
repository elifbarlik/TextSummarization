import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/summarize"

def summarize_via_api(text):
    response = requests.post(API_URL, json={"text": text})
    if response.status_code == 200:
        return response.json()["summary"]
    else:
        return f"Error: {response.status_code} - {response.text}"
    
iface = gr.Interface(
    fn=summarize_via_api,
    inputs=gr.Textbox(lines=15, label="E-posta Metni"),
    outputs=gr.Textbox(label="Özet"),
    title="Gradio + FastAPI: E-Posta Özetleyici",
    description="Arka planda çalışan API ile metin özetleme"
)

iface.launch()
