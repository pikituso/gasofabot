import requests, time, json, os
from config import API_URL
import random

CACHE_FILE = "gasolineras_cache.json"
CACHE_TTL = 3600  # 1 hora

def get_gas_stations():
    # Primero intentar usar cache (evita peticiones innecesarias)
    if os.path.exists(CACHE_FILE):
        mtime = os.path.getmtime(CACHE_FILE)
        if time.time() - mtime < CACHE_TTL:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)

    # Headers más realistas y variados
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ]

    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Origin': 'https://sedeaplicaciones.minetur.gob.es',
        'Referer': 'https://sedeaplicaciones.minetur.gob.es/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    try:
        # Pequeño delay aleatorio para evitar saturación
        time.sleep(random.uniform(0.1, 0.5))
        
        resp = requests.get(API_URL, headers=headers, timeout=15, verify=False)
        
        if resp.status_code == 200:
            data = resp.json().get("ListaEESSPrecio", [])
            
            # Guardar cache
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
                
            return data
        else:
            raise Exception(f"HTTP Error: {resp.status_code}")
            
    except Exception as e:
        print(f"Error API: {e}")
        # Fallback a cache existente
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return []