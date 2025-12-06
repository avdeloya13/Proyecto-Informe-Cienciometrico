import openai
import base64
import httpx

# --- Función de utilidad para codificar la imagen ---
def encode_image(image_path):
    """Codifica el archivo de imagen en una cadena Base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# --- 1. Credenciales de Autenticación (se mantienen igual) ---
USER = 'rag_user'
PASSWORD = 'plm+cuan-ruf*85735e4a.'

# --- 2. Codifica las credenciales en Base64 ---
credentials = f"{USER}:{PASSWORD}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# --- 3. Define la URL base y el cliente HTTP (se mantienen igual) ---
BASE_URL = "https://dinamica1.fciencias.unam.mx/lmstudio/v1/"

# Crea un cliente HTTP que NO VERIFICA los certificados SSL
http_client = httpx.Client(
    verify=False
)

# --- 4. Inicializa el cliente (se mantiene igual) ---
client = openai.OpenAI(
    base_url=BASE_URL,
    api_key="lm-studio",  # Sigue siendo necesario
    default_headers={
        "Authorization": f"Basic {encoded_credentials}"
    },
    http_client=http_client
)

print("CLIENTE OPENAI CONECTADO")

# --- 5. Define la ruta de la imagen y codifícala ---
# **ASEGÚRATE DE CAMBIAR ESTO POR LA RUTA REAL DE TU IMAGEN**
IMAGE_PATH = "img_prueba.jpeg" 
try:
    base64_image = encode_image(IMAGE_PATH)
except FileNotFoundError:
    print(f"\nERROR: No se encontró el archivo de imagen en la ruta: {IMAGE_PATH}")
    print("Por favor, asegúrate de que el archivo exista y la ruta sea correcta.")
    exit()

# Construye el URI de la imagen en Base64 para el mensaje
image_uri = f"data:image/jpeg;base64,{base64_image}" # Asumiendo que es JPEG. Cambia a "image/png" si es necesario.


# --- 6. Llamada al modelo con contenido multimodal (texto e imagen) ---
try:
    print(f"\nEnviando solicitud al modelo: bartowski/OpenGVLab_InternVL3_5-8B-GGUF...")
    
    completion = client.chat.completions.create(
        model="bartowski/OpenGVLab_InternVL3_5-8B-GGUF", # Modelo solicitado
        messages=[
            {"role": "system", "content": "content": "Eres un científico de datos experto en cienciometría y en la interpretación de gráficos e imágenes científicas."},
            {"role": "user", "content": [
                {
                    # El prompt de texto
                    "type": "text", 
                    "text": "Describe y analiza únicamente la información visible en la imagen proporcionada. No incluyas introducciones ni conclusiones generales, entrega solo la información técnica y relevante. Si un dato en la imagen no es legible o no está presente, no lo inventes. No inventes valores, fechas o unidades. Si es una gráfica, identifica el tipo de gráfica, ejes y qué representan, tendencias principales, picos o valles relevantes, y cualquier anotación o valor claramente legible. Mantén resultados concisos."
                },
                {
                    # La imagen codificada
                    "type": "image_url",
                    "image_url": {"url": image_uri}
                }
            ]}
        ],
        temperature=0.2, #La temperatura debe estar entre 0.0 y 0.2 genera respuestas más deterministas y precisas
    )
    
    print("\n--- Respuesta del Modelo ---")
    print(completion.choices[0].message.content)
    print("---------------------------\n")

except openai.AuthenticationError as e:
    print("\nError de autenticación: Verifica tu usuario y contraseña en la base_url.")
    print(e)
except openai.APIConnectionError as e:
    print("\nError de conexión: No se pudo conectar al servidor. ¿Está Nginx corriendo?")
    print(e)
except Exception as e:
    print(f"\nOcurrió un error inesperado: {e}")
