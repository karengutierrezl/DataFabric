#  python3 -m streamlit run app06.py
# install streamlit = pip3 install streamlit
import json
import streamlit as st


def run_app():
    st.title(":eye::bee::m: Bienvenido al Consumo de Datos!")

    user_info = None
    with st.sidebar:
        user_name = st.text_input("Ingresa tu Usuario")
        st.button('Validar', on_click=click_button)


        if st.session_state.clicked:
            user_info = valida(user_name)
            if user_info is None:
                "El usuario No tiene acceso"


    if user_info:
        st.text(user_info)


def click_button():
    st.session_state.clicked = True

def valida(user_name):
    with open('users.json', 'r') as file:
        users_data = json.load(file)


    user_info = None
    for user in users_data['users']:
        if user.get('username').lower() == user_name.lower():
            user_info = user
            break
    return user_info


if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if True:
    run_app()