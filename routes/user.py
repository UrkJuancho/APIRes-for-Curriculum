from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.user import basicDataEntity, basicDataList, xpDataEntity, xpDataList, schoolarDataEntity, schoolarDataList
from models.user import basicData, xpData, schoolarData
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

# Manejo de basicData (Información Personal)

@user.get("/allPersonalData", tags=["Información Personal"])
def find_all_basic_data():
    data = basicDataList(conn.dataForCurriculum.personalData.find())
    return {
        "ok": True,
        "details": "Información personal",
        "body": data
    }


@user.post("/createPersonalData", tags=["Información Personal"])
def create_basic_data(data: basicData):
    new_data = dict(data)
    del new_data["id"]  # MongoDB genera el ID
    id = conn.dataForCurriculum.personalData.insert_one(new_data).inserted_id
    user_data = conn.dataForCurriculum.personalData.find_one({"_id": id})
    return {
        "ok": True,
        "details": "Información personal creada",
        "body": basicDataEntity(user_data)
    }


@user.get("/findPersonalData/{id}", tags=["Información Personal"])
def find_basic_data(id: str):
    user_data = conn.dataForCurriculum.personalData.find_one({"_id": ObjectId(id)})
    if user_data:
        return {
            "ok": True,
            "details": "Información personal",
            "body": basicDataEntity(user_data)
        }
    return {"ok": False, "details": "Usuario no encontrado"}


@user.put("/updatePersonalData/{id}", tags=["Información Personal"])
def update_basic_data(id: str, data: basicData):
    updated_data = conn.dataForCurriculum.personalData.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(data)}
    )
    if updated_data:
        return {
            "ok": True,
            "details": "Información personal actualizada",
            "body": basicDataEntity(conn.dataForCurriculum.personalData.find_one({"_id": ObjectId(id)}))
        }
    return {"ok": False, "details": "Error al actualizar los datos"}


@user.delete("/deletePersonalData/{id}", tags=["Información Personal"])
def delete_basic_data(id: str):
    conn.dataForCurriculum.personalData.find_one_and_delete({"_id": ObjectId(id)})
    return {
        "ok": True,
        "details": "Información personal eliminada"
    }

# Manejo de xpData (Experiencia Laboral)

@user.get("/allXpData", tags=["Experiencia Laboral"])
def find_all_xp_data():
    data = xpDataList(conn.dataForCurriculum.xpData.find())
    return {
        "ok": True,
        "details": "Experiencia laboral",
        "body": data
    }


@user.post("/createXpData", tags=["Experiencia Laboral"])
def create_xp_data(data: xpData):
    new_data = dict(data)
    id = conn.dataForCurriculum.xpData.insert_one(new_data).inserted_id
    xp_data = conn.dataForCurriculum.xpData.find_one({"_id": id})
    return {
        "ok": True,
        "details": "Experiencia laboral creada",
        "body": xpDataEntity(xp_data)
    }


@user.get("/findXpData/{id}", tags=["Experiencia Laboral"])
def find_xp_data(id: str):
    xp_data = conn.dataForCurriculum.xpData.find_one({"_id": ObjectId(id)})
    if xp_data:
        return {
            "ok": True,
            "details": "Experiencia laboral",
            "body": xpDataEntity(xp_data)
        }
    return {"ok": False, "details": "Experiencia no encontrada"}


@user.put("/updateXpData/{id}", tags=["Experiencia Laboral"])
def update_xp_data(id: str, data: xpData):
    conn.dataForCurriculum.xpData.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(data)}
    )
    return {
        "ok": True,
        "details": "Experiencia laboral actualizada",
        "body": xpDataEntity(conn.dataForCurriculum.xpData.find_one({"_id": ObjectId(id)}))
    }


@user.delete("/deleteXpData/{id}", tags=["Experiencia Laboral"])
def delete_xp_data(id: str):
    conn.dataForCurriculum.xpData.find_one_and_delete({"_id": ObjectId(id)})
    return {
        "ok": True,
        "details": "Experiencia laboral eliminada"
    }

# Manejo de schoolarData (Datos Académicos)

@user.get("/allSchoolarData", tags=["Datos Académicos"])
def find_all_schoolar_data():
    data = schoolarDataList(conn.dataForCurriculum.schoolarData.find())
    return {
        "ok": True,
        "details": "Datos académicos",
        "body": data
    }


@user.post("/createSchoolarData", tags=["Datos Académicos"])
def create_schoolar_data(data: schoolarData):
    new_data = dict(data)
    id = conn.dataForCurriculum.schoolarData.insert_one(new_data).inserted_id
    schoolar_data = conn.dataForCurriculum.schoolarData.find_one({"_id": id})
    return {
        "ok": True,
        "details": "Datos académicos creados",
        "body": schoolarDataEntity(schoolar_data)
    }


@user.get("/findSchoolarData/{id}", tags=["Datos Académicos"])
def find_schoolar_data(id: str):
    schoolar_data = conn.dataForCurriculum.schoolarData.find_one({"_id": ObjectId(id)})
    if schoolar_data:
        return {
            "ok": True,
            "details": "Datos académicos",
            "body": schoolarDataEntity(schoolar_data)
        }
    return {"ok": False, "details": "Datos académicos no encontrados"}


@user.put("/updateSchoolarData/{id}", tags=["Datos Académicos"])
def update_schoolar_data(id: str, data: schoolarData):
    conn.dataForCurriculum.schoolarData.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(data)}
    )
    return {
        "ok": True,
        "details": "Datos académicos actualizados",
        "body": schoolarDataEntity(conn.dataForCurriculum.schoolarData.find_one({"_id": ObjectId(id)}))
    }


@user.delete("/schoolarData/{id}", tags=["Datos Académicos"])
def delete_schoolar_data(id: str):
    conn.dataForCurriculum.schoolarData.find_one_and_delete({"_id": ObjectId(id)})
    return {
        "ok": True,
        "details": "Datos académicos eliminados"
    }
