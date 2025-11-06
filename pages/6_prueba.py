import streamlit as st
import os

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Sección 5: ODS y Patentes",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================================
# --- VARIABLES DE CONTENIDO ---
# Se extrae y adapta el contenido del input del usuario.
# Los 'iframes' se convierten a rutas de imagen para la función display_image_with_fallback.
# =========================================================================

# Encabezado sección principal 
main_title = '''5. Contribución a los Objetivos de Desarrollo Sostenible (ODS) y Patentes'''

# Función para extraer rutas y leyendas de las etiquetas HTML de imagen
def extract_img_info(html_string):
    """Extrae la ruta de la imagen y el caption (si existe) del HTML."""
    path = ""
    caption = ""
    
    # Intenta encontrar la ruta de la imagen
    if 'src="' in html_string:
        start = html_string.find('src="') + 5
        end = html_string.find('"', start)
        path = html_string[start:end]
        
    # Intenta encontrar el caption (asumiendo que está en una etiqueta <p>)
    if '<p' in html_string and '</p>' in html_string:
        start_p = html_string.find('<p')
        end_p = html_string.find('</p>', start_p)
        
        # Elimina etiquetas HTML internas (br) y limpia espacios para el caption
        caption_raw = html_string[start_p:end_p]
        caption_raw = caption_raw.split('>')[-1].strip() # Solo toma el texto después del último >
        caption = caption_raw.replace('<br />', ' ').replace('\n', '').strip()
        
    return path, caption

# Sección 1: Patentes
sec_one_title = '''Patentes'''
sec_one_text1 = '''Citations From Patents (Citas Provenientes de Patentes): Los artículos que corresponden a GC han recibido 125 citas de patentes en todo el periodo, pero ninguna en el periodo 2020-2024. Los artículos sin GC registran 106 citas de patentes en todo el periodo, y tampoco ninguna en el periodo reciente.'''
image_one_path, image_one_caption = extract_img_info('''<div style="text-align: center;"> <iframe src="images/sec_5_img_1.png" style="border:none;" width="508px" height="210px"></iframe> <p style="margin-top: 15px; font-size: 0.8em; color: #555;"> Citas desde patentes a la producción científica del ICN </p></div>''')

sec_one_text2 = '''De acuerdo con datos registrados en SIGI y corroborados en Lens.org se identificaron 7 patentes registradas pertenecientes a dos familias de patentes con autoría de investigadores del ICN.'''
image_two_path, image_two_caption = extract_img_info('''<iframe src="images/sec_5_img_2.png" style="border:none;" width="900" height="320px"></iframe>''')

sec_one_text3 = '''De acuerdo con el sistema de clasificación CPC (Cooperative Patent Classification) desarrollado por la Oficina Europea de Patentes (EPO) y la Oficina de Patentes de EE.UU. (USPTO), donde cada código representa un área técnica o tecnológica específica, las patentes analizadas se clasifican en Necesidades Humanas y Química Metalúrgica.'''
image_three_path, image_three_caption = extract_img_info('''<iframe src="images/sec_5_img_3.png" style="border:none;" width="600" height="210px"></iframe>''')


# Sección 2: ODS
sec_two_title = '''Objetivos de Desarrollo Sostenible (ODS)'''
sec_two_text1 = '''En la Tabla se muestra la distribución de documentos según su contribución a los Objetivos de Desarrollo Sostenible (ODS) de la Agenda 2030, tal como son clasificados por WoS (Sustainable Development Goals mapping). El 19.8% de los documentos contribuyen a algún ODS. El ODS más representado en la producción científica es Salud y bienestar (ODS 3), lo que sugiere un fuerte enfoque de investigación en temas médicos, biomédicos o de salud pública. Le siguen Acción por el clima (ODS 13) y Energía asequible y no contaminante (ODS 7), que también muestran una importante contribución.'''
image_four_path, image_four_caption = extract_img_info('''<div style="text-align: center;"> <iframe src="images/sec_5_img_4.png" style="border:none;" width="100%" height="500px"></iframe><p style="margin-top: 1px; margin-left: -140px; font-size: 0.8em; color: #f2eded;"> Documentos según su contribución a los Objetivos de Desarrollo Sostenible (ODS) <br /> de la Agenda 2030 </p></div>''')
image_five_path, image_five_caption = extract_img_info('''<div style="text-align: center;"> <iframe src="images/sec_5_img_5.png" style="border:none;" width="630" height="300px"></iframe><p style="margin-top: 7px; font-size: 0.8em; color: #f2eded;"> Evolución de la proporción de artículos en los diferentes ODS </p></div>''')


# --- Función Auxiliar para Mostrar Imágenes ---
def display_image_with_fallback(path, caption="", width=None):
    """Muestra una imagen si existe, o un placeholder con advertencia."""
    # Uso de un placeholder más sobrio para informes
    placeholder_url = f"https://placehold.co/600x400/333333/ffffff?text=IMAGEN+NO+DISPONIBLE" 
    
    # NOTA: En este entorno, asumimos que las imágenes se referencian correctamente, 
    # pero usamos el placeholder si la ruta es una cadena vacía (o si os.path.exists no funcionara)
    if not path or not os.path.exists(path):
        st.error(f"⚠️ ¡Error de Recurso! La ruta de la imagen '{path}' no está disponible.")
        st.image(placeholder_url, caption=f"Placeholder: {caption}", use_column_width=True)
    else:
        # Nota: La ruta real es la de desarrollo. Aquí solo simulamos la carga.
        st.image(path, caption=caption, use_column_width=(width is None), width=width)


# =========================================================================
# --- ESTRUCTURA PRINCIPAL DE LA APLICACIÓN ---
# =========================================================================

# Título principal con estilo
st.markdown(
    f"<h1 style='text-align: center; color: #4B0082; font-size: 2.5em;'>{main_title}</h1>", 
    unsafe_allow_html=True
)
st.markdown("---") 

# 1. Sección Patentes (Citas y Clasificación)
st.subheader(f"💡 {sec_one_title}")

tab_citas, tab_registro = st.tabs(["Citas Provenientes de Patentes", "Clasificación de Patentes Registradas"])

with tab_citas:
    st.markdown("#### Análisis de Citas de Patentes")
    
    col1, col2 = st.columns([2, 3])
    with col1:
        # Caja de texto destacada para el dato principal
        st.info(sec_one_text1, icon="📎")
    with col2:
        # La imagen se muestra en la columna derecha
        display_image_with_fallback(image_one_path, image_one_caption)


with tab_registro:
    st.markdown("#### Patentes Registradas y Clasificación CPC")
    st.markdown(sec_one_text2)
    
    # Distribución de patentes (imagen 2)
    st.markdown("##### Familias de Patentes")
    display_image_with_fallback(image_two_path, image_two_caption)
    
    # Clasificación CPC (imagen 3)
    st.markdown("---")
    col3, col4 = st.columns([1, 2])
    with col3:
        # Texto explicativo para la clasificación
        st.markdown(sec_one_text3)
        st.markdown(
            """
            <div style='background-color: #f0f8ff; padding: 10px; border-radius: 5px; border-left: 5px solid #007bff;'>
                <p style='font-weight: bold;'>Clasificación CPC (Cooperative Patent Classification)</p>
                <small>Sistema desarrollado por EPO y USPTO que codifica áreas técnicas.</small>
            </div>
            """, 
            unsafe_allow_html=True
        )
    with col4:
        # Gráfico de clasificación
        display_image_with_fallback(image_three_path, image_three_caption, width=400)


st.markdown("<br><hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)


# 2. Sección Objetivos de Desarrollo Sostenible (ODS)
st.subheader(f"🌍 {sec_two_title}")

# División de la sección ODS en Texto/Gráfico Principal y Evolución

col_text, col_img_4 = st.columns([1, 1.5])

with col_text:
    st.markdown("#### Distribución de Documentos por ODS")
    # Uso de st.success para destacar el principal hallazgo (ODS 3)
    st.success(sec_two_text1, icon="✅")
    
    # Mini-tabla de referencia para los principales ODS
    st.markdown("""
        <div style='margin-top: 20px; padding: 10px; border: 1px solid #4CAF50; border-radius: 5px;'>
            <p style='font-weight: bold;'>Principales ODS:</p>
            <ul>
                <li><span style='color: #4CAF50;'>ODS 3: Salud y bienestar</span> (Más representado)</li>
                <li>ODS 13: Acción por el clima</li>
                <li>ODS 7: Energía asequible y no contaminante</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


with col_img_4:
    st.markdown("<h5 style='text-align: center;'>Contribución por Objetivo (WoS Mapping)</h5>", unsafe_allow_html=True)
    # Gráfico de distribución de documentos por ODS (imagen 4)
    display_image_with_fallback(image_four_path, image_four_caption)


st.markdown("---")

st.markdown("#### Evolución de la Contribución a ODS")
# Gráfico de evolución de la proporción de artículos en ODS (imagen 5)
col_vacia_2, col_img_5, col_vacia_3 = st.columns([1, 2, 1])
with col_img_5:
    display_image_with_fallback(image_five_path, image_five_caption, width=600)

st.markdown("<br>", unsafe_allow_html=True)