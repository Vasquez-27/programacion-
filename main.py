from fastapi import FastAPI
from Crontoler.abb_controler import abb_route


app = FastAPI()

# Incluir el router con el prefijo /abb ya definido
app.include_router(abb_route)


# Puedes agregar una ruta raíz opcional para verificar el estado del API
@app.get("/")
def read_root():
    return {"message": "API de mascotas con ABB funcionando"}