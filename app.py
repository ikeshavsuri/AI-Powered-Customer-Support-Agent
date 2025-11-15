import gradio as gr
from app.agent import handle_message

def chat_fn(user_message):
    out = handle_message(user_message)
    reply = out["reply"]
    trace = out["trace"]
    # Format trace for display (optional)
    trace_str = "\n".join([f'{t["action"]}: {t["output"]}' for t in trace])
    return reply, trace_str

with gr.Blocks() as demo:
    gr.Markdown("# Customer Support AI Agent")
    inp = gr.Textbox(placeholder="Type customer message here...", lines=2)
    out1 = gr.Textbox(label="Agent Reply", lines=6)
    out2 = gr.Textbox(label="Trace (debug)", lines=10)
    btn = gr.Button("Send")
    btn.click(chat_fn, inputs=inp, outputs=[out1, out2])

if __name__ == "__main__":
    demo.launch()
