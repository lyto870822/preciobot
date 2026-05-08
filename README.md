# PrecioBot — Bot de monitoreo de precios de Amazon

Bot en Python que monitorea precios de productos en Amazon y te envía alertas por email automáticamente cuando encuentra una oferta.

## Requisitos

- Python 3.6+
- pip install requests beautifulsoup4

## Cómo usar

1. Edita las variables al final del script:
   - `URL`: link del producto de Amazon
   - `PRECIO_OBJETIVO`: precio mínimo para recibir alerta
   - `INTERVALO`: cada cuántos segundos revisar (3600 = 1 hora)

2. Configura tu correo:
   - En `enviar_alerta()`, cambia `tu@email.com` por tu correo
   - Usa una contraseña de aplicación de Gmail (no tu contraseña normal)

3. Ejecuta:
   ```bash
   python3 precio_bot.py
   ```

## ⚠️ Importante

- Necesitas una contraseña de aplicación de Gmail para `smtplib`
- Amazon puede bloquear requests si haces muchas en poco tiempo
- Usa un intervalo de al menos 300 segundos (5 min)

## Tutorial

Video completo en: https://youtu.be/qmQnSRSNBG4
