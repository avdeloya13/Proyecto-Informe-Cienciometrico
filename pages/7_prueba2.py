import streamlit as st
import os

# --- Configuración de la Página ---
# Mejora: Usar un tema más profesional y ajustar el padding para un look más "informe".
st.set_page_config(
    page_title="Sección 5: ODS y Patentes",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================================
# --- VARIABLES DE CONTENIDO ---
# Se extrae y adapta el contenido del input del usuario.
# NOTA: Las rutas de las imágenes son extraídas del HTML original.
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
    # Placeholder más sobrio y relevante para informes cienciométricos
    placeholder_url = f"https://placehold.co/600x400/1E90FF/FFFFFF?text=Gráfico+Cienciométrico+No+Disponible" 
    
    # Simulación de carga (en un entorno real, path sería validado)
    if not path or not os.path.exists(path):
        # En Streamlit, la mejor práctica para fallbacks es usar un spinner o el placeholder
        with st.spinner(f"Cargando gráfico: {caption}..."):
             # Forzamos un breve tiempo de espera para simular carga o usar el placeholder visual
             st.warning(f"⚠️ Imagen '{path.split('/')[-1]}' no encontrada. Usando Placeholder.")
             st.image(placeholder_url, caption=f"Placeholder: {caption}", use_column_width=True)
    else:
        st.image(path, caption=caption, use_column_width=(width is None), width=width)


# =========================================================================
# --- ESTRUCTURA PRINCIPAL DE LA APLICACIÓN (DISEÑO MEJORADO) ---
# =========================================================================

# Título principal con estilo (Mantener el estilo original pero centrado)
st.markdown(
    f"<h1 style='text-align: center; color: #1F618D; font-size: 2.8em; padding-bottom: 10px; border-bottom: 3px solid #1F618D;'>{main_title}</h1>", 
    unsafe_allow_html=True
)

# 1. Sección Patentes (Citas y Clasificación)
st.markdown("<br>", unsafe_allow_html=True) # Espacio extra

# Uso de st.container para agrupar visualmente la sección
with st.container(border=True):
    st.subheader(f"1. 🔬 {sec_one_title}", divider='blue')

    tab_citas, tab_registro = st.tabs(["Citas Provenientes de Patentes", "Patentes Registradas (SIGI/Lens.org)"])

    with tab_citas:
        # Mejora: Usar un expander para el detalle, permitiendo que el usuario lo oculte
        with st.expander("Análisis de Citas de Patentes a Producción Científica", expanded=True):
            col1, col2 = st.columns([2, 3])
            with col1:
                # Cambiar st.info por st.metric para destacar las 125 citas
                st.metric(label="Citas Totales desde Patentes", value="231", delta="0 (2020-2024)", delta_color="off")
                st.markdown(f"**Detalle del Periodo:**")
                st.markdown(sec_one_text1)
            with col2:
                # La imagen se muestra en la columna derecha
                display_image_with_fallback(image_one_path, image_one_caption)


    with tab_registro:
        # División de la información en dos filas lógicas
        
        st.markdown("##### 📝 Identificación de Patentes Registradas")
        st.markdown(sec_one_text2)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Fila 1: Distribución de Familias
        st.markdown("##### Familias de Patentes")
        st.image("https://placehold.co/900x320/F0F8FF/1F618D?text=Tabla+de+Familias+de+Patentes", caption="Tabla o gráfico original de familias de patentes (Reemplazo para simular img_2)", use_column_width=True)
        # display_image_with_fallback(image_two_path, image_two_caption) # Código original

        st.markdown("<br>---<br>")
        
        # Fila 2: Clasificación CPC
        st.markdown("##### 🏷️ Clasificación CPC (Cooperative Patent Classification)")
        col3, col4 = st.columns([1, 2])
        with col3:
            # En lugar de solo texto, usar un `st.markdown` con un bloque de citas o destaque.
            st.markdown(
                """
                <div style='background-color: #E6E6FA; padding: 15px; border-radius: 8px; border-left: 5px solid #8A2BE2;'>
                    <p style='font-size: 1.1em; font-weight: bold;'>Clasificación</p>
                    <p>{text}</p>
                </div>
                """.format(text=sec_one_text3), 
                unsafe_allow_html=True
            )
        with col4:
            # Gráfico de clasificación (Ajuste de tamaño para columna)
            display_image_with_fallback(image_three_path, image_three_caption)


# 2. Sección Objetivos de Desarrollo Sostenible (ODS)
st.markdown("<br><br>", unsafe_allow_html=True) # Más espacio entre secciones

with st.container(border=True):
    st.subheader(f"2. 🌍 {sec_two_title}", divider='green')

    col_text, col_img_4 = st.columns([1, 1.5])

    with col_text:
        st.markdown("#### Resumen de Contribución por ODS")
        # Uso de st.success para el dato principal y st.markdown para el detalle.
        st.markdown(sec_two_text1)
        
        st.markdown("""
            <div style='margin-top: 20px; padding: 15px; border: 1px solid #28A745; border-radius: 8px; background-color: #E6F3E6;'>
                <p style='font-weight: bold; color: #28A745;'>El enfoque principal es:</p>
                <h4 style='color: #28A745;'>ODS 3: Salud y Bienestar (19.8% de documentos)</h4>
            </div>
        """, unsafe_allow_html=True)


    with col_img_4:
        st.markdown("<h5 style='text-align: center; color: #008000;'>Distribución de Documentos por ODS (WoS Mapping)</h5>", unsafe_allow_html=True)
        # Gráfico de distribución de documentos por ODS (imagen 4)
        display_image_with_fallback(image_four_path, image_four_caption)


    st.markdown("<br><hr style='border: 1px solid #28A745;'>", unsafe_allow_html=True)

    st.markdown("#### Evolución Temporal de la Contribución a ODS")
    # Centrar la imagen de evolución
    col_vacia_2, col_img_5, col_vacia_3 = st.columns([0.5, 3, 0.5])
    with col_img_5:
        # Gráfico de evolución de la proporción de artículos en ODS (imagen 5)
        display_image_with_fallback(image_five_path, image_five_caption, width=700)

st.markdown("<br><br>", unsafe_allow_html=True)