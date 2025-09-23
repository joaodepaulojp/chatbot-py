import streamlit as st 
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

modelo = OpenAI(api_key=openai_api_key)

st.write("### ChatBot com IA")

#session_state = memória do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

#exibir histórico
for msg in st.session_state["lista_mensagens"]:
    role = msg["role"]
    content = msg["content"]
    st.chat_message(role).write(content)

#pegar input
user_input = st.chat_input("Digite sua mensagem aqui")

if user_input:
    st.chat_message("user").write(user_input)
    msg = {"role": "user", "content": user_input}
    st.session_state["lista_mensagens"].append(msg)

    response = modelo.chat.completions.create(
        messages = st.session_state["lista_mensagens"],
        model="gpt-4o",
    )

    response_ia = response.choices[0].message.content

    #exibir resposta da ia na tela
    st.chat_message("assistant").write(response_ia)
    msg = {"role": "assistant", "content": response_ia}
    st.session_state["lista_mensagens"].append(msg)