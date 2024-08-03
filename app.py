import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = "sk-proj-gPPoMvDVBOMCp0hXTpkNT3BlbkFJOXduQLtuhYeEw2AbciTY"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

st.title('홍보 포스터 만들기😍')

keyword = st.text_input("키워드를 입력하세요")

if st.button('생성하기'):
    with st.spinner('생성 중입니다.'):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": keyword,
                },
                {
                    "role": "system",
                    "content": "입력 받은 키워드에 대한 150자 이내의 솔깃한 제품 홍보 문구를 작성해줘.",
                }
            ],
            model="gpt-4o",
        )

    result = chat_completion.choices[0].message.content
    st.write(result)
