import speech_recognition as sr
import requests
from openai import OpenAI

PROMPT_BASE = """
Actúa como un sistema de extracción de variables de gastos personales. Para cada texto de entrada, devuelve un JSON con las siguientes claves:

- monto (número)
- moneda (USD, COP, etc.)
- categoría (Transporte, Comida, Salud, etc.)
- acción (gasto o ingreso)
- descripción (opcional)

Ejemplos:

Entrada: "Gaste 30 dólares en Uber"
Salida:
{
  "monto": 30,
  "moneda": "USD",
  "categoría": "Transporte",
  "acción": "gasto",
  "descripción": "Uber"
}

Entrada: "Recibí 200 mil pesos por una venta en MercadoLibre"
Salida:
{
  "monto": 200000,
  "moneda": "COP",
  "categoría": "Ingreso",
  "acción": "ingreso",
  "descripción": "MercadoLibre"
}


"""

r = sr.Recognizer()
audio_file = sr.AudioFile(r"C:\Users\aleco\Downloads\WhatsApp-Audio-2025-07-22-at-21.30.09_d796c81d.waptt.wav")  # Ej: "gasto_uber.wav"

with audio_file as source:
    audio = r.record(source)  
    try:
        text = r.recognize_google(audio, language="es-ES")  # Usar Google STT (requiere internet)
        print("Texto detectado:", text)
    except Exception as e:
        print("Error al procesar el audio:", e)

cliente = OpenAI(api_key="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", base_url='https://openrouter.ai/api/v1')


def analizartexto(text):
    response = cliente.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role": "system", "content": PROMPT_BASE},
            {"role": "user", "content": text}
        ],
        
    )  
    return response.choices[0].message.content


print("Análisis del texto:", analizartexto(text))