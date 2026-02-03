#SECCION 4

import streamlit as st
from llm.llm_generator import generator
import os

if "interpretaciones" not in st.session_state:
    st.session_state.interpretaciones = {}
    
if "generadas" not in st.session_state:
    st.session_state.generadas = False

st.set_page_config(
    page_title="Caracterización Temática de la Producción Científica",
    layout="wide",
    initial_sidebar_state="collapsed"
)

main_title = "Caracterización Temática de la Producción Científica"

#Pestaña 1 imagenes
sec_one_title = "Categorías Temáticas"

image_one_path = "assets/images/sec_4_img_1.png" 
image_one_caption = "50 primeras categorías temáticas de acuerdo al número de artículos, periodo: 1980-2024"

image_two_path = "assets/images/sec_4_img_2.png" #Sin caption en el reporte original

image_three_path = "assets/images/sec_4_img_3.png"
image_three_caption = "50 primeras categorías temáticas de acuerdo al número de artículos, periodo: 2020-2024"

#Pestaña 2 imagenes
sec_two_title = "Evolución de los Temas de Investigación"

image_four_path = "assets/images/sec_4_img_4.png"
image_four_caption = "Gráfico de evolución de categorías 1"

image_five_path = "assets/images/sec_4_img_5.png"
image_five_caption = "Evolución del Core temático"

image_six_path = "assets/images/sec_4_img_6.png"
image_six_caption = "Evolución del perfil temático (core)"

image_seven_path = "assets/images/sec_4_img_7.png"
image_seven_caption = "Gráfico de evolución de categorías 2"

##Pestaña 3 imagenes
sec_three_title = "Caracterización Temática: Micro y Meso Tópicos"

image_eight_path = "assets/images/sec_4_img_8.png"
image_eight_caption = '''Producción ([detalles](https://sigi.nucleares.unam.mx/sgiicn/userfiles/files/evolution/icn2_2_adn_evolution.html)) e Impacto ([detalles](https://sigi.nucleares.unam.mx/sgiicn/userfiles/files/evolution/icn2_2_evolution.html))'''

image_nine_path = "assets/images/sec_4_img_9.png"
image_nine_caption = "Periodo 1980-2024"

# Para mostrar imágenes con caption y manejo de error.
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
            st.session_state.interpretaciones["img25"] = generator(image_one_path, image_one_caption)
            st.session_state.interpretaciones["img26"] = generator(image_two_path)
            st.session_state.interpretaciones["img27"] = generator(image_three_path, image_three_caption)
            st.session_state.interpretaciones["img28"] = generator(image_four_path, image_four_caption)
            st.session_state.interpretaciones["img29"] = generator(image_five_path, image_five_caption)
            st.session_state.interpretaciones["img30"] = generator(image_six_path, image_six_caption)
            st.session_state.interpretaciones["img31"] = generator(image_seven_path, image_seven_caption)
            st.session_state.interpretaciones["img32"] = generator(image_eight_path, image_eight_caption)
            st.session_state.interpretaciones["img33"] = generator(image_nine_path, image_nine_caption)
            st.session_state.generadas = True

st.markdown("---")

st.header("Indicadores Temáticos Clave")
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric("Áreas de Investigación", "15", help="Clasificación por categorías WoS")
with metric_col2:
    st.metric("Concentración Temática", "65%", delta="Física y Astrofísica")
with metric_col3:
    st.metric("Clústeres en Mapa", "4-5", help="Estructura interna identificada por co-ocurrencia")
with metric_col4:
    st.metric("Interdisciplinaridad", "Alta", delta_color="normal", delta="Basado en densidad de enlaces")
    

#PESTAÑAS
tab1, tab2, tab3 = st.tabs([f"Categorías Temáticas", f"Evolución Temática", f"Caracterización Temática"])

# =========================================================================
# PESTAÑA 1
# =========================================================================
with tab1:

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Periodo 1980-2024 (Artículos)")
        display_image(image_one_path, image_one_caption)
        
    with col2:
        display_interpretacion("img25", image_one_path, image_one_caption)

    st.markdown("---")

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Periodo 2020-2024 (Artículos)")
        display_image(image_two_path, " ")
        display_interpretacion("img26", image_two_path)

    with col4:
        display_image(image_three_path, image_three_caption)
        display_interpretacion("img27", image_three_path, image_three_caption)

    st.markdown("---")

# =========================================================================
# PESTAÑA 2
# =========================================================================
with tab2:
    st.subheader("Evolución del Perfil Temático (Core)")

    col1, col2 = st.columns(2)
    with col1:
        with st.expander("Ver Detalles"):
            display_interpretacion("img29", image_five_path, image_five_caption)
        display_image(image_five_path, image_five_caption)

    with col2:
        with st.expander("Ver Detalles"):
            display_interpretacion("img30", image_six_path, image_six_caption)
        display_image(image_six_path, image_six_caption)

    st.markdown("---")

    st.subheader("Gráficos Adicionales de Evolución")
    col3, col4 = st.columns(2)
    with col3:
        with st.expander("Ver Detalles"):
            display_interpretacion("img28", image_four_path, image_four_caption)
        display_image(image_four_path, image_four_caption)

    with col4:
        with st.expander("Ver Detalles"):
            display_interpretacion("img31", image_seven_path, image_seven_caption)
        display_image(image_seven_path, image_seven_caption)

    st.markdown("---")

#=========================================================================
#PESTAÑA 3
#=========================================================================
with tab3:
    st.subheader(sec_three_title)

    col1, col2 = st.columns([3, 2])
    with col1:
        display_interpretacion("img32", image_eight_path, image_eight_caption)
    with col2:
        display_image(image_eight_path, image_eight_caption)

    col3, col4 = st.columns([2, 3])
    with col3:
        display_image(image_nine_path, image_nine_caption) 
    with col4: 
        display_interpretacion("img33", image_nine_path, image_nine_caption) 
        
    st.markdown("---")
