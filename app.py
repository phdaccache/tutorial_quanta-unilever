import streamlit as st
from firebase_connection.firebase import connectFirebase

connectFirebase()

db = st.session_state['db']
storage = st.session_state['storage']

dic = {
    "Ellen": 3
}

db.child("Usuarios").push(dic)

storage.child("Imagem-top").put("Logo-Atalho.png")

st.selectbox("Teste", ["Opa"])