#!/usr/bin/env python3
"""
PrecioBot — Monitoreo automatico de precios en Amazon
Tutorial: https://youtu.be/qmQnSRSNBG4
"""

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


def obtener_precio(url):
    """Extrae el precio actual de un producto de Amazon."""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    span = soup.find(class_='a-price-whole')
    if span:
        precio = span.text.replace(',', '')
        return float(precio)
    return None


def enviar_alerta(producto, precio, url):
    """Envia un correo cuando el precio baja del objetivo."""
    msg = MIMEMultipart()
    msg['Subject'] = f'OFERTA: {producto} bajo a ${precio}'
    msg['From'] = 'tu@email.com'
    msg['To'] = 'tu@email.com'

    cuerpo = f"""
    El producto {producto} acaba de bajar de precio!

    Precio actual: ${precio}
    Link: {url}

    Corre a comprarlo antes de que suba!
    """
    msg.attach(MIMEText(cuerpo, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('tu@email.com', 'tu_password_app')
    server.send_message(msg)
    server.quit()


# ── Configuracion ─────────────────────────────────
URL = 'https://www.amazon.com.mx/dp/TU_ASIN'
PRECIO_OBJETIVO = 1000.0
INTERVALO = 3600  # segundos (1 hora)

# ── Loop de monitoreo ─────────────────────────────
while True:
    precio = obtener_precio(URL)
    if precio and precio <= PRECIO_OBJETIVO:
        enviar_alerta('Producto', precio, URL)
        print(f'[!] Oferta encontrada! ${precio} — revisa tu email')
    elif precio:
        print(f'[.] Precio actual: ${precio} — no hay oferta')
    else:
        print('[x] No se pudo obtener el precio')
    time.sleep(INTERVALO)
