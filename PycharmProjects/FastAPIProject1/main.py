from fastapi import FastAPI
from controller import abb, add_pet, list_pets

app = FastAPI()

app.post("/add")(add_pet)
app.get("/list")(list_pets)

