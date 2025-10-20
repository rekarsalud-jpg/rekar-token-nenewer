import requests
import os
from datetime import datetime

# ✅ CONFIGURACIÓN
APP_ID = "2067093000697157"  # ID de tu app (de Meta)
APP_SECRET = "4b7c6faa2a88296c420dc7ee5c05a20d"  # Clave secreta de tu app
SHORT_LIVED_TOKEN = "EAAdYApgGNUUBPqNSRzctLqfmlz5BD1gNE74FTX1TR7FJ9iHkMx87T9lIpmsyBKt0B9dJOLXMHXOMZBlSCyhJvnokhm4Tg5CcFTywZBxY7MtkE7uxB50QaZC5jzHxbRmMKZBMZCoEZCSWahiIHwCBZC1Qk1rQewQZC1Bgh09N1MYUSrYiJy5QUn6egzRtZAWq812gckF4JD0hY31t3flOBeOI8uZBozbD5AOHr7ub6ZB12OHLKb9p7zlwOCm0jwmIB3vj8M2PWZCpfb9SG2vRHHjeSLzrZBIOQlen9cMjoy2wZD"  # Tu token actual

# 📡 URL de renovación del token
url = f"https://graph.facebook.com/v17.0/oauth/access_token"
params = {
    "grant_type": "fb_exchange_token",
    "client_id": APP_ID,
    "client_secret": APP_SECRET,
    "fb_exchange_token": SHORT_LIVED_TOKEN
}

try:
    response = requests.get(url, params=params)
    data = response.json()

    if "access_token" in data:
        new_token = data["access_token"]
        expiration = data.get("expires_in", "unknown")

        # Guarda el token nuevo en un archivo local
        with open("new_token.txt", "w") as f:
            f.write(new_token)

        print("✅ Nuevo token generado correctamente:")
        print(new_token)
        print(f"⏳ Expira en: {expiration} segundos")
        print(f"📅 Fecha de actualización: {datetime.now()}")

    else:
        print("❌ Error al renovar el token:")
        print(data)

except Exception as e:
    print("⚠️ Error general:")
    print(e)
