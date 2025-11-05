import streamlit as st
import os

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Sección 3: Análisis de la Colaboración",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Variables de Contenido (Mantenidas del código original) ---

# Encabezado sección principal 
main_title_section = "3. Análisis de la Colaboración"

# Sección 1: Interdepartamental
sec_one_title = '''Interdepartamental'''
sec_one_text1 = '''Para el estudio de la red de colaboración entre los investigadores del ICN, se extrajo información de todos los artículos arbitrados publicados entre 2014 y 2024 (excluyendo grandes colaboraciones) incluidos en el Sistema Integral de Gestión de Información del ICN. Mediante un script programado en PHP se obtuvo la información en formato json de VOSViewer que posteriormente fue exportado a formato GML para ser procesado con el programa GEPHI.'''
sec_one_text2 = '''Cada nodo representa un investigador, y su tamaño es proporcional al número de artículos publicados durante el período de estudio. Las conexiones entre investigadores indican coautorías, el grosor de las líneas es proporcional al número de colaboraciones entre ellos. Los departamentos en la Fig. 13 son representados por diferentes colores, mientras que en la Fig. 14 se representan con diferentes figuras (círculos, triángulos, cuadrados, etc.).'''
sec_one_text3 = '''La agrupación obtenida en la figura 13 se obtuvo usando el algoritmo de disposición Contraction y en la Fig. 14 se empleó el algoritmo Force Atlas con los parámetros por defecto. Para la detección de los clústeres, se usó el algoritmo Modularity, también con los parámetros por defecto, incluido en el panel Statistics. \n\nEn la Fig. 13 se observa que las principales colaboraciones ocurren entre investigadores que pertenecen a un mismo departamento. Además, dentro de un mismo departamento, se observan subgrupos con fuerte colaboración interna pero poca colaboración con otros subgrupos.'''
image_one_path = "assets/images/sec_3_img_1.png"
image_one_caption = "Figura 13. Red de colaboración entre investigadores del ICN 2014-2024. Fuente: SIGI"

sec_one_text4 = '''En la Fig. 14 se muestra la agrupación de los investigadores en 17 clústeres, algunos de los cuales combinan investigadores de varios departamentos (nodos con diferentes formas). Por ejemplo, el cluster azul celeste está formado por investigadores de los departamentos de Física de Altas Energías, Estructura de la Materia, Física de Plasmas y del departamento de Gravitación. En este cluster, se encuentran los investigadores cuya actividad está asociada fuertemente con el C3.'''
image_two_path = "assets/images/sec_3_img_2.png"
image_two_caption = "Figura 14. Red de colaboración entre investigadores del ICN 2014-2024. Fuente: SIGI"

# Sección 2: Colaboración Nacional
sec_two_title = '''Colaboración Nacional'''
sec_two_text1 = '''Desde el punto de vista nacional, las principales colaboraciones son con la propia UNAM.'''
image_three_path = "assets/images/sec_3_img_3.png"
image_four_path = "assets/images/sec_3_img_4.png"

# Sección 3: Colaboración Internacional
sec_three_title = '''Colaboración Internacional'''
image_five_path = "assets/images/sec_3_img_5.png"
image_five_caption = "Figura. Distribución y agrupamiento de los países colaboradores con el ICN de acuerdo a los porcentajes de las publicaciones en revistas Q1, Q2, Q3 y Q4. Se escogieron 36 países con los que se ha tenido una mayor colaboración en el periodo 1980-2024."
image_six_path = "assets/images/sec_3_img_6.png"
image_six_caption = "Figura. Distribución y agrupamiento de los países colaboradores con el ICN de acuerdo a los porcentajes de las publicaciones en revistas Q1, Q2, Q3 y Q4. Se escogieron 40 países con los que se ha tenido una mayor colaboración en el periodo 2024-2024."
image_seven_path = "assets/images/sec_3_img_7.png"
image_seven_caption = "Figura. Distribución y agrupamiento de los perfiles de desempeño de las colaboraciones del ICN con un grupo de países. Se escogieron 36 países con los que se ha tenido una mayor colaboración en el periodo 1980-2024."
image_eight_path = "assets/images/sec_3_img_8.png"
image_eight_caption = "Figura. Distribución y agrupamiento de los perfiles de desempeño de las colaboraciones del ICN con un grupo de países. Se escogieron 39 países con los que se ha tenido una mayor colaboración en el periodo 2020-2024."

# Sección 4: Género
sec_four_title = '''Género'''
sec_four_text1 = '''Las mujeres están presentes en la mayoría de los clusters, pero en general sus nodos son más pequeños (menos publicaciones o conexiones). En el cluster gris, destaca la producción de una doctora.'''
image_nine_path = "assets/images/sec_3_img_9.png"


# --- Estructura del Dashboard ---

# Título Principal
st.title(main_title_section)
st.markdown("---")


# 1. Sección Interdepartamental
st.header(f":dart: {sec_one_title}")

st.markdown(sec_one_text1)
st.markdown(sec_one_text2)

# Columna 1 para texto y Columna 2 para Figura 13
col1_1, col1_2 = st.columns([3, 2])

with col1_1:
    # Reemplazo el <br /> por doble salto de línea en Markdown
    st.markdown(sec_one_text3.replace('<br />', '\n'))

with col1_2:
    try:
        st.image(image_one_path, caption=image_one_caption, use_column_width=True)
    except FileNotFoundError:
        st.warning(f"No se encontró la imagen: {image_one_path}. Asegúrate de que esté en la carpeta 'images'.")

st.markdown(sec_one_text4)

# Figura 14 a ancho completo
try:
    st.image(image_two_path, caption=image_two_caption, use_column_width=True)
except FileNotFoundError:
    st.warning(f"No se encontró la imagen: {image_two_path}. Asegúrate de que esté en la carpeta 'images'.")

st.markdown("---")


# 2. Sección Colaboración Nacional
st.header(f":flag-mx: {sec_two_title}")
st.markdown(sec_two_text1)

# Imágenes 3 y 4 en columnas
col2_1, col2_2 = st.columns(2)

with col2_1:
    try:
        st.image(image_three_path, caption="Colaboración Nacional con UNAM (Gráfica 1)", use_column_width=True)
    except FileNotFoundError:
        st.warning(f"No se encontró la imagen: {image_three_path}")

with col2_2:
    try:
        st.image(image_four_path, caption="Colaboración Nacional con UNAM (Gráfica 2)", use_column_width=True)
    except FileNotFoundError:
        st.warning(f"No se encontró la imagen: {image_four_path}")

st.markdown("---")


# 3. Sección Colaboración Internacional
st.header(f":globe_with_meridians: {sec_three_title}")

# Imágenes en dos filas de dos columnas
st.subheader("Publicaciones Q1-Q4")
col3_1, col3_2 = st.columns(2)
with col3_1:
    try:
        st.image(image_five_path, caption=image_five_caption, use_column_width=True)
    except FileNotFoundError:
        st.warning(f"No se encontró la imagen: {image_five_path}")

with col3_2:
    try:
        st.image(image_six_path, caption=image_six_caption, use_column_width=True)
    except FileNotFoundError:
        st.warning(f"No se encontró la imagen: {image_six_path}")

st.subheader("Perfiles de Desempeño")
col3_3, col3_4 = st.columns(2)
with col3_3:
    try:
        st.image(image_seven_path, caption=image_seven_caption, use_column_width=True)
    except FileNotFoundError:
        st.warning(f"No se encontró la imagen: {image_seven_path}")

with col3_4:
    try:
        st.image(image_eight_path, caption=image_eight_caption, use_column_width=True)
    except FileNotFoundError:
        st.warning(f"No se encontró la imagen: {image_eight_path}")

st.markdown("---")


# 4. Sección Género
st.header(f":female-scientist: {sec_four_title}")
st.markdown(sec_four_text1)

# Imagen 9 a ancho completo
try:
    st.image(image_nine_path, caption="Distribución de Género en la Red de Colaboración", use_column_width=True)
except FileNotFoundError:
    st.warning(f"No se encontró la imagen: {image_nine_path}")
