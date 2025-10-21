#SECCION 2

import streamlit as st
import os

# --- Configuración de la Página (Título, Ícono, Layout) ---
st.set_page_config(
    page_title="Reporte Cienciométrico - Sección 2",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Definimos las variables de texto e imágenes (Adaptadas del Notebook)
main_title = "Impacto de la Producción Científica"

# --- Subsección 1: Citas y Factor H ---
sec_one_title = "Análisis de las Citas y el Factor H"
sec_one_text1 = "El índice H (o factor H) fue propuesto por Jorge Hirsch en 2005 para cuantificar la calidad de las investigaciones de un científico. El índice h se define como el número de artículos h que han recibido por lo menos h citas. El índice H del ICN se calcula considerando los documentos del ICN indexados en el Web of Science (WoS) en el periodo 1968-2024. El valor de H para la producción científica del ICN es de 97. Este valor indica que 97 documentos han sido citados al menos 97 veces.  Al igual que se hizo con el análisis de producción, este valor se ajusta considerando solo artículos y reviews, excluyendo las grandes colaboraciones. El índice H ajustado es de 86. Estos valores son altos para una institución dedicada a la investigación básica en el área de la física."

# --- Subsección 2: Citas por Documento ---
sec_two_title = "Citas por Documento"
sec_two_text1 = "El promedio de citas por documento (CPD) es un indicador de impacto. En la Fig. 8 se muestra la CPD por año, para toda la producción científica del ICN. Se observa que el valor de CPD por año varía entre 0 y 45. El mayor impacto en el periodo evaluado (1968-2024) se obtuvo en el año 1989, con un valor de 45.92. Este alto impacto se debe principalmente al artículo 'The geometry of the general-relativistic 2-body problem' de S. D'Eath y R. E. K. S. E. K. S. J. (498 citas)."
image_one_path = "assets/images/sec_2_img_1.png"
image_one_caption = "Fig. 8. Promedio de citas por documento por año. ICN en el Web of Science, 1968-2024"

sec_two_text2 = "En la Fig. 9 se observa la CPD por año excluyendo las grandes colaboraciones. Se puede apreciar que la variación entre años es menor, al igual que los valores extremos, oscilando entre 0 y 38. Los años con mayor impacto siguen siendo 1989 (38.82 citas por documento), 1990 (38.16 citas por documento), y 1987 (37.14 citas por documento)."
image_two_path = "assets/images/sec_2_img_2.png"
image_two_caption = "Fig. 9. Promedio de citas por documento por año, excluyendo grandes colaboraciones. ICN en el Web of Science, 1968-2024"

# --- Subsección 3: Distribución de Citas y Citas por Investigador ---
sec_three_title = "Distribución de Citas y Rendimiento de Impacto"
sec_three_text1 = "La distribución de las citas es muy asimétrica. Un pequeño número de artículos acumula una gran parte de las citas. La Fig. 10 muestra esta distribución, donde se observa que el 80% de las citas (75,650) están concentradas en el 20% de los documentos (1,230 artículos)."
image_three_path = "assets/images/sec_2_img_3.png"
image_three_caption = "Fig. 10. Distribución acumulada de citas para la producción científica del ICN"

sec_three_text2 = "Considerando el número de académicos a tiempo completo, se puede calcular la CPD por investigador. En la Fig. 11 y Fig. 12 se muestra la CPD por investigador con y sin grandes colaboraciones respectivamente. Se observa una tendencia general al alza, lo que indica que el impacto del ICN se ha incrementado en los últimos años."
image_four_path = "assets/images/sec_2_img_4.png"
image_four_caption = "Fig. 11. Promedio de citas por documento por investigador, 1996-2024"
image_five_path = "assets/images/sec_2_img_5.png"
image_five_caption = "Fig. 12. Promedio de citas por documento por investigador, excluyendo grandes colaboraciones, 1996-2024"


# --- Secciones del Informe (para el menú final - Se mantienen las mismas referencias) ---
sec_five_title1 = "Evolución del Volumen de la Producción Científica"
sec_five_title3 = "Análisis de la Colaboración"
sec_five_title4 = "Caracterización Temática de la Producción Científica"
sec_five_title5 = "Contribución a los Objetivos de Desarrollo Sostenible (ODS)"


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
st.header("Indicadores de Impacto Clave")
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric("Índice H (Global)", "97")
with metric_col2:
    st.metric("Índice H (Ajustado)", "86", help="Excluyendo grandes colaboraciones")
with metric_col3:
    st.metric("Promedio Citas / Documento", "22.14", delta="Valor anterior: 18.03") # Se usa el valor de la Secc 1 como referencia
with metric_col4:
    st.metric("Total de Citas Acumuladas", "94,563")

st.markdown("---")


# --- Bloque Principal con Pestañas (Tabs) ---
tab1, tab2, tab3 = st.tabs([f"1. {sec_one_title}", f"2. {sec_two_title}", f"3. {sec_three_title}"])

# =========================================================================
# PESTAÑA 1: CITAS Y FACTOR H
# =========================================================================
with tab1:
    st.subheader("Cuantificación de la Calidad y Producción")
    st.markdown(sec_one_text1)

    st.markdown(
        """
        El valor de **H=97 (Global)** y **H=86 (Ajustado)** sugiere una alta productividad de artículos bien citados a lo largo del periodo, lo que es un indicador de la solidez en investigación básica.
        """
    )


# =========================================================================
# PESTAÑA 2: CITAS POR DOCUMENTO (CPD)
# =========================================================================
with tab2:
    st.subheader("CPD por Año: Análisis de Impacto Temporal")

    # Fila 1: Fig. 8 (Global)
    col1, col2 = st.columns([1.5, 0.5])
    with col1:
        display_image(image_one_path, image_one_caption)
    with col2:
        st.markdown(sec_two_text1)
        st.info("El pico de 1989 (45.92 CPD) se debe a un artículo altamente citado sobre la relatividad general.")

    st.markdown("---")

    # Fila 2: Fig. 9 (Ajustado)
    col3, col4 = st.columns([0.5, 1.5])
    with col3:
        st.markdown(sec_two_text2)
        st.info("Al excluir las grandes colaboraciones, la variación anual del CPD se suaviza, mostrando valores máximos más consistentes alrededor de los años 80 y 90.")
    with col4:
        display_image(image_two_path, image_two_caption)


# =========================================================================
# PESTAÑA 3: DISTRIBUCIÓN DE CITAS Y RENDIMIENTO DE IMPACTO
# =========================================================================
with tab3:
    st.subheader("Concentración de Citas (Principio de Pareto)")

    # Fila 1: Fig. 10 (Distribución Asimétrica)
    col1, col2 = st.columns([0.8, 1.2])
    with col1:
        st.markdown(sec_three_text1)
        st.warning("La concentración del 80% de las citas en el 20% de los documentos es un fenómeno común en la literatura científica (Ley de Lotka o principio de Pareto).")
    with col2:
        display_image(image_three_path, image_three_caption)

    st.markdown("---")
    st.subheader("CPD Ajustado por Investigador")

    st.markdown(sec_three_text2)

    # Fila 2: Fig. 11 y Fig. 12 (CPD por Investigador)
    col3, col4 = st.columns(2)
    with col3:
        display_image(image_four_path, image_four_caption)
    with col4:
        display_image(image_five_path, image_five_caption)
