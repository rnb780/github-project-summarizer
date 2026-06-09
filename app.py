from fastapi import FastAPI, File, UploadFile
from chatbot_file import chatbot_fun
app = FastAPI()

@app.get("/")
def home():
    return {"message":"Bravo ! Ton serveur web marche"}

@app.post("/resume")
async def resume_file(file: UploadFile):
    texte_du_fichier = (await file.read()).decode("UTF-8")
    reponse = chatbot_fun(texte_du_fichier)
    return {"name_file" : file.filename , "texte_apercu" : texte_du_fichier[:100], "resume" : reponse}