#SECCION 5

import streamlit as st
from llm.llm_generator import generator
import os

if "interpretaciones" not in st.session_state:
    st.session_state.interpretaciones = {}
    
if "generadas" not in st.session_state:
    st.session_state.generadas = False

st.set_page_config(
    page_title="Contribución a los Objetivos de Desarrollo Sostenible (ODS)",
    layout="wide",
    initial_sidebar_state="collapsed"
)

main_title = "Contribución a los Objetivos de Desarrollo Sostenible (ODS)"

#Pestaña 1 imagenes
sec_one_title = "Patentes"

image_one_path = "assets/images/sec_5_img_1.png"
image_one_caption = "Citas desde patentes a la producción científica del ICN"

image_two_path = "assets/images/sec_5_img_2.png" #Sin caption en el reporte original

image_three_path = "assets/images/sec_5_img_3.png" #Sin caption en el reporte original

# --- Subsección 2
sec_two_title = '''Objetivos de Desarrollo Sostenible (ODS)'''

image_four_path = "assets/images/sec_5_img_4.png"
image_four_caption = "Documentos según su contribución a los Objetivos de Desarrollo Sostenible (ODS)"

image_five_path = "assets/images/sec_5_img_5.png"
image_five_caption = "Evolución de la proporción de artículos en los diferentes ODS"

#Para mostrar imágenes con caption y manejo de error.
def display_image(path, caption):
    """Muestra la imagen con un caption centrado."""
    if not os.path.exists(path):
        st.warning(f"Imagen no encontrada en: {path}. Asegúrate de que el directorio 'assets/images/' exista y contenga las imágenes.")
        st.info(f"Placeholder para: {caption}")
        st.image("https://placehold.co/600x460/cccccc/333333?text=IMAGEN+FALTANTE", caption=caption, width="stretch")
    else:
        st.image(path, caption=caption, width="stretch")

#Para mostrar la interpretacion de la imagen cuya llave y path pasan como parametro
def display_interpretacion(img_key, img_path, img_caption=None):
    if img_key in st.session_state.interpretaciones:
        st.markdown(st.session_state.interpretaciones[img_key])

        if st.button("Regenerar", key=f"regen_{img_key}"):
            st.session_state.interpretaciones[img_key] = st.empty()
            with st.spinner("Regenerando..."):
                st.session_state.interpretaciones[img_key] = generator(img_path, img_caption)
            st.rerun()
    else:
        st.empty()

st.title(main_title)

st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #2e7d32;
        color: white;
        font-weight: 600;
        border-radius: 6px;
        padding: 0.5em 1em;
    }
    div.stButton > button:hover {
        background-color: #2e7d32;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

headerbutt1, headerbutt2 = st.columns([7, 2])
with headerbutt2:
    if st.button("Generar interpretaciones"):
        with st.spinner("Generando..."):
            st.session_state.interpretaciones["img34"] = generator(image_one_path, image_one_caption)
            st.session_state.interpretaciones["img35"] = generator(image_two_path)
            st.session_state.interpretaciones["img36"] = generator(image_three_path)
            st.session_state.interpretaciones["img37"] = generator(image_four_path, image_four_caption)
            st.session_state.interpretaciones["img38"] = generator(image_five_path, image_five_caption)
            st.session_state.generadas = True

st.markdown("---")

st.header("Indicadores ODS Clave")
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric("Citas de Patentes", "125", help="Los artículos correspondientes a GC recibieron 125 citas de patentes en todo el periodo.")
with metric_col2:
    st.metric("Contribución al ODS en %", "19.8%", help="Porcentaje de documentos que contribuyen a algún ODS.")
with metric_col3:
    st.metric("Documentos totales al ODS", "1044", help="Total de documentos que contribuyen a todos los ODS.")
with metric_col4:
    st.metric("ODS de Mayor Potencial", "ODS 03", delta="Salud y Bienestar")


#PESTAÑAS
tab1, tab2 = st.tabs([f"1. {sec_one_title}", f"Distribución de Documentos"])

#=========================================================================
#PESTAÑA 1
#=========================================================================
with tab1:
    st.subheader(sec_one_title)

    col1, col2 = st.columns(2)
    with col1:
        display_interpretacion("img34", image_one_path, image_one_caption)
    with col2:
        display_image(image_one_path, image_one_caption)

    col3, col4 = st.columns(2)
    with col3:
        display_image(image_two_path, " ")
    with col4:
        display_interpretacion("img35", image_two_path)

    col5, col6 = st.columns(2)
    with col5:
        display_interpretacion("img36", image_three_path)
    with col6:
        display_image(image_three_path, " ")

    st.markdown("---")

#=========================================================================
#PESTAÑA 2
#=========================================================================
with tab2:
    st.subheader(sec_two_title)

    col1, col2 = st.columns(2)
    with col1:
        display_interpretacion("img37", image_four_path, image_four_caption)
    with col2:
        display_image(image_four_path, image_four_caption)

    st.markdown("---")

    st.markdown("#### Evolución de la Contribución a ODS")
    col3, col4, col5 = st.columns([1, 4, 1])

    display_interpretacion("img38", image_five_path, image_five_caption)
        
    with col4:
        display_image(image_five_path, image_five_caption)

    st.markdown("---")
