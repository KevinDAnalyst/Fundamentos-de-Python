import requests

# Consumir una API pública para obtener tipo de cambio / datos simulados
url = "https://api.exchangerate-api.com/v4/latest/USD"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()
    tipo_cambio_colones = datos['rates']['CRC']
    print(f"\n\tTipo de cambio actual (USD a Colones): {tipo_cambio_colones}\n")
else:
    print("Error al conectar con la API")