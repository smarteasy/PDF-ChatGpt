# PDF-ChatGpt

PDF 업로드, PDF와 상호작용. 사용자 입력에 답변을 생성한다. 


Langchain, Gradio, OpenAI API, ChromaDB가 사용된다. 
https://www.gradio.app/

pdf 업로드 미리보기가 가능하고, OpenAI API키를 쉽게 업로드할 수 있고 챗이 가능하다. 

[데모](https://youtu.be/ARVCUIxr5u0)

## 설치

1. Clone the repository:

   ```bash
   git clone https://github.com/ayushwattal/PDF-ChatGpt.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Access the application in your web browser as specified in the console.

3. Enter your OpenAI API key in the provided input box and press enter.

4. To preview a PDF file, click the "Upload PDF" button and select the PDF file from your local machine. The application will display a preview of the PDF file.

5. Use the chatbox to ask questions or have a conversation with the chatbot. The chatbot will generate responses based on the input.


## Configuration

- The application uses the OpenAI API for generating chatbot responses. Make sure to provide a valid OpenAI API key.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

This application was developed using https://www.analyticsvidhya.com/blog/2023/05/build-a-chatgpt-for-pdfs-with-langchain/
