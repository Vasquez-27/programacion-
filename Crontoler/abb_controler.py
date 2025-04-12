from model.pet import Pet
from service import abb_service
from fastapi import APIRouter, Response, status, HTTPException
from typing import Dict

abb_service = abb_service.ABBService()

abb_route = APIRouter(prefix="/abb")


# 1. Listar todas las mascotas
@abb_route.get("/", response_model=list[Pet])
async def get_pets_inorder():
    try:
        return abb_service.get_all()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.args[0])


# 2. Crear mascota
# @abb_route.post("/abb", status_code=201)
@abb_route.post("/", status_code=201)
async def create_pet(pet: Pet, response: Response):
    try:
        abb_service.abb.add(pet)
        return {"message": "Mascota añadida exitosamente"}
    except ValueError as ve:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {"message": f"Datos inválidos: {ve.args[0]}"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": e.args[0]}


# 3. Actualizar mascota
@abb_route.put("/{id}")
async def update_pet(id: int, pet: Pet, response: Response):
    try:
        abb_service.abb.update(pet, id)
        return {"message": "Mascota actualizada exitosamente"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": e.args[0]}


# 4. Eliminar mascota
@abb_route.delete("/{id}")
async def delete_pet(id: int, response: Response):
    try:
        abb_service.delete(id)
        return {"message": f"Mascota con id {id} eliminada correctamente"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": e.args[0]}


# 5. Contar mascotas por raza
@abb_route.get("/count-by-breed", response_model=Dict[str, int])
async def count_by_breed():
    try:
        return abb_service.count_by_breed()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.args[0])


# 6. Listar solo los IDs de las mascotas
@abb_route.get("/ids", response_model=list[int])
async def list_pet_ids():
    try:
        return abb_service.get_ids()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.args[0])


# 7. Listar mascotas en preorden
@abb_route.get("/preorder", response_model=list[Pet])
async def get_pets_preorder():
    try:
        return abb_service.get_preorder()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.args[0])


# 8. Listar mascotas en postorden
@abb_route.get("/postorder", response_model=list[Pet])
async def get_pets_postorder():
    try:
        return abb_service.get_postorder()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.args[0])


@abb_route.get("/report-by-location-gender")
async def report_location_gender():
    try:
        return abb_service.report_by_location_and_gender()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.args[0])

@abb_route.get("/average-age-by-gender")
async def average_age_by_gender():
    try:
        return abb_service.average_age_by_gender()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.args[0])
