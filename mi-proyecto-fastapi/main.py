import zoneinfo
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hola Soy Ilya jeje, este es mi primer hola mundo en Python con FastAPI ٩(˘◡˘)۶"}


country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
    "CL": "America/Santiago",
    "EC": "America/Guayaquil",
    "UY": "America/Montevideo",
    "PA": "America/Panama",
    "CR": "America/Costa_Rica",
    "GT": "America/Guatemala",
    "HN": "America/Tegucigalpa",
    "NI": "America/Managua",
    "SV": "America/El_Salvador",
    "DO": "America/Santo_Domingo",
    "VE": "America/Caracas",
    "PY": "America/Asuncion",
    "BO": "America/La_Paz",
    "GF": "America/Cayenne",
    "GP": "America/Guadeloupe",
    "MQ": "America/Martinique",
    "RE": "America/Reunion",
    "AW": "America/Aruba",
    "BQ": "America/Kralendijk",
    "CW": "America/Curacao"
}


@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    if timezone_str is None:
        return {"error": "Código de país no válido"}
    else:
        tz = zoneinfo.ZoneInfo(timezone_str)
        return {"timezone": timezone_str,
                "time": datetime.now(tz)}
        
@app.get("/timeFormat/{iso_code}")
async def timeformat(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    if timezone_str is None:
        return{"error": "Código de país no valido"}
    else:
        tz = zoneinfo.ZoneInfo(timezone_str)
        date_object  = datetime.strftime(datetime.now(tz), "%Y-%m-%d %H:%M:%S")
        return {"timezone": timezone_str,
                "time": date_object}    
    