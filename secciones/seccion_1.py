#"Sección 1: Evolución del Volumen de la Producción Científica".

import streamlit as st
import os

# --- Configuración de la Página (Título, Ícono, Layout) ---
st.set_page_config(
    page_title="Reporte Cienciométrico - Sección 1",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Definimos las variables de texto e imágenes que estaban en el notebook
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
        st.image("https://placehold.co/600x460/cccccc/333333?text=IMAGEN+FALTANTE", caption=caption, use_container_width="auto")
    else:
        st.image(path, caption=caption, use_container_width="auto")

# ----------------------------------------------------
# APLICACIÓN PRINCIPAL
# ----------------------------------------------------

st.title(main_title)
st.markdown("---")


# SECCIÓN 1: Descripción General
st.header(f"1. {sec_one_title}")

# Layout para la primera sección
col1_1, col1_2 = st.columns([1, 1])

with st.container():
    st.markdown(f"**{sec_one_text1}**")

    # Fila 2: Texto y Fig. 1
    col2_1, col2_2 = st.columns([1, 1])
    with col2_1:
        st.markdown(sec_one_text2)
    with col2_2:
        display_image(image_one_path, image_one_caption)

    # Fila 3: Fig. 2 y Texto (Nota: Invertimos el orden para coincidir con la apariencia del notebook si es posible)
    col3_1, col3_2 = st.columns([1, 1])
    with col3_1:
        # Se incluye el margen superior para replicar la alineación visual del notebook
        st.markdown(
            f"""
            <style>
            .margin-top-90 {{
                margin-top: 50px; /* Ajuste para espacio visual */
            }}
            </style>
            <div class="margin-top-90">
            {display_image(image_two_path, image_two_caption)}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3_2:
        st.markdown(sec_one_text3.replace('<br />', '\n\n')) # Reemplazar <br /> por doble salto de línea en Markdown

    # Fila 4: Texto final
    st.markdown(sec_one_text4)

st.markdown("---")

# SECCIÓN 2: Producción Anual
st.header(f"2. {sec_two_title}")

# Layout para la segunda sección
col4_1, col4_2 = st.columns([1, 1])
with col4_1:
    # Simula el margen superior de la imagen
    st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
    display_image(image_three_path, image_three_caption)

with col4_2:
    st.markdown(sec_two_text1)
    st.markdown(sec_two_text2)

# Fila 5: Texto y Fig. 4
col5_1, col5_2 = st.columns([1, 1])
with col5_1:
    st.markdown(sec_two_text3.replace('<br />', '\n\n'))
with col5_2:
    display_image(image_four_path, image_four_caption)

# Fila 6: Fig. 5 (centrada/ancho completo)
st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
st.markdown("---")
display_image(image_five_path, image_five_caption)


# SECCIÓN 3: Producción en Revistas JCR
st.header(f"3. {sec_three_title}")

# Layout para la tercera sección
col6_1, col6_2 = st.columns([1, 1.4])
with col6_1:
    st.markdown(sec_three_text1)

with col6_2:
    display_image(image_six_path, image_six_caption)

# Fila 8: Tabla 1 y Texto
col7_1, col7_2 = st.columns([1, 1.4])
with col7_1:
    display_image(image_seven_path, image_seven_caption)
with col7_2:
    st.markdown(sec_three_text2)

# Fila 9: Ley de Bradford (Texto y Fig. 7)
col8_1, col8_2 = st.columns([1, 1])
with col8_1:
    st.markdown(sec_three_text3.replace('<br />', '\n\n'))
with col8_2:
    display_image(image_eight_path, image_eight_caption)

# ----------------------------------------------------
# MENÚ DE NAVEGACIÓN (Simulando el final del notebook)
# ----------------------------------------------------

st.markdown("""
---
## Navegación
Selecciona la sección del reporte a la que deseas ir:
""")

# Creamos una cuadrícula para simular las "cards" de navegación
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

# Usamos st.page_link para simular el acceso a las otras secciones (requiere que los archivos existan)
with nav_col1:
    st.subheader(sec_five_title2)
    st.page_link("seccion_2.py", label="Ir a Sección 2", icon="📈")

with nav_col2:
    st.subheader(sec_five_title3)
    st.page_link("seccion_3.py", label="Ir a Sección 3", icon="🤝")

with nav_col3:
    st.subheader(sec_five_title4)
    st.page_link("seccion_4.py", label="Ir a Sección 4", icon="📚")

with nav_col4:
    st.subheader(sec_five_title5)
    st.page_link("seccion_5.py", label="Ir a Sección 5", icon="🌍")

st.markdown("---")
st.caption("Footer: © ICN Reportes Cienciométricos. Contacto: [Email] | Síguenos en Redes Sociales.")