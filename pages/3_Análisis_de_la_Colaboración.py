#SECCION 3

import streamlit as st
import os

st.set_page_config(
    page_title="Reporte Cienciométrico - Sección 3",
    layout="wide",
    initial_sidebar_state="collapsed"
)

main_title = "Análisis de la Colaboración"

# --- Subsección 1: Colaboracion en el ICN ---
sec_one_title = "Colaboración Interdepartamental"
sec_one_text0 = "Para el estudio de la red de colaboración entre los investigadores del ICN, se extrajo información de todos los artículos arbitrados publicados entre 2014 y 2024 (excluyendo grandes colaboraciones) incluidos en el Sistema Integral de Gestión de Información del ICN. Mediante un script programado en PHP se obtuvo la información en formato json de VOSViewer que posteriormente fue exportado a formato GML para ser procesado con el programa GEPHI. Cada nodo representa un investigador, y su tamaño es proporcional al número de artículos publicados durante el período de estudio. Las conexiones entre investigadores indican coautorías, el grosor de las líneas es proporcional al número de colaboraciones entre ellos. Los departamentos en la Fig. 13 son representados por diferentes colores, mientras que en la Fig. 14 se representan con diferentes figuras (círculos, triángulos, cuadrados, etc.)."
sec_one_text1_1="La agrupación obtenida en la Fig. 13 se obtuvo usando el algoritmo de disposición Contraction y en la Fig. 14 se empleó el algoritmo Force Atlas con los parámetros por defecto. Para la detección de los clústeres, se usó el algoritmo Modularity, también con los parámetros por defecto, incluido en el panel Statistics."
sec_one_text1= "En la Fig. 14 se muestra la agrupación de los investigadores en 17 clústeres, algunos de los cuales combinan investigadores de varios departamentos (nodos con diferentes formas). Por ejemplo, el cluster azul celeste está formado por investigadores de los departamentos de Física de Altas Energías, Estructura de la Materia, Física de Plasmas y del departamento de Gravitación. En este cluster, se encuentran los investigadores cuya actividad está asociada fuertemente con el C3."
image_one_path = "assets/images/sec_3_img_1.png"
image_one_caption = "Figura 13. Red de colaboración entre investigadores del ICN 2014-2024. Fuente: SIGI"
image_two_path = "assets/images/sec_3_img_2.png"
image_two_caption = "Figura 14. Red de colaboración entre investigadores del ICN 2014-2024. Fuente: SIGI"

# --- Subsección 2: Colaboracion Nacional ---
sec_two_title = "Colaboración Nacional"
sec_two_text1 = "Desde el punto de vista nacional, las principales colaboraciones son con la propia UNAM."
image_three_path = "assets/images/sec_3_img_3.png"

# --- Subsección 3: Distribución de la Colaboración Internacional ---
sec_three_title = "Distribución de la Colaboración Internacional"
sec_three_text1 = "La colaboración internacional está distribuida en 90 países. En la Fig. 15 se muestran los 20 países con mayor colaboración con el ICN. El país con mayor colaboración es Estados Unidos (USA), seguido por España (Spain) y Alemania (Germany). Esta distribución es consistente con los patrones de colaboración de las instituciones mexicanas, dado la cercanía geográfica y las relaciones históricas con estos países. Además, se observa una colaboración importante con países de Europa y Asia. La colaboración con instituciones de América Latina es importante, siendo Chile y Brasil los países más representativos."
image_three_path = "assets/images/sec_3_img_3.png"
image_three_caption = "Fig. 15. Colaboración internacional por país (Top 20 países)"

sec_three_text2 = "La colaboración con instituciones en Estados Unidos (USA) es del 19.33% y con instituciones de España (Spain) es del 5.16%."
sec_three_text3 = "En la Tabla 2 se muestra la colaboración por país, incluyendo la producción científica, el número de instituciones colaboradoras y el número de autores. Se observa que Estados Unidos es el país con mayor número de instituciones colaboradoras (543) y el mayor número de autores (2,228). Esta información confirma la importancia de la colaboración con Estados Unidos."
image_four_path = "assets/images/sec_3_img_4.png"
image_four_caption = "Tabla 2. Colaboración internacional del ICN por país"


# --- Secciones del Informe (para el menú final) ---
sec_nav_title1 = "Evolución del Volumen de la Producción Científica"
sec_nav_title2 = "Impacto de la Producción Científica"
sec_nav_title4 = "Caracterización Temática de la Producción Científica"
sec_nav_title5 = "Contribución a los Objetivos de Desarrollo Sostenible (ODS)"

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
    st.metric("Media Autores / Documento", "4.01", help="Excluyendo grandes colaboraciones")
with metric_col2:
    st.metric("Coautoría Internacional", "56.17%", delta="Alta proyección")
with metric_col3:
    st.metric("Países Colaboradores", "90")
with metric_col4:
    st.metric("País Principal", "USA", delta="19.33% de la colaboración")

st.markdown("---")


#PESTAÑAS
tab1, tab2, tab3 = st.tabs([f"1. {sec_one_title}", f"2. {sec_two_title}", f"3. {sec_three_title}"])

# =========================================================================
# PESTAÑA 1
# =========================================================================
with tab1:
    st.subheader(sec_one_title)
    st.markdown(sec_one_text0)

    col1, col2 = st.columns([0.6, 1.4])
    with col1:
        st.markdown(sec_one_text1_1)
        st.info("En la Fig. 13 se observa que las principales colaboraciones ocurren entre investigadores que pertenecen a un mismo departamento. Además, dentro de un mismo departamento, se observan subgrupos con fuerte colaboración interna pero poca colaboración con otros subgrupos.")  
    with col2:
        display_image(image_one_path, image_one_caption)

    st.markdown(sec_two_text1)
    display_image(image_two_path, image_two_caption)


# =========================================================================
# PESTAÑA 2
# =========================================================================
with tab2:
    st.subheader(sec_two_title)

    col1, col2 = st.columns([1.5, 0.5])
    with col1:
        display_image(image_two_path, image_two_caption)
    with col2:
        st.markdown(sec_two_text1)
        st.success(f"La tendencia al alza es un indicador positivo, alcanzando un pico de **78.38% en 2024**.")


# =========================================================================
# PESTAÑA 3
# =========================================================================
with tab3:
    st.subheader(sec_three_title)

    # Fila 1: Texto y Fig. 15 (Top 20 Países)
    col1, col2 = st.columns([0.6, 1.4])
    with col1:
        st.markdown(sec_three_text1)
        st.markdown(sec_three_text2)
        st.markdown(sec_three_text3)
    with col2:
        display_image(image_three_path, image_three_caption)

    st.markdown("---")
    st.subheader("Detalle de la Colaboración por País")

    # Fila 2: Tabla 2 (Colaboración por País)
    st.info("La siguiente tabla resume la colaboración con los principales países, destacando el número de instituciones colaboradoras y autores.")
    display_image(image_four_path, image_four_caption)
