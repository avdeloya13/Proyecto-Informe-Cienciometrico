
#En cada una de las paginas de las secciones, se va a modificar la funcion display_image para mandar a llamar la funcion de este script describe_image

#description = describe_image(path)
#st.write(description)

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

def describe_image(image_path):
    """Devuelve una descripción generada por el modelo para la imagen dada."""
    if not os.path.exists(image_path):
        return f"No se pudo encontrar la imagen: {image_path}"

    base64_img = encode_image(image_path)
    image_uri = f"data:image/jpeg;base64,{base64_img}"

    try:
        completion = client.chat.completions.create(
            model="bartowski/OpenGVLab_InternVL3_5-8B-GGUF",
            messages=[
                {"role": "system",
                 "content": "Eres un científico de datos experto en cienciometría y en la interpretación de gráficos e imágenes científicas."},
                {"role": "user", "content": [
                    {"type": "text",
                     "text": "Describe y analiza únicamente la información visible en la imagen proporcionada. No incluyas introducciones ni conclusiones generales, entrega solo la información técnica y relevante. Si un dato en la imagen no es legible o no está presente, no lo inventes. No inventes valores, fechas o unidades. Si es una gráfica, identifica el tipo de gráfica, ejes y qué representan, tendencias principales, picos o valles relevantes, y cualquier anotación o valor claramente legible. Mantén resultados concisos."},
                    {"type": "image_url",
                     "image_url": {"url": image_uri}}
                ]}
            ], #Prioriza la precisión y sigue estrictamente el formato de salida JSON solicitado en la solicitud del usuario. 
            temperature=0.2 ##La temperatura debe estar entre 0.0 y 0.2 genera respuestas más deterministas y precisas
        )
        return completion.choices[0].message.content

    except Exception as e:
        return f"Error al analizar la imagen: {str(e)}"

