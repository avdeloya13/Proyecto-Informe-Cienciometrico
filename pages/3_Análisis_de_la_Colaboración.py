#SECCION 3

import streamlit as st
import os

st.set_page_config(
    page_title="Reporte Cienciométrico - Sección 3",
    layout="wide",
    initial_sidebar_state="collapsed"
)

main_title = "Análisis de la Colaboración"

# --- Subsección 1
sec_one_title = "Colaboración entre Investigadores del ICN"
sec_one_text1 = '''Para el estudio de la red de colaboración entre los investigadores del ICN, se extrajo información de todos los artículos arbitrados publicados entre 2014 y 2024 (excluyendo grandes colaboraciones) incluidos en el Sistema Integral de Gestión de Información del ICN. Mediante un script programado en PHP se obtuvo la información en formato json de VOSViewer que posteriormente fue exportado a formato GML para ser procesado con el programa GEPHI.'''
sec_one_text2 = '''Cada nodo representa un investigador, y su tamaño es proporcional al número de artículos publicados durante el período de estudio. Las conexiones entre investigadores indican coautorías, el grosor de las líneas es proporcional al número de colaboraciones entre ellos. Los departamentos en la Fig. 1 son representados por diferentes colores, mientras que en la Fig. 2 se representan con diferentes figuras (círculos, triángulos, cuadrados, etc.).'''
sec_one_text3 = '''La agrupación obtenida en la Fig. 1 se obtuvo usando el algoritmo de disposición Contraction y en la Fig. 2 se empleó el algoritmo Force Atlas con los parámetros por defecto. Para la detección de los clústeres, se usó el algoritmo Modularity, también con los parámetros por defecto, incluido en el panel Statistics. \n\nEn la Fig. 1 se observa que las principales colaboraciones ocurren entre investigadores que pertenecen a un mismo departamento. Además, dentro de un mismo departamento, se observan subgrupos con fuerte colaboración interna pero poca colaboración con otros subgrupos.'''
image_one_path = "assets/images/sec_3_img_1.png"
image_one_caption = "Fig. 1. Red de colaboración entre investigadores del ICN 2014-2024. Fuente: SIGI"

sec_one_text4 = '''En la Fig. 2. se muestra la agrupación de los investigadores en 17 clústeres, algunos de los cuales combinan investigadores de varios departamentos (nodos con diferentes formas). Por ejemplo, el cluster azul celeste está formado por investigadores de los departamentos de Física de Altas Energías, Estructura de la Materia, Física de Plasmas y del departamento de Gravitación. En este cluster, se encuentran los investigadores cuya actividad está asociada fuertemente con el C3.'''
image_two_path = "assets/images/sec_3_img_2.png"
image_two_caption = "Figura 2. Red de colaboración entre investigadores del ICN 2014-2024. Fuente: SIGI"

# --- Subsección 2
sec_two_title = "Colaboración Nacional"
sec_two_text1 = '''Desde el punto de vista nacional, las principales colaboraciones son con la propia UNAM.'''
image_three_path = "assets/images/sec_3_img_3.png"
image_four_path = "assets/images/sec_3_img_4.png"

# --- Subsección 3
sec_three_title = '''Colaboración Internacional'''
image_five_path = "assets/images/sec_3_img_5.png"
image_five_caption = "Figura. Distribución y agrupamiento de los países colaboradores con el ICN de acuerdo a los porcentajes de las publicaciones en revistas Q1, Q2, Q3 y Q4. Se escogieron 36 países con los que se ha tenido una mayor colaboración en el periodo 1980-2024."
image_six_path = "assets/images/sec_3_img_6.png"
image_six_caption = "Figura. Distribución y agrupamiento de los países colaboradores con el ICN de acuerdo a los porcentajes de las publicaciones en revistas Q1, Q2, Q3 y Q4. Se escogieron 40 países con los que se ha tenido una mayor colaboración en el periodo 2024-2024."
image_seven_path = "assets/images/sec_3_img_7.png"
image_seven_caption = "Figura. Distribución y agrupamiento de los perfiles de desempeño de las colaboraciones del ICN con un grupo de países. Se escogieron 36 países con los que se ha tenido una mayor colaboración en el periodo 1980-2024."
image_eight_path = "assets/images/sec_3_img_8.png"
image_eight_caption = "Figura. Distribución y agrupamiento de los perfiles de desempeño de las colaboraciones del ICN con un grupo de países. Se escogieron 39 países con los que se ha tenido una mayor colaboración en el periodo 2020-2024."

