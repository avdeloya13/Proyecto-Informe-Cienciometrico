#SECCION 2

import streamlit as st
from llm.llm_generator import generator
import os

if "interpretaciones" not in st.session_state:
    st.session_state.interpretaciones = {}
    
if "generadas" not in st.session_state:
    st.session_state.generadas = False

st.set_page_config(
    page_title="Reporte Cienciométrico - Sección 2",
    layout="wide",
    initial_sidebar_state="collapsed"
)

main_title = "Impacto de la Producción Científica"

#Pestaña 1 imagenes
sec_one_title = "Análisis Comparativo"

image_one_path = "assets/images/sec_2_img_1.png"
image_one_caption = "Tabla 1. Indicadores de impacto"

#Pestaña 2 imagenes
sec_two_title = "Evolución del Impacto"

image_two_path = "assets/images/sec_2_img_2.png"
image_two_caption = "Citas recibidas por la producción científica del ICN en todo el periodo"

image_three_path = "assets/images/sec_2_img_3.png"
image_three_caption = "Category Normalized Citation Impact (CNCI) de la producción científica del ICN entre 1980 y 2024"

image_four_path = "assets/images/sec_2_img_4.png"
image_four_caption = "Porcentaje de documentos en top 1 de la producción científica del ICN entre 1980 y 2024"

image_five_path = "assets/images/sec_2_img_5.png"
image_five_caption = "Porcentaje de documentos en top 100 de la producción científica del ICN entre 1980 y 2024"

image_six_path = "assets/images/sec_2_img_6.png"
image_six_caption = "Average Percentile de la producción científica del ICN entre 1980 y 2024"

image_seven_path = "assets/images/sec_2_img_7.png"
image_seven_caption = "Evolución del perfil multidimensional de desempeño"

#Para mostrar imagenes con caption centrada y manejo de error.
def display_image(path, caption):
    if not os.path.exists(path):
        st.warning(f"⚠️ Imagen no encontrada en: {path}. Asegúrate de que el directorio 'assets/images/' exista y contenga las imágenes.")
        st.info(f"Placeholder para: {caption}")
        st.image("https://placehold.co/600x460/cccccc/333333?text=IMAGEN+FALTANTE", caption=caption, width="stretch")
    else:
        st.image(path, caption=caption, width="stretch")

#Para mostrar la interpretacion de la imagen cuya llave y path pasan como parametro
def display_interpretacion(img_key, img_path):
    if img_key in st.session_state.interpretaciones:
        st.markdown(st.session_state.interpretaciones[img_key])

        if st.button("Regenerar", key=f"regen_{img_key}"):
            st.session_state.interpretaciones[img_key] = st.empty()
            with st.spinner("Cargando..."):
                st.session_state.interpretaciones[img_key] = generator(img_path)
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
            st.session_state.interpretaciones["img9"] = generator(image_one_path)
            st.session_state.interpretaciones["img10"] = generator(image_two_path)
            st.session_state.interpretaciones["img11"] = generator(image_three_path)
            st.session_state.interpretaciones["img12"] = generator(image_four_path)
            st.session_state.interpretaciones["img13"] = generator(image_five_path)
            st.session_state.interpretaciones["img14"] = generator(image_six_path)
            st.session_state.interpretaciones["img15"] = generator(image_seven_path)
            st.session_state.generadas = True

st.markdown("---")

st.header("Indicadores de Impacto Clave")
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric(
        label="Media Autores / Documento", 
        value="4.01", 
        help="Excluyendo grandes colaboraciones, indica el tamaño promedio de los equipos de investigación."
    )
with metric_col2:
    st.metric(
        label="Coautoría Internacional", 
        value="56.17%", 
        delta="Alta proyección", 
        help="Porcentaje de documentos con al menos un autor de una institución extranjera."
    )
with metric_col3:
    st.metric(
        label="Países Colaboradores", 
        value="90", 
        help="Número total de países con al menos una coautoría con el ICN."
    )
with metric_col4:
    st.metric(
        label="Principal Colaborador", 
        value="USA", 
        delta="19.33% de la Colaboración Total",
        delta_color="normal",
        help="País con la mayor frecuencia de coautorías."
    )


#PESTAÑAS
tab1, tab2 = st.tabs([f"1. {sec_one_title}", f"2. {sec_two_title}"])

#=========================================================================
#PESTAÑA 1
#=========================================================================
with tab1:
    st.subheader("Métricas Relacionadas con el Impacto de las Publicaciones Científicas")

    col1, col2 = st.columns([2, 3]) #2/5 partes para texto, 3/5 para imagen
    with col1:
        display_interpretacion("img9", image_one_path)    

    with col2:   
        display_image(image_one_path, image_one_caption)

    st.markdown("---")

#=========================================================================
#PESTAÑA 2
#=========================================================================
with tab2:
    st.markdown("### CNCI: Impacto Normalizado por Categoría")

    col1, col2 = st.columns([2, 3]) #2/5 partes para texto, 3/5 para imagen
    with col1:
        display_interpretacion("img11", image_three_path)
       # st.success(" El impacto normalizado experimentó un crecimiento sostenido post-2005, superando consistentemente el promedio mundial (CNCI > 1) entre 2011 y 2016.")

    with col2:
        display_image(image_three_path, image_three_caption)

    st.markdown("---")

    st.markdown("### Top 1%: Artículos de Máxima Excelencia")
    
    col3, col4 = st.columns([3, 2])

    with col3:
        display_image(image_four_path, image_four_caption)

    with col4:
        display_interpretacion("img12", image_four_path)
        #st.info(" Aunque la presencia fue nula en los 80/90, el instituto registró picos de más del 5% de artículos en el Top 1% mundial entre 2010 y 2012.")

    st.markdown("---")

    st.markdown("### Perspectiva Global: Tendencia de Citas y Top 10%")
  #  st.markdown("Esta sección agrupa la evolución de la tendencia de citas brutas y el porcentaje en el Top 10%, permitiendo una visión comparativa del impacto amplio.")


    col5, col6 = st.columns(2) 
    with col5:
        st.markdown("#### **Citas Recibidas**")
        display_image(image_two_path, image_two_caption)
        with st.expander("Ver Definiciones de Métricas"):
            display_interpretacion("img10", image_two_path)

    with col6:
        st.markdown("#### **Documentos en Top 10%**")
        display_interpretacion("img13", image_five_path)
        display_image(image_five_path, image_five_caption)

    st.markdown("---")

    st.markdown("### Resumen y Perfil de Desempeño Final")
    #st.markdown("Las últimas dos figuras ofrecen una visión de resumen: el percentil promedio (rendimiento relativo) y un perfil multidimensional (integración de métricas).")

    col7, col8 = st.columns(2) 
    with col7:
        st.markdown("#### **Evolución del Percentil Promedio**")
        display_interpretacion("img14", image_six_path) #NUEVO
        display_image(image_six_path, image_six_caption)

    with col8:
        st.markdown("#### **Perfil Multidimensional de Desempeño**")
        display_interpretacion("img15", image_seven_path) #NUEVO
        display_image(image_seven_path, image_seven_caption)
