import requests, time, json, os

from config import API_URL


CACHE_FILE = "gasolineras_cache.json"
CACHE_TTL = 3600  # 1 hora

def get_gas_stations():
    if os.path.exists(CACHE_FILE):
        mtime = os.path.getmtime(CACHE_FILE)
        if time.time() - mtime < CACHE_TTL:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)

    # Si no, pedir a la API
    resp = requests.get(API_URL)
    data = resp.json()["ListaEESSPrecio"]

    # Guardar caché
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    return data