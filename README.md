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

## 사용

1. 애플리케이션 실행

   ```bash
   python app.py
   ```

2. 콘솔에서 알려주는 대로 웹 브라우저에서 애플리케이션에 액세스.
   
3. OpenAI API 키를 입력 Enter. 애플리케이션은 챗봇 응답을 생성하기 위해 OpenAI API를 사용한다. 
  
4. PDF 업로드하면 미리보기가 표시된다. 

5. 챗봇에게 질문하거나 대화를 나눈다. 


This application was developed using https://www.analyticsvidhya.com/blog/2023/05/build-a-chatgpt-for-pdfs-with-langchain/
