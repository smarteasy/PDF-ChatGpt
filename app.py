import gradio as gr
import os
from user_interface import create_demo
# user_interface.py의 create_demo 함수- gradio로 ui를 만들고, 만들어진 ui 구성요소들을 리턴한다. 
from logic import set_api_key, enable_api_box, add_text, generate_response, render_file

demo, api_key, change_api_key, chatbot, show_img, txt, submit_btn, btn = create_demo()

# Set up event handlers
with demo:
    # Event handler for submitting the OpenAI API key
    api_key.submit(set_api_key, inputs=[api_key], outputs=[api_key])

    # Event handler for changing the API key
    change_api_key.click(enable_api_box, outputs=[api_key])

    # Event handler for uploading a PDF
    btn.upload(render_file, inputs=[btn], outputs=[show_img])

    # Event handler for submitting text and generating response
    submit_btn.click(add_text, inputs=[chatbot, txt], outputs=[chatbot], queue=False).\
        success(generate_response, inputs=[chatbot, txt, btn], outputs=[chatbot,txt]).\
        success(render_file, inputs=[btn], outputs=[show_img])

if __name__ == "__main__":
    demo.launch()

