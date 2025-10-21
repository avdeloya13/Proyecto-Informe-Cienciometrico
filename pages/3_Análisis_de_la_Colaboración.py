#SECCION 3

import streamlit as st
import os

# --- Configuración de la Página (Título, Ícono, Layout) ---
st.set_page_config(
    page_title="Reporte Cienciométrico - Sección 3",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Definimos las variables de texto e imágenes (Adaptadas del Notebook)
main_title = "Análisis de la Colaboración"

# --- Subsección 1: Colaboración en el ICN ---
sec_one_title = "Colaboración en el ICN"
sec_one_text1 = "La colaboración es una característica importante de la producción científica del ICN. La colaboración se puede medir por el número de autores por documento y la participación internacional. El número de autores por documento ha aumentado en los últimos años, con una media de 102 autores por documento para toda la colección. Este valor está sesgado por la presencia de grandes colaboraciones. Al excluir las grandes colaboraciones, el número de autores por documento es de 4.01. [Image of collaboration diagram]. El ICN es una institución que promueve la colaboración. En la Fig. 13 se muestra el diagrama de colaboración de los autores del ICN, donde se observa un núcleo de autores altamente conectados."
image_one_path = "assets/images/sec_3_img_1.png"
image_one_caption = "Fig. 13. Colaboración entre autores del ICN"

# --- Subsección 2: Coautoría Internacional ---
sec_two_title = "Coautoría Internacional"
sec_two_text1 = "La coautoría internacional es del 56.17% para toda la producción, lo que es un indicador de la proyección internacional del ICN. En la Fig. 14 se muestra la coautoría internacional por año. Se observa una tendencia general al alza, con un valor promedio de 56.17% en todo el periodo. El valor máximo se alcanza en el año 2024 (78.38%), lo que indica un aumento en la colaboración internacional en los últimos años. Este comportamiento es positivo para la institución, ya que la colaboración internacional promueve el impacto de la producción científica."
image_two_path = "assets/images/sec_3_img_2.png"
image_two_caption = "Fig. 14. Coautoría internacional por año (porcentaje de artículos con al menos un autor extranjero)"

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


# --- Bloque Principal con Pestañas (Tabs) ---
tab1, tab2, tab3 = st.tabs([f"1. {sec_one_title}", f"2. {sec_two_title}", f"3. {sec_three_title}"])

# =========================================================================
# PESTAÑA 1: COLABORACIÓN EN EL ICN
# =========================================================================
with tab1:
    st.subheader(sec_one_title)

    # Fila 1: Texto y Fig. 13 (Diagrama de Colaboración)
    col1, col2 = st.columns([0.6, 1.4])
    with col1:
        st.markdown(sec_one_text1)
        st.info("El alto promedio de 102 autores por documento en la colección global se debe a las 'grandes colaboraciones'. El valor ajustado de 4.01 es más representativo de la colaboración interna.")
    with col2:
        display_image(image_one_path, image_one_caption)


# =========================================================================
# PESTAÑA 2: COAUTORÍA INTERNACIONAL
# =========================================================================
with tab2:
    st.subheader(sec_two_title)

    # Fila 1: Fig. 14 (Coautoría Internacional por año)
    col1, col2 = st.columns([1.5, 0.5])
    with col1:
        display_image(image_two_path, image_two_caption)
    with col2:
        st.markdown(sec_two_text1)
        st.success(f"La tendencia al alza es un indicador positivo, alcanzando un pico de **78.38% en 2024**.")


# =========================================================================
# PESTAÑA 3: DISTRIBUCIÓN DE LA COLABORACIÓN INTERNACIONAL
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
