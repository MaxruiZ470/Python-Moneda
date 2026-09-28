import requests

respuesta = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")
datos = respuesta.json()
moneda_mas_alta = ""
cambio_mas_alto = 0
for moneda, cambio in datos["rates"].items():
    
    if cambio > cambio_mas_alto:
        cambio_mas_alto = cambio
        moneda_mas_alta = moneda
print("La moneda con el cambio más alto es:", moneda_mas_alta)
print("Su cambio es:", cambio_mas_alto)