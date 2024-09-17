# schemas/user.py
def basicDataEntity(item) -> dict:
    return {
        "name": item["name"],
        "typeDoc": item["typeDoc"],
        "numberDoc": item["numberDoc"],
        "dateBirthday": item["dateBirthday"],
        "numberPhone": item["numberPhone"],
        "email": item["email"]
    }

def basicDataList(entities) -> list:
    return [basicDataEntity(item) for item in entities]

def xpDataEntity(item) -> dict:
    return {
        "company": item["company"],
        "datetime": item["datetime"],
        "position": item["position"]
    }

def xpDataList(entities) -> list:
    return [xpDataEntity(item) for item in entities]

def schoolarDataEntity(item) -> dict:
    return {
        "institute": item["institute"],
        "datetime": item["datetime"],
        "schoolarTitle": item["schoolarTitle"]
    }

def schoolarDataList(entities) -> list:
    return [schoolarDataEntity(item) for item in entities]
