import os
import base64
import openai
import httpx
from dotenv import load_dotenv

load_dotenv()

def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# Configuración desde variables de entorno
LM_USER = os.getenv("LM_USER", "rag_user")
LM_PASSWORD = os.getenv("LM_PASSWORD", "plm+cuan-ruf*85735e4a.")
LM_BASE_URL = os.getenv("LM_BASE_URL", "https://dinamica1.fciencias.unam.mx/lmstudio/v1/")
LM_MODE = os.getenv("LM_MODE", "remote").lower()

http_client = httpx.Client(verify=False)

if LM_MODE == "local":
    # Modo conexión local a LM Studio
    client = openai.OpenAI(
        base_url="http://localhost:1234/v1/",
        api_key="lm-studio"
    )
else:
    # Modo conexión remota
    credentials = f"{LM_USER}:{LM_PASSWORD}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    
    client = openai.OpenAI(
        base_url=LM_BASE_URL,
        api_key="lm-studio",
        default_headers={"Authorization": f"Basic {encoded_credentials}"},
        http_client=http_client
    )

def generator(image_path, img_caption=None):
    """Devuelve una descripción generada por el modelo para la imagen dada."""
    if not os.path.exists(image_path):
        return f"No se pudo encontrar la imagen: {image_path}"

    base64_img = encode_image(image_path)
    image_uri = f"data:image/jpeg;base64,{base64_img}"

    img_caption_text = ""
    if img_caption:
        img_caption_text = (
            "La imagen cienciométrica a analizar cuenta con el siguiente caption descriptivo, el cual debe utilizarse únicamente como contexto temático general y no como fuente de datos numéricos o semánticos no visibles: " f"\"{img_caption}\"")

    try:
        completion = client.chat.completions.create(
            model="pixtral-12b",
            messages=[
                {
                    "role": "system",
                    "content": ("Eres un científico de datos experto en cienciometría y en la interpretación de gráficos y representaciones visuales científicas. Debes priorizar la precisión y evitar cualquier suposición no respaldada visualmente.")
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Analiza únicamente la información visible en la imagen proporcionada. "
                                "Redacta una síntesis narrativa fluida con un tono técnico y formal de reporte científico. "
                                "Evita descripciones literales del diseño (como colores de cajas, iconos o fondos) y "
                                "frases meta-discursivas (ej. no uses 'la imagen muestra', 'se observan cajas' o 'los elementos legibles son'). "
                                "Enfócate en integrar los datos y patrones visuales de forma orgánica en el discurso. "
                                "Debes incluir obligatoriamente: Elementos legibles, componentes visuales clave y patrones generales observados. "
                                "Las inferencias son permitidas pero deben ser claramente marcadas como tales. "
                                "Abstente de mencionar elementos no legibles o inventar datos. "
                                "La respuesta debe estar escrita únicamente con letras del alfabeto latino. "
                                "No incluyas introducciones, conclusiones ni títulos de secciones."
                            )
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": image_uri}
                        }
                    ]
                }
            ],
            temperature=0.7
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error al analizar la imagen: {str(e)}"
