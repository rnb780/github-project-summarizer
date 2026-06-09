import streamlit as st
import requests

st.title("Analysateur Github")
fichier_charge = st.file_uploader("Entrez votre fichier", type=["txt"])

if fichier_charge :
    with st.spinner("Analyse du fichier en cours, veuillez patienter"):
        files_envoye = {"file" : (fichier_charge.name, fichier_charge.getvalue(), "text/plain")}
        reponse = requests.post("http://127.0.0.1:8000/resume", files=files_envoye)
        conversion_reponse = reponse.json()
        recuperation_finale = conversion_reponse["resume"]
    st.write(recuperation_finale)
st.caption("rnb780/Ryan")