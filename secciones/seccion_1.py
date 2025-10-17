#"Sección 1: Evolución del Volumen de la Producción Científica".

import streamlit as st
import os

# --- Configuración de la Página (Título, Ícono, Layout) ---
st.set_page_config(
    page_title="Reporte Cienciométrico - Sección 1",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Definimos las variables de texto e imágenes (sin cambios)
main_title = "Evolución del Volumen de la Producción Científica"

# --- Sección 1: Descripción General ---
sec_one_title = "Descripción General"
sec_one_text1 = "Se recuperaron un total de 6153 documentos, publicados desde 1968 hasta el 2024. Todos los documentos fueron exportados a R haciendo uso del paquete Biblioemtrix. De este total, 66 no fueron recuperados desde Incites por corresponder a documentos publicados antes de 1980."
sec_one_text2 = "Una descripción general de los documentos se observa en la Fig.1. La colección muestra una producción científica creciente (tasa anual de 8.88%) y altamente colaborativa, con una importante participación internacional (56%) y un nivel considerable de citación promedio por artículo (22.14). La alta cantidad de autores y referencias indica una red científica activa y extensa. Se publica en 707 fuentes diferentes."
image_one_path = "assets/images/sec_1_img_1.png"
image_one_caption = "Fig. 1. Producción científica del ICN en el Web of Science, 1968-2024"

sec_one_text3 = "De los 6153 documentos 4695 están clasificados como artículos y 88 como reviews. Además, 1077 corresponden a publicaciones de grupos de autores según la clasificación del WoS o tienen más de 20 autores. En total la producción del ICN conformada por artículos o reviews que no corresponden a grandes colaboraciones es de 3 909 documentos (Fig. 2). En este subconjunto, la tasa de crecimiento anual es de 7.96% y una media de 4.01 coautores por artículo, lo que contrasta con el valor anterior de 102 coautores por documento, asociado a colaboraciones masivas. La proporción de coautoría internacional se mantiene alta (52.49% frente al 56.17% global), y se observa un promedio de 18.03 citas por documento, ligeramente inferior al promedio general (22.14)."
sec_one_text4 = "En cuanto al impacto y la actividad investigadora, el ICN muestra una sólida trayectoria con una edad promedio de publicación de 14.4 años y un total de 94,563 referencias citadas. Los datos destacan la contribución del ICN sin el sesgo de grandes colaboraciones al mostrar un promedio de 18 citas por documento."
image_two_path = "assets/images/sec_1_img_2.png"
image_two_caption = "Fig. 2. Producción científica del ICN en el Web of Science, considerando sólo artículos y reviews y excluyendo grandes colaboraciones. 1968-2024"

# --- Sección 2: Producción Anual ---
sec_two_title = "Producción Anual"
sec_two_text1 = "La producción científica del ICN creció de 2 artículos en 1968, hasta llegar a más de 200 documentos por año en la actualidad (Fig. 3)."
sec_two_text2 = "En el año 2002 se observa un pico en la gráfica, al evaluar detenidamente la producción de este año se observa que un posdoctorante (Dong, SH) asociado al ICN ese año publicó 19 artículos. Además, otros investigadores estuvieron por encima de la media como Raga, AC (9 artículos), Frank, A (8 artículos), Guven J (7 artículos) y Hirsch, JG (6 artículos)."
image_three_path = "assets/images/sec_1_img_3.png"
image_three_caption = "Fig. 3. Evolución de la producción científica del ICN en el Web of Science, 1968-2024"

sec_two_text3 = "El número de académicos a tiempo completo asociado al ICN ha aumentado desde su fundación como entidad académica hasta la actualidad. En los últimos años, este número ha mostrado cierta estabilidad. En las Fig. 4 y 5 se muestra la producción ajustada por el número de investigadores asociados a la institución en el periodo de 1996-2024, con y sin grandes colaboraciones respectivamente. Se observa una tendencia al crecimiento. Este crecimiento pudiera asociarse no solo al crecimiento de la actividad institucional, sino también a la propia cobertura de las bases de datos, dado el aumento de la cobertura del WoS durante los últimos años."
image_four_path = "assets/images/sec_1_img_4.png"
image_four_caption = "Fig. 4. Total de documentos publicados, por investigador, 1996-2024"
image_five_path = "assets/images/sec_1_img_5.png"
image_five_caption = "Fig. 5. Total de artículos, sin considerar grandes colaboraciones, publicados por investigador, 1996-2024"

# --- Sección 3: Producción en Revistas JCR ---
sec_three_title = "Producción en Revistas con Factor de Impacto (Revistas JCR)"
sec_three_text1 = "La comunidad del ICN publica artículos científicos en más de 500 revistas. En la Fig. 6 se listan las 20 revistas donde más se publica."
image_six_path = "assets/images/sec_1_img_6.png"
image_six_caption = "Fig. 6. Top 20 revistas donde más publica el ICN"

sec_three_text2 = "Las 20 revistas se distribuyen de acuerdo al cuartil como: 8 en Q1, 7 en Q2, 4 en Q3 y 1 en Q4. Si se analizan las 20 fuentes principales donde se ha publicado en los últimos 10 años, se mantienen 14 revistas. En la tabla 1 se muestra la distribución de acuerdo al número de artículos y el cuartil."
image_seven_path = "assets/images/sec_1_img_7.png"
image_seven_caption = "Tabla 1. Top 20 revistas donde más se publica"

sec_three_text3 = "La Fig. 7 muestra la aplicación de la Ley de Bradford a las publicaciones científicas del ICN en todo el periodo. En el eje X (log-rank) se representan las revistas ordenadas de mayor a menor número de artículos sobre el tema de estudio y en el eje Y se muestra la cantidad de artículos publicados en cada revista. El área sombreada indica las revistas nucleares o fuentes principales, donde se publica la mayor parte de la producción científica del ICN (10 revistas). La forma de la curva confirma la dispersión de la literatura científica, con un pequeño grupo de revistas publicando la mayor parte de los artículos. La presencia de un gran número de revistas en la zona 3 indica una dispersión de publicaciones en múltiples fuentes."
image_eight_path = "assets/images/sec_1_img_8.png"
image_eight_caption = "Fig. 7. Ley de Bradford de las publicaciones científicas del ICN en todo el periodo"

# --- Secciones del Informe (para el menú final) ---
sec_five_title2 = "Impacto de la Producción Científica"
sec_five_title3 = "Análisis de la Colaboración"
sec_five_title4 = "Caracterización Temática de la Producción Científica"
sec_five_title5 = "Contribución a los Objetivos de Desarrollo Sostenible (ODS)"

# Función auxiliar para mostrar imágenes con caption y manejo de error.
def display_image(path, caption):
    """Muestra la imagen con un caption centrado."""
    if not os.path.exists(path):
        st.warning(f"⚠️ Imagen no encontrada en: {path}. Asegúrate de que el directorio 'assets/images/' exista y contenga las imágenes.")
        st.info(f"Placeholder para: {caption}")
        st.image("https://placehold.co/600x460/cccccc/333333?text=IMAGEN+FALTANTE", caption=caption, use_column_width="auto")
    else:
        st.image(path, caption=caption, use_column_width="auto")

# ----------------------------------------------------
# APLICACIÓN PRINCIPAL (DISEÑO MEJORADO)
# ----------------------------------------------------

st.title(main_title)
st.markdown("---")


# --- Bloque de Métricas Resumen ---
st.header("Resumen Ejecutivo")
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric("Documentos Totales", "6,153", delta="Publicados hasta 2024")
with metric_col2:
    st.metric("Citas Promedio (Global)", "22.14", delta_color="inverse")
with metric_col3:
    st.metric("Tasa de Crecimiento Anual", "8.88%", delta="Alta")
with metric_col4:
    st.metric("Colaboración Internacional", "56%", delta="Sólida")

st.markdown("---")

# --- Bloque Principal con Pestañas (Tabs) ---
tab1, tab2, tab3 = st.tabs([f"1. {sec_one_title}", f"2. {sec_two_title}", f"3. {sec_three_title}"])

# =========================================================================
# PESTAÑA 1: DESCRIPCIÓN GENERAL
# =========================================================================
with tab1:
    st.subheader("Análisis de la Colección Global vs. Sin Grandes Colaboraciones")

    # Fila 1: Descripción Inicial y Fig. 1
    col1, col2 = st.columns([0.6, 1.4])
    with col1:
        st.markdown(f"**{sec_one_text1}**")
        st.markdown(sec_one_text2)
    with col2:
        display_image(image_one_path, image_one_caption)

    st.markdown("---")

    # Fila 2: Análisis Detallado (Texto y Fig. 2)
    col3, col4 = st.columns([1.4, 0.6])
    with col3:
        st.markdown("### Colección Principal (Artículos y Reviews, Sin Grandes Colaboraciones)")
        st.markdown(sec_one_text3)
        st.markdown(sec_one_text4)
    with col4:
        display_image(image_two_path, image_two_caption)


# =========================================================================
# PESTAÑA 2: PRODUCCIÓN ANUAL
# =========================================================================
with tab2:
    st.subheader("Evolución de la Productividad a lo largo del tiempo")

    # Fila 1: Fig. 3 (Evolución) y explicación del pico
    col1, col2 = st.columns([1.4, 0.6])
    with col1:
        display_image(image_three_path, image_three_caption)
    with col2:
        st.markdown(sec_two_text1)
        st.markdown(f"**Nota sobre el pico de 2002:**")
        st.info(sec_two_text2)

    st.markdown("---")
    st.subheader("Producción Ajustada por Investigador")
    st.markdown(sec_two_text3)

    # Fila 2: Fig. 4 y Fig. 5 (Producción por Investigador)
    col3, col4 = st.columns(2)
    with col3:
        display_image(image_four_path, image_four_caption)
    with col4:
        display_image(image_five_path, image_five_caption)


# =========================================================================
# PESTAÑA 3: PRODUCCIÓN EN REVISTAS JCR
# =========================================================================
with tab3:
    st.subheader("Análisis de las Fuentes de Publicación")

    # Fila 1: Texto de Revistas y Fig. 6 (Top 20 Revistas)
    col1, col2 = st.columns([0.6, 1.4])
    with col1:
        st.markdown(sec_three_text1)
        st.markdown(sec_three_text2)
    with col2:
        display_image(image_six_path, image_six_caption)

    st.markdown("---")
    st.subheader("Distribución por Cuartil y Ley de Bradford")

    # Fila 2: Fig. 7 (Ley de Bradford) y Tabla 1
    col3, col4 = st.columns([1, 1])
    with col3:
        st.markdown(sec_three_text3)
        display_image(image_eight_path, image_eight_caption)
    with col4:
        # Se pone la Tabla 1 al lado del texto para mejor comparación
        st.markdown("### Tabla de Distribución (Referencia)")
        display_image(image_seven_path, image_seven_caption)

# ----------------------------------------------------
# MENÚ DE NAVEGACIÓN (Simulando el final del notebook)
# ----------------------------------------------------

st.markdown("""
---
## 📄 Navegación Rápida a Otras Secciones
""")

# Creamos una cuadrícula para simular las "cards" de navegación
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

# Usamos st.page_link para simular el acceso a las otras secciones (requiere que los archivos existan)
# NOTA: st.page_link solo funciona si se ejecuta con 'streamlit run' en modo multipágina
with nav_col1:
    st.markdown(f"**{sec_five_title2}**")
    st.page_link("seccion_2.py", label="Ir a Sección 2", icon="📈")

with nav_col2:
    st.markdown(f"**{sec_five_title3}**")
    st.page_link("seccion_3.py", label="Ir a Sección 3", icon="🤝")

with nav_col3:
    st.markdown(f"**{sec_five_title4}**")
    st.page_link("seccion_4.py", label="Ir a Sección 4", icon="📚")

with nav_col4:
    st.markdown(f"**{sec_five_title5}**")
    st.page_link("seccion_5.py", label="Ir a Sección 5", icon="🌍")

st.markdown("---")
st.caption("Footer: © ICN Reportes Cienciométricos. Contacto: [Email] | Síguenos en Redes Sociales.")
