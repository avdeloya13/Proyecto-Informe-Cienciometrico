#SECCION 1

import streamlit as st
from llm.llm_generator import generator
import os

if "interpretaciones" not in st.session_state:
    st.session_state.interpretaciones = {}
    
if "generadas" not in st.session_state:
    st.session_state.generadas = False

st.set_page_config(
    page_title="Evolución del Volumen de la Producción Científica",
    layout="wide",
    initial_sidebar_state="collapsed"
)

main_title = "Evolución del Volumen de la Producción Científica"

#Pestaña 1 imagenes
sec_one_title = "Descripción General"

image_one_path = "assets/images/sec_1_img_1.png"
image_one_caption = "Producción científica del ICN en el Web of Science, 1968-2024"

image_two_path = "assets/images/sec_1_img_2.png"
image_two_caption = "Producción científica del ICN en el Web of Science, considerando sólo artículos y reviews y excluyendo grandes colaboraciones. 1968-2024"

#Pestaña 2 imagenes
sec_two_title = "Producción Anual"

image_three_path = "assets/images/sec_1_img_3.png"
image_three_caption = "Evolución de la producción científica del ICN en el Web of Science, 1968-2024"

image_four_path = "assets/images/sec_1_img_4.png"
image_four_caption = "Total de documentos publicados, por investigador, 1996-2024"

image_five_path = "assets/images/sec_1_img_5.jpeg"
image_five_caption = "Total de artículos, sin considerar grandes colaboraciones, publicados por investigador, 1996-2024"

#Pestaña 3 imagenes
sec_three_title = "Producción en Revistas con Factor de Impacto (Revistas JCR)"

image_six_path = "assets/images/sec_1_img_6.png"
image_six_caption = "Top 20 revistas donde más publica el ICN"

image_seven_path = "assets/images/sec_1_img_7.png"
image_seven_caption = "Top 20 revistas donde más se publica"

image_eight_path = "assets/images/sec_1_img_8.png"
image_eight_caption = "Ley de Bradford de las publicaciones científicas del ICN en todo el periodo"

#Para mostrar imagenes con caption y manejo de error
def display_image(path, caption):
    """Muestra la imagen con un caption centrado."""
    if not os.path.exists(path):
        st.warning(f"⚠️ Imagen no encontrada en: {path}. Asegúrate de que el directorio 'assets/images/' exista y contenga las imágenes.")
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
            st.session_state.interpretaciones["img1"] = generator(image_one_path, image_one_caption)
            st.session_state.interpretaciones["img2"] = generator(image_two_path, image_two_caption)
            st.session_state.interpretaciones["img3"] = generator(image_three_path, image_three_caption)
            st.session_state.interpretaciones["img4"] = generator(image_four_path, image_four_caption)
            st.session_state.interpretaciones["img5"] = generator(image_five_path, image_five_caption)
            st.session_state.interpretaciones["img6"] = generator(image_six_path, image_six_caption)
            st.session_state.interpretaciones["img7"] = generator(image_seven_path, image_seven_caption)
            st.session_state.interpretaciones["img8"] = generator(image_eight_path, image_eight_caption)
            st.session_state.generadas = True

st.markdown("---")

st.header("Información Destacada")
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric("Documentos Totales", "6,153", delta="Publicados hasta 2024")
with metric_col2:
    st.metric("Citas Promedio (Global)", "22.14", delta_color="inverse")
with metric_col3:
    st.metric("Tasa de Crecimiento Anual", "8.88%", delta="Alta")
with metric_col4:
    st.metric("Colaboración Internacional", "56.17%", delta="Sólida")


#PESTAÑAS
tab1, tab2, tab3 = st.tabs([f"1. {sec_one_title}", f"2. {sec_two_title}", f"3. {sec_three_title}"])

#=========================================================================
#PESTAÑA 1
#=========================================================================
with tab1:
    st.subheader("Análisis de la Colección Global vs. Sin Grandes Colaboraciones")

    #Fila 1
    col1, col2 = st.columns([1.6, 1.4])
    with col1:
        display_interpretacion("img1", image_one_path, image_one_caption)

    with col2:
        display_image(image_one_path, image_one_caption)

    st.markdown("---")

    #Fila 2
    st.markdown("### Colección Principal (Artículos y Reviews, Sin Grandes Colaboraciones)") 

    col1, col2 = st.columns([1.6, 1.4])
    with col1:
        display_interpretacion("img2", image_two_path, image_two_caption)

    with col2:
        display_image(image_two_path, image_two_caption)

#=========================================================================
#PESTAÑA 2
#=========================================================================
with tab2:
    st.subheader("Evolución de la Productividad a lo largo del tiempo")

    #Fila 1
    col1, col2 = st.columns(2)
    with col1:
        display_interpretacion("img3", image_three_path, image_three_caption)
        	
    with col2:
        display_image(image_three_path, image_three_caption)

    st.markdown("---")
    st.subheader("Producción Ajustada por Investigador")

    #Fila 2
    col3, col4 = st.columns(2)
    with col3:
        display_image(image_four_path, image_four_caption)

        display_interpretacion("img4", image_four_path, image_four_caption)

    with col4:
        display_image(image_five_path, image_five_caption)

        display_interpretacion("img5", image_five_path, image_five_caption)

#=========================================================================
#PESTAÑA 3
#=========================================================================
with tab3:
    st.subheader("Análisis de las Fuentes de Publicación")

    #Fila 1
    col1, col2 = st.columns([0.6, 1.4])
    with col1:
        display_interpretacion("img6", image_six_path, image_six_caption)

    with col2:
        display_image(image_six_path, image_six_caption)

    #Fila 2
    col3, col4 = st.columns([1, 1])
    with col3:
        display_image(image_seven_path, image_seven_caption)
    with col4:
        display_interpretacion("img7", image_seven_path, image_seven_caption)

    st.markdown("---")
    st.subheader("Ley de Bradford")

    display_image(image_eight_path, image_eight_caption)

    display_interpretacion("img8", image_eight_path, image_eight_caption)

st.markdown("---")
