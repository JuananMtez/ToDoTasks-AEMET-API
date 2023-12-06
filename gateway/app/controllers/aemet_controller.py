from fastapi import APIRouter, Depends, HTTPException, Response
import requests
from fastapi.responses import FileResponse, StreamingResponse

aemet_controller = APIRouter(
    prefix="/aemet",
    tags=["aemet"])

token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqdWFuYW50b25pby5tYXJ0aW5lemxAdW0uZXMiLCJqdGkiOiI2OGUxMmY3NS00OWYxLTQ1NWUtYTgxYy1iYzQxYTc0YzY2YzUiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTY3NzA1ODkzNywidXNlcklkIjoiNjhlMTJmNzUtNDlmMS00NTVlLWE4MWMtYmM0MWE3NGM2NmM1Iiwicm9sZSI6IiJ9.gO-iH4empGfepVE4h1Lyc6P-fROhPTDnS_wcRxuM8KU'
url = 'https://opendata.aemet.es/opendata/api'
querystring = {"api_key":f"{token}"}
headers = {
    'cache-control': "no-cache"
    }


@aemet_controller.get("/prediccion/especifica/montaña/pasada/area/nev1")
def get_sierra_nevada_prediction_last_24_36_hours():
    response = requests.get(f'{url}/prediccion/especifica/montaña/pasada/area/nev1', headers=headers, params=querystring)
    obj = {}
    if response.status_code == 200:
        response_datos = requests.get(response.json()['datos'])
        obj['datos'] = response_datos.json()
        response_metadatos = requests.get(response.json()['metadatos'])
        obj['metadatos'] = response_metadatos.json()
        return obj

    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Peticion sin datos")
    elif response.status_code == 429:
        raise HTTPException(status_code=429, detail="Peticion que sobrepasa los limites del servicio")


@aemet_controller.get("/api/prediccion/especifica/montaña/pasada/area/nev1/dia/hoy")
def get_sierra_nevada_prediction_today():
    response = requests.get(f'{url}/prediccion/especifica/montaña/pasada/area/nev1/dia/0', headers=headers, params=querystring)
    obj = {}
    if response.status_code == 200:
        response_datos = requests.get(response.json()['datos'])
        obj['datos'] = response_datos.json()
        response_metadatos = requests.get(response.json()['metadatos'])
        obj['metadatos'] = response_metadatos.json()
        return obj

    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Peticion sin datos")
    elif response.status_code == 429:
        raise HTTPException(status_code=429, detail="Peticion que sobrepasa los limites del servicio")


@aemet_controller.get("/api/prediccion/especifica/montaña/pasada/area/nev1/dia/mañana")
def get_sierra_nevada_prediction_tomorrow():
    response = requests.get(f'{url}/prediccion/especifica/montaña/pasada/area/nev1/dia/1', headers=headers, params=querystring)
    obj = {}
    if response.status_code == 200:
        response_datos = requests.get(response.json()['datos'])
        obj['datos'] = response_datos.json()
        response_metadatos = requests.get(response.json()['metadatos'])
        obj['metadatos'] = response_metadatos.json()
        return obj

    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Peticion sin datos")
    elif response.status_code == 429:
        raise HTTPException(status_code=429, detail="Peticion que sobrepasa los limites del servicio")


@aemet_controller.get("/api/prediccion/especifica/murcia/hoy")
def get_murcia_prediction_today():
    response = requests.get(f'{url}/prediccion/especifica/municipio/diaria/30030', headers=headers, params=querystring)
    obj = {}
    if response.status_code == 200:
        response_datos = requests.get(response.json()['datos'])
        obj['datos'] = response_datos.json()
        response_metadatos = requests.get(response.json()['metadatos'])
        obj['metadatos'] = response_metadatos.json()
        return obj

    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Peticion sin datos")
    elif response.status_code == 429:
        raise HTTPException(status_code=429, detail="Peticion que sobrepasa los limites del servicio")

@aemet_controller.get("/api/prediccion/especifica/uvi/hoy")
def get_uvi_radiaction_prediction_today():
    response = requests.get(f'{url}/prediccion/especifica/uvi/0', headers=headers, params=querystring)
    obj = {}
    if response.status_code == 200:
        response_datos = requests.get(response.json()['datos'])
        print(response_datos.text)
        obj['datos'] = response_datos.text
        response_metadatos = requests.get(response.json()['metadatos'])
        obj['metadatos'] = response_metadatos.json()
        return obj

    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Peticion sin datos")
    elif response.status_code == 429:
        raise HTTPException(status_code=429, detail="Peticion que sobrepasa los limites del servicio")

@aemet_controller.get('/api/satelites/producto/nvdi')
def get_normalized_index_vegetation():
    response = requests.get(f'{url}/satelites/producto/nvdi', headers=headers, params=querystring)

    if response.status_code == 200:
        gif = requests.get(response.json()['datos'], stream=True)
        return StreamingResponse(gif.iter_content(chunk_size=1024), media_type="image/gif")



    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Peticion sin datos")
    elif response.status_code == 429:
        raise HTTPException(status_code=429, detail="Peticion que sobrepasa los limites del servicio")

