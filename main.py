import pandas as pd
import requests, json, random, hashlib, sqlite3, os
from timeit import default_timer

# Funciones

# BD

def create_bd():
    conexion = sqlite3.connect("time.bd")

    try:
        conexion.execute(
            """create table tiempos (
                id integer primary key autoincrement,
                mean real,
                maximum real,
                minimum real
            )"""
        )
        return "Tabla creada"
    except sqlite3.OperationalError:
        return "La tabla ya existe"
    conexion.close()

def insert_bd(mean, maximum, minimum):
    conexion = sqlite3.connect("time.bd")
    conexion.execute("Insert into tiempos (mean,maximum,minimum) values(?,?,?)",(mean,maximum, minimum))
    conexion.commit()
    conexion.close()

def create_json ():
    conexion = sqlite3.connect("time.bd")
    df = pd.read_sql_query("Select mean, maximum, minimum from tiempos", conexion)
    with open('data.json', 'w') as file:
        file.write(df.to_json(orient = 'table'))

# Data frame

def search_region():
    url = "https://restcountries-v1.p.rapidapi.com/all"

    headers = {
        'x-rapidapi-key': "9190433b4fmsh6edaec05b4533bfp12fb33jsn101b3273fc56",
        'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    js = response.json()
    df = pd.read_json(json.dumps(js))
    return df.region.unique();

def search_country(region):
    response_country = requests.get("https://restcountries.eu/rest/v2/region/"+region+"?fields=name")
    js_country = response_country.json()
    return js_country[random.randrange(len(js_country))]['name']

def search_language(country):
    response_language = requests.get("https://restcountries.eu/rest/v2/name/"+country+"?fields=languages")
    js_language = response_language.json()
    return js_language[0]['languages'][0]['name']

# -------------------------------------------------------------------

create_bd()

table = pd.DataFrame() 

for r in search_region():
    if r!='':
        start = default_timer()
        country = search_country(r)
        h = hashlib.sha1()
        h.update(search_language(country).encode(encoding="utf-8"))
        language = h.hexdigest()
        end = default_timer()
        table = table.append({'Region' : r , 'Country' : country ,'Languaje' : language, 'Time' : (end - start)} , ignore_index=True)

print(table)

insert_bd(table['Time'].mean(),table['Time'].max(),table['Time'].min())

create_json()



