import openai
import base64
import httpx
import os

def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

USER = "rag_user"
PASSWORD = "plm+cuan-ruf*85735e4a."
credentials = f"{USER}:{PASSWORD}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

http_client = httpx.Client(verify=False)

client = openai.OpenAI(
    base_url="https://dinamica1.fciencias.unam.mx/lmstudio/v1/",
    api_key="lm-studio",
    default_headers={"Authorization": f"Basic {encoded_credentials}"},
    http_client=http_client
)

def generator(image_path):
    """Devuelve una descripción generada por el modelo para la imagen dada."""
    if not os.path.exists(image_path):
        return f"No se pudo encontrar la imagen: {image_path}"

    base64_img = encode_image(image_path)
    image_uri = f"data:image/jpeg;base64,{base64_img}"

    try:
        completion = client.chat.completions.create(
            model="pixtral-12b",
            messages=[
            {"role": "system", "content":  "Eres un científico de datos experto en cienciometría y en la interpretación de gráficos y representaciones visuales científicas. Debes priorizar la precisión y evitar cualquier suposición no respaldada visualmente."},
            {"role": "user", "content": [
                {
                    # El prompt de texto
                    "type": "text", 
                    "text": "Analiza únicamente la información visible en la imagen proporcionada. Redacta un párrafo con un tono técnico y formal de un reporte científico que contenga obligatoriamente lo siguiente: Elementos explícitamente legibles en la imagen, componentes visuales identificables (tipo de gráfica, ejes, colores, símbolos), patrones visuales generales observables (tendencias, aumentos o disminuciones), las inferencias son permitidas pero deben ser claramente marcadas como inferencias, abstente de mencionar elementos no legibles, ambiguos o no identificables; no menciones años específicos, valores exactos, rangos temporales, intersecciones o significados de ejes a menos que estén claramente indicados y sean legibles en la imagen; si un dato no puede leerse con claridad, indícalo explícitamente como no legible o no identificable; no inventes valores, fechas, unidades ni significados semánticos. La respuesta debe estar escrita únicamente con letras del alfabeto latino. No incluyas introducciones ni conclusiones generales ni títulos de secciones."                            
                },
                {
                    # Imagen codificada
                    "type": "image_url",
                    "image_url": {"url": image_uri}
                }
            ]}
        ], #Prioriza la precisión y sigue estrictamente el formato de salida JSON solicitado en la solicitud del usuario. 
            temperature=0.7
        )
        return completion.choices[0].message.content

    except Exception as e:
        return f"Error al analizar la imagen: {str(e)}"