# --- Subsección 4
sec_four_title = "Género"
sec_four_text1 = '''Las mujeres están presentes en la mayoría de los clusters, pero en general sus nodos son más pequeños (menos publicaciones o conexiones). En el cluster gris, destaca la producción de una doctora.'''
image_nine_path = "assets/images/sec_3_img_9.png"

#Para mostrar imágenes con caption y manejo de error.
def display_image(path, caption):
    """Muestra la imagen con un caption centrado."""
    if not os.path.exists(path):
        st.warning(f"⚠️ Imagen no encontrada en: {path}. Asegúrate de que el directorio 'assets/images/' exista y contenga las imágenes.")
        st.info(f"Placeholder para: {caption}")
        st.image("https://placehold.co/600x460/cccccc/333333?text=IMAGEN+FALTANTE", caption=caption, width="stretch")
    else:
        st.image(path, caption=caption, width="stretch")

st.title(main_title)
st.markdown("---")

st.header("Indicadores Clave de Colaboración")

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
tab1, tab2, tab3, tab4 = st.tabs([f"Interdepartamental", f"Nacional", f"Internacional", f"4. {sec_four_title}"])

# =========================================================================
# PESTAÑA 1
# =========================================================================
with tab1:
    st.subheader(sec_one_title)
    st.markdown(sec_one_text1)
    st.markdown(sec_one_text2)

    col1_1, col1_2 = st.columns([2, 3])

    with col1_1:
        st.markdown(sec_one_text3.replace('<br />', '\n'))

    with col1_2:
        display_image(image_one_path, caption=image_one_caption)

    col1_3, col1_4 = st.columns([3, 2])

    with col1_3:
        display_image(image_two_path, caption=image_two_caption)

    with col1_4:
        st.markdown(sec_one_text4)
    

# =========================================================================
# PESTAÑA 2
# =========================================================================
with tab2:
    st.subheader(sec_two_title)
    st.info(sec_two_text1)

    col2_1, col2_2 = st.columns(2)

    with col2_1:
        display_image(image_three_path, "Colaboración Nacional con la UNAM")

    with col2_2:
        display_image(image_four_path, "Colaboración Nacional con la UNAM")

st.divider()


# =========================================================================
# PESTAÑA 3
# =========================================================================
with tab3:
    st.subheader(sec_three_title)

    st.info("Análisis de países colaboradores basado en el porcentaje de publicaciones en revistas del cuartil Q1 al Q4.")
    col3_1, col3_2 = st.columns(2)
    with col3_1:
        st.subheader("Periodo 1980-2024")
        display_image(image_five_path, image_five_caption)
    with col3_2:
        st.subheader("Periodo 2020-2024")
        display_image(image_six_path, image_six_caption)


    st.info("Distribución y agrupación de países según sus perfiles de desempeño (impacto normalizado, etc.).")
    col3_3, col3_4 = st.columns(2)
    with col3_3:
        st.subheader("Periodo 1980-2024")
        display_image(image_seven_path, image_seven_caption)
    with col3_4:
        st.subheader("Periodo 2020-2024")
        display_image(image_eight_path, image_eight_caption)

    st.divider()

# =========================================================================
# PESTAÑA 4
# =========================================================================
with tab4:
    st.subheader(sec_four_title)

    col1_1, col1_2 = st.columns([2, 2])

    with col1_1: 
        st.markdown(sec_four_text1)

    with col1_2: 
        display_image(image_nine_path, "Distribución de Género en la Red de Colaboración")