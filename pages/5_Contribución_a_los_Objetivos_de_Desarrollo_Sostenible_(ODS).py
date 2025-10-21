#SECCION 5

import streamlit as st
import os

# --- Configuración de la Página (Título, Ícono, Layout) ---
st.set_page_config(
    page_title="Reporte Cienciométrico - Sección 5",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Definimos las variables de texto e imágenes (Adaptadas al contenido ODS)
main_title = "Contribución a los Objetivos de Desarrollo Sostenible (ODS)"

# --- Subsección 1: Distribución de la Producción por ODS ---
sec_one_title = "Distribución de la Producción por ODS"
sec_one_text1 = "El análisis de la producción científica del ICN revela una contribución significativa a varios de los 17 Objetivos de Desarrollo Sostenible (ODS) de la ONU. La metodología de mapeo asigna cada documento a los ODS relevantes a través de palabras clave y clasificación temática. La Fig. 19 muestra la distribución de documentos vinculados, destacando que los ODS más representados son: ODS 7 (Energía asequible y no contaminante), ODS 9 (Industria, Innovación e Infraestructura) y ODS 13 (Acción por el clima). Estos tres ODS concentran más del 50% de las contribuciones ODS del ICN."
image_one_path = "assets/images/sec_5_img_1.png"
image_one_caption = "Fig. 19. Documentos por ODS (Top 10 Contribuciones)"

# --- Subsección 2: Evolución Anual de la Contribución ODS ---
sec_two_title = "Evolución Anual de la Contribución ODS"
sec_two_text1 = "La vinculación de la investigación a los ODS ha mostrado un crecimiento constante y acelerado en los últimos cinco años (Fig. 20). Este aumento refleja una mayor orientación temática hacia problemas globales y una posible conciencia institucional sobre la relevancia de estos objetivos. El pico de crecimiento se observa en 2023, coincidiendo con iniciativas de la UNAM para promover la investigación orientada a la sostenibilidad."
image_two_path = "assets/images/sec_5_img_2.png"
image_two_caption = "Fig. 20. Porcentaje de documentos anuales vinculados a ODS"

# --- Subsección 3: Impacto Geográfico de la Colaboración ODS ---
sec_three_title = "Impacto Geográfico de la Colaboración ODS"
sec_three_text1 = "La colaboración internacional en temas de ODS se concentra fuertemente en países desarrollados, pero también incluye enlaces vitales con economías en desarrollo. La Fig. 21 muestra el mapa de colaboración internacional, donde se observa que los proyectos ODS tienen mayor colaboración con socios en Europa y Norteamérica. Sin embargo, los proyectos de mayor impacto en ODS específicos (como ODS 2, Hambre Cero, o ODS 6, Agua Limpia) tienden a involucrar a países latinoamericanos con problemáticas similares, lo que potencia el impacto regional."
image_three_path = "assets/images/sec_5_img_3.png"
image_three_caption = "Fig. 21. Mapa de colaboración internacional en investigaciones ODS"

sec_three_text2 = "El ICN demuestra ser un actor clave en la investigación orientada a la sostenibilidad, con potencial para ampliar su impacto a ODS menos representados actualmente."


# --- Secciones del Informe (para el menú final) ---
sec_nav_title1 = "Evolución del Volumen de la Producción Científica"
sec_nav_title2 = "Impacto de la Producción Científica"
sec_nav_title3 = "Análisis de la Colaboración"
sec_nav_title4 = "Caracterización Temática de la Producción Científica"


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
st.header("Indicadores ODS Clave")
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric("Documentos Vinculados", "42%", help="Porcentaje de la producción total con vinculación ODS.")
with metric_col2:
    st.metric("ODS Más Representados", "ODS 7, 9, 13", delta="Concentran el 50%")
with metric_col3:
    st.metric("Crecimiento Anual (2023)", "↑ 18%", help="Incremento en el porcentaje de publicaciones ODS respecto al año anterior.")
with metric_col4:
    st.metric("ODS de Mayor Potencial", "ODS 14 (Vida Submarina)", delta_color="off", delta="Necesita mayor foco")

st.markdown("---")


# --- Bloque Principal con Pestañas (Tabs) ---
tab1, tab2, tab3 = st.tabs([f"1. {sec_one_title}", f"2. {sec_two_title}", f"3. {sec_three_title}"])

# =========================================================================
# PESTAÑA 1: DISTRIBUCIÓN POR ODS
# =========================================================================
with tab1:
    st.subheader(sec_one_title)

    # Fila 1: Texto y Fig. 19 (Distribución ODS)
    col1, col2 = st.columns([0.6, 1.4])
    with col1:
        st.markdown(sec_one_text1)
        st.info("La fuerte concentración en ODS 7, 9 y 13 es un reflejo de las líneas de investigación en Física de Materiales, Astrofísica y Energía. ")
    with col2:
        display_image(image_one_path, image_one_caption)


# =========================================================================
# PESTAÑA 2: EVOLUCIÓN ANUAL
# =========================================================================
with tab2:
    st.subheader(sec_two_title)

    # Fila 1: Fig. 20 (Evolución Temporal)
    col1, col2 = st.columns([1.5, 0.5])
    with col1:
        display_image(image_two_path, image_two_caption)
    with col2:
        st.markdown(sec_two_text1)
        st.success("La tendencia positiva indica una alineación creciente entre la investigación del ICN y los desafíos de sostenibilidad global.")


# =========================================================================
# PESTAÑA 3: IMPACTO GEOGRÁFICO
# =========================================================================
with tab3:
    st.subheader(sec_three_title)

    # Fila 1: Texto y Fig. 21 (Mapa de Colaboración ODS)
    col1, col2 = st.columns([0.6, 1.4])
    with col1:
        st.markdown(sec_three_text1)
        st.markdown(sec_three_text2)
    with col2:
        display_image(image_three_path, image_three_caption)

    st.markdown("---")
    st.caption("La colaboración en ODS con países de la región es clave para traducir la ciencia básica en soluciones aplicables a contextos locales.")
