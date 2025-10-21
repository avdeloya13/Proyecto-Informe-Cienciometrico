#SECCION 4

import streamlit as st
import os

# --- Configuración de la Página (Título, Ícono, Layout) ---
st.set_page_config(
    page_title="Reporte Cienciométrico - Sección 4",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Definimos las variables de texto e imágenes (Adaptadas al contenido temático)
main_title = "Caracterización Temática de la Producción Científica"

# --- Subsección 1: Distribución por Área de Investigación ---
sec_one_title = "Distribución por Área de Investigación"
sec_one_text1 = "La producción científica del ICN está clasificada en diversas áreas de conocimiento. El análisis por categorías del Web of Science revela que las 5 principales áreas, basadas en el número de artículos, son Física, Astrofísica, Ciencias de la Computación, Matemáticas y Química. Aproximadamente el 65% de la producción se concentra en Física y Astrofísica, lo que refleja el núcleo tradicional de la institución. En la Fig. 16 se muestra el porcentaje de documentos por área temática, evidenciando el enfoque principal del ICN."
image_one_path = "assets/images/sec_4_img_1.png"
image_one_caption = "Fig. 16. Distribución de documentos por área de investigación (Top 15 categorías WoS)"

# --- Subsección 2: Evolución de los Temas de Investigación ---
sec_two_title = "Evolución de los Temas de Investigación"
sec_two_text1 = "El análisis de las palabras clave (autor y WoS) a través del tiempo permite identificar las tendencias temáticas. Se observa que los temas tradicionales del ICN (Física de Altas Energías, Relatividad) mantienen una presencia constante. Sin embargo, hay un crecimiento notable en la presencia de términos asociados a áreas emergentes como Inteligencia Artificial (IA) aplicada a la física, Ciencia de Datos y nuevos materiales. La Fig. 17 ilustra la evolución de los temas principales a lo largo del periodo, identificando focos de crecimiento y estabilización."
image_two_path = "assets/images/sec_4_img_2.png"
image_two_caption = "Fig. 17. Evolución temporal de la prominencia de temas clave de investigación"

# --- Subsección 3: Mapa de Co-ocurrencia de Palabras Clave ---
sec_three_title = "Estructura Temática y Mapa de la Ciencia"
sec_three_text1 = "El mapa de co-ocurrencia de palabras clave (Fig. 18) es una herramienta poderosa para visualizar la estructura interna de la investigación. Cada nodo representa un tema o palabra clave, y los enlaces representan la co-ocurrencia de estos términos en los mismos documentos, formando clústeres temáticos. Se identifican típicamente 4 o 5 clústeres principales que definen las líneas de investigación del ICN. La densidad de los clústeres sugiere una fuerte especialización, mientras que los enlaces entre ellos indican áreas de interdisciplinaridad."
image_three_path = "assets/images/sec_4_img_3.png"
image_three_caption = "Fig. 18. Mapa de co-ocurrencia de palabras clave. Nodos = Palabras clave, Bordes = Co-ocurrencia."

sec_three_text2 = "Los clústeres identificados son consistentes con las Divisiones y Grupos de Trabajo del ICN, reflejando una estructura temática bien definida pero también interconectada. Esta interconectividad es un signo positivo de colaboración interna y potencial para proyectos interdisciplinarios."


# --- Secciones del Informe (para el menú final) ---
sec_nav_title1 = "Evolución del Volumen de la Producción Científica"
sec_nav_title2 = "Impacto de la Producción Científica"
sec_nav_title3 = "Análisis de la Colaboración"
sec_nav_title5 = "Contribución a los Objetivos de Desarrollo Sostenible (ODS)"


# Función auxiliar para mostrar imágenes con caption y manejo de error.
def display_image(path, caption):
    """Muestra la imagen con un caption centrado."""
    if not os.path.exists(path):
        st.warning(f"⚠️ Imagen no encontrada en: {path}. Asegúrate de que el directorio 'assets/images/' exista y contenga las imágenes.")
        st.info(f"Placeholder para: {caption}")
        st.image("https://placehold.co/600x460/cccccc/333333?text=IMAGEN+FALTANTE", caption=caption, width="stretch")
    else:
        st.image(path, caption=caption, width="stretch")


# ----------------------------------------------------
# APLICACIÓN PRINCIPAL
# ----------------------------------------------------

st.title(main_title)
st.markdown("---")

# --- Bloque de Métricas Resumen ---
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

st.markdown("---")


# --- Bloque Principal con Pestañas (Tabs) ---
tab1, tab2, tab3 = st.tabs([f"1. {sec_one_title}", f"2. {sec_two_title}", f"3. {sec_three_title}"])

# =========================================================================
# PESTAÑA 1: DISTRIBUCIÓN POR ÁREA
# =========================================================================
with tab1:
    st.subheader(sec_one_title)

    # Fila 1: Texto y Fig. 16 (Distribución de Áreas)
    col1, col2 = st.columns([0.6, 1.4])
    with col1:
        st.markdown(sec_one_text1)
        st.info("La concentración en áreas troncales es esperada, pero la presencia de otras áreas (Computación, Biofísica) indica diversificación.")
    with col2:
        display_image(image_one_path, image_one_caption)


# =========================================================================
# PESTAÑA 2: EVOLUCIÓN DE LOS TEMAS
# =========================================================================
with tab2:
    st.subheader(sec_two_title)

    # Fila 1: Fig. 17 (Evolución Temporal)
    col1, col2 = st.columns([1.5, 0.5])
    with col1:
        display_image(image_two_path, image_two_caption)
    with col2:
        st.markdown(sec_two_text1)
        st.success("El surgimiento de temas como IA y Ciencia de Datos reflejan la adaptación del ICN a las metodologías modernas de la física teórica y experimental.")


# =========================================================================
# PESTAÑA 3: ESTRUCTURA TEMÁTICA Y MAPA DE LA CIENCIA
# =========================================================================
with tab3:
    st.subheader(sec_three_title)

    # Fila 1: Texto y Fig. 18 (Mapa de Co-ocurrencia)
    col1, col2 = st.columns([0.6, 1.4])
    with col1:
        st.markdown(sec_three_text1)
        st.markdown(sec_three_text2)
    with col2:
        display_image(image_three_path, image_three_caption)

    st.markdown("---")
    st.caption("Los clústeres identificados corresponden a la estructura de investigación del ICN: Física Teórica, Astrofísica y Cosmología, Materiales y Nanociencias, y Biofísica.")

