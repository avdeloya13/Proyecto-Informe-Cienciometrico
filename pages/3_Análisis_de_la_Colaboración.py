#SECCION 3

import streamlit as st
from llm.llm_generator import generator
import os

if "interpretaciones" not in st.session_state:
    st.session_state.interpretaciones = {}
    
if "generadas" not in st.session_state:
    st.session_state.generadas = False

st.set_page_config(
    page_title="Análisis de la Colaboración",
    layout="wide",
    initial_sidebar_state="collapsed"
)

main_title = "Análisis de la Colaboración"

#Pestaña 1 imagenes
sec_one_title = "Colaboración entre Investigadores del ICN"

image_one_path = "assets/images/sec_3_img_1.png"
image_one_caption = "Red de colaboración entre investigadores del ICN 2014-2024. Fuente: SIGI"

image_two_path = "assets/images/sec_3_img_2.png"
image_two_caption = "Red de colaboración entre investigadores del ICN 2014-2024. Fuente: SIGI"

#Pestaña 2 imagenes
sec_two_title = "Colaboración Nacional"

image_three_path = "assets/images/sec_3_img_3.png"
image_three_caption = "Colaboración Nacional con la UNAM"

image_four_path = "assets/images/sec_3_img_4.png"
image_four_caption = "Colaboración Nacional con la UNAM"

# --- Subsección 3
sec_three_title = '''Colaboración Internacional'''

image_five_path = "assets/images/sec_3_img_5.png"
image_five_caption = "Distribución y agrupamiento de los países colaboradores con el ICN de acuerdo a los porcentajes de las publicaciones en revistas Q1, Q2, Q3 y Q4. Se escogieron 36 países con los que se ha tenido una mayor colaboración en el periodo 1980-2024."

image_six_path = "assets/images/sec_3_img_6.png"
image_six_caption = "Distribución y agrupamiento de los países colaboradores con el ICN de acuerdo a los porcentajes de las publicaciones en revistas Q1, Q2, Q3 y Q4. Se escogieron 40 países con los que se ha tenido una mayor colaboración en el periodo 2024-2024."

image_seven_path = "assets/images/sec_3_img_7.png"
image_seven_caption = "Distribución y agrupamiento de los perfiles de desempeño de las colaboraciones del ICN con un grupo de países. Se escogieron 36 países con los que se ha tenido una mayor colaboración en el periodo 1980-2024."

image_eight_path = "assets/images/sec_3_img_8.png"
image_eight_caption = "Distribución y agrupamiento de los perfiles de desempeño de las colaboraciones del ICN con un grupo de países. Se escogieron 39 países con los que se ha tenido una mayor colaboración en el periodo 2020-2024."

# --- Subsección 4
sec_four_title = "Género"

image_nine_path = "assets/images/sec_3_img_9.png"
image_nine_caption = "Distribución de Género en la Red de Colaboración"

#Para mostrar imágenes con caption y manejo de error.
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
            st.session_state.interpretaciones["img16"] = generator(image_one_path, image_one_caption)
            st.session_state.interpretaciones["img17"] = generator(image_two_path, image_two_caption)
            st.session_state.interpretaciones["img18"] = generator(image_three_path, image_three_caption)
            st.session_state.interpretaciones["img19"] = generator(image_four_path, image_four_caption)
            st.session_state.interpretaciones["img20"] = generator(image_five_path, image_five_caption)
            st.session_state.interpretaciones["img21"] = generator(image_six_path, image_six_caption)
            st.session_state.interpretaciones["img22"] = generator(image_seven_path, image_seven_caption)
            st.session_state.interpretaciones["img23"] = generator(image_eight_path, image_eight_caption)
            st.session_state.interpretaciones["img24"] = generator(image_nine_path, image_nine_caption)
            st.session_state.generadas = True

st.markdown("---")

st.header("Indicadores Clave de Colaboración")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric("Principal Colaborador Nacional", "UNAM")
with metric_col2:
    st.metric("Periodo de Coautoría Internacional", "1980 - 2024", help="Periodo analizado.")
with metric_col3:
    st.metric("Países Colaboradores", "40", help="Cantidad máxima de países analizados, con al menos una coautoría con el ICN.")
with metric_col4:
    st.metric("Género Predominante en Colaboradores", "Masculino", help="Excluyendo grandes colaboraciones, indica el tamaño promedio de los equipos de investigación.")


#PESTAÑAS
tab1, tab2, tab3, tab4 = st.tabs([f"Interdepartamental", f"Nacional", f"Internacional", f"4. {sec_four_title}"])

#=========================================================================
#PESTAÑA 1
#=========================================================================
with tab1:
    st.subheader(sec_one_title)

    col1, col2 = st.columns([2, 3])
    with col1:
        display_interpretacion("img16", image_one_path, image_one_caption)

    with col2:
        display_image(image_one_path, caption=image_one_caption)

    col3, col4 = st.columns([3, 2])
    with col3:
        display_image(image_two_path, caption=image_two_caption)

    with col4:
        display_interpretacion("img17", image_two_path, image_two_caption)

    st.markdown("---")

#=========================================================================
#PESTAÑA 2
#=========================================================================
with tab2:
    st.subheader(sec_two_title)

    col1, col2 = st.columns(2)
    with col1:
        display_image(image_three_path, image_three_caption)

    with col2:
        display_interpretacion("img18", image_three_path)

    col3, col4 = st.columns(2)
    with col3:
        display_interpretacion("img19", image_four_path)

    with col4:
        display_image(image_four_path, image_four_caption)

    st.markdown("---")

# =========================================================================
# PESTAÑA 3
# =========================================================================
with tab3:
    st.subheader(sec_three_title)

    #st.info("Análisis de países colaboradores basado en el porcentaje de publicaciones en revistas del cuartil Q1 al Q4.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### **Periodo 1980-2024**")
        with st.expander("Ver Detalles"):
            display_interpretacion("img20", image_five_path, image_five_caption)

        display_image(image_five_path, image_five_caption)

    with col2:
        st.markdown("#### **Periodo 2020-2024**")
        with st.expander("Ver Detalles"):
            display_interpretacion("img21", image_six_path, image_six_caption)
        
        display_image(image_six_path, image_six_caption)

    #st.info("Distribución y agrupación de países según sus perfiles de desempeño (impacto normalizado, etc.).")
    col3_3, col3_4 = st.columns(2)
    with col3_3:
        st.markdown("#### **Periodo 1980-2024**")
        with st.expander("Ver Detalles"):
            display_interpretacion("img22", image_seven_path, image_seven_caption)

        display_image(image_seven_path, image_seven_caption)

    with col3_4:
        st.markdown("#### **Periodo 2020-2024**") #ERROR
        with st.expander("Ver Detalles"):
            display_interpretacion("img23", image_eight_path, image_eight_caption)
        
        display_image(image_eight_path, image_eight_caption)

    st.markdown("---")

# =========================================================================
# PESTAÑA 4
# =========================================================================
with tab4:
    st.subheader(sec_four_title)

    col1, col2 = st.columns([2, 2])
    with col1: 
        display_interpretacion("img24", image_nine_path)

    with col2: 
        display_image(image_nine_path, image_nine_caption)

    st.markdown("---")