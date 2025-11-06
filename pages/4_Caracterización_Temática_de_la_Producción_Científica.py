#SECCION 4

import streamlit as st
import os

st.set_page_config(
    page_title="Reporte Cienciométrico - Sección 4",
    layout="wide",
    initial_sidebar_state="collapsed"
)

main_title = "Caracterización Temática de la Producción Científica"

# --- Subsección 1
sec_one_title = "Categorías Temáticas"
image_one_path = "assets/images/sec_4_img_1.png" 
image_one_caption = "50 primeras categorías temáticas de acuerdo al número de artículos, periodo: 1980-2024"
image_two_path = "assets/images/sec_4_img_2.png" #Sin caption en el informe original, se deja en blanco
image_three_path = "assets/images/sec_4_img_3.png"
image_three_caption = "50 primeras categorías temáticas de acuerdo al número de artículos, periodo: 2020-2024"

# --- Subsección 2-
sec_two_title = "Evolución de los Temas de Investigación"
image_four_path = "assets/images/sec_4_img_4.png" #Sin caption en el original
image_five_path = "assets/images/sec_4_img_5.png"
image_five_caption = "Evolución del Core temático"
image_six_path = "assets/images/sec_4_img_6.png"
image_six_caption = "Evolución del perfil temático (core)"
image_seven_path = "assets/images/sec_4_img_7.png" #Sin caption en el original

# --- Subsección 3
sec_three_title = "Caracterización Temática: Micro y Meso Tópicos"
sec_three_text1 = '''Las gráficas muestran cómo ha evolucionado, durante el periodo 1980-2024, la producción científica del Instituto y su impacto, a través de la nueva ontología de WoS: Citation Topics. Esta Ontología, a diferencia de las anteriores de WoS, permite etiquetar a los artículos de manera única haciendo uso de la Inteligencia Artificial y un algoritmo de detección de comunidades en la red compleja de citas. La ontología está organizada de manera jerárquica en 3 niveles: Macro (10), Meso (326) y Micro tópicos (2449).'''
sec_three_text2 = '''En el eje de las X están todos los años del período de estudio (la evolución desde 1980 a 2024). En el eje vertical se listan los 326 meso tópicos organizados dentro del macro tópico correspondiente diferenciado por los distintos colores.'''
sec_three_text3 = '''
1. Ciencias clínicas y biológicas
2. Química
3. Agricultura, Medio Ambiente y Ecología
4. Ingeniería Eléctrica, Electrónica y Ciencias de la Computación
5. Física
6. Ciencias Sociales
7. Ingeniería y ciencia de los materiales
8. Ciencias de la Tierra
9. Matemáticas
10. Artes y Humanidades
'''
sec_three_text4 = "Cada celda del Heatmap múltiple refleja la incidencia normalizada a nivel de micro tópico de la ciencia que se produce (izquierda) y su impacto (derecha). En las imágenes se puede apreciar que, desde el punto de vista de su producción, el Instituto es relativamente disciplinar (Física y Química). En las demás áreas hay aportes pero en su mayoría muy vinculados a aplicaciones de esas dos disciplinas. En particular, se ha comenzando a ver que en los últimos años aparecen más aportes en áreas de la salud y ciencias de la vida."
sec_three_text5 = "En cambio, desde el punto de vista del impacto, la cobertura interdisciplinar sí es mayor. Áreas como las Matemáticas (en particular los Sistemas dinámicos y las Estadísticas Aplicadas) han sido impactadas desde hace mucho. El resto de las disciplinas a partir de finales de los 90s e inicios de los 2000s, con tendencia a un mayor impacto en décadas recientes. Sólo las “Artes y Humanidades” son impactadas de manera tardía a partir de 2010 y no es tan abundante el impacto."
image_eight_path = "assets/images/sec_4_img_8.png"
image_eight_caption = '''Producción ([detalles](https://sigi.nucleares.unam.mx/sgiicn/userfiles/files/evolution/icn2_2_adn_evolution.html)) e Impacto ([detalles](https://sigi.nucleares.unam.mx/sgiicn/userfiles/files/evolution/icn2_2_evolution.html))'''
image_nine_path = "assets/images/sec_4_img_9.png"
image_nine_caption = "Periodo 1980-2024"

# Para mostrar imágenes con caption y manejo de error.
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
    

#PESTAÑAS
tab1, tab2, tab3 = st.tabs([f"Categorías Temáticas", f"Evolución Temática", f"Caracterización Temática"])

# =========================================================================
# PESTAÑA 1
# =========================================================================
with tab1:
    col1_1, col1_2 = st.columns(2)

    with col1_1:
        st.subheader("Periodo 1980-2024 (Artículos)")
        display_image(image_one_path, image_one_caption)

    with col1_2:
        st.subheader("Periodo 2020-2024 (Artículos)")
        display_image(image_two_path, " ")
        display_image(image_three_path, image_three_caption)

st.divider()

# =========================================================================
# PESTAÑA 2
# =========================================================================
with tab2:
    st.subheader("Evolución del Perfil Temático (Core)")

    col2_1, col2_2 = st.columns(2)
    with col2_1:
        display_image(image_five_path, image_five_caption) # Evolución del Core temático
    with col2_2:
        display_image(image_six_path, image_six_caption) # Evolución del perfil temático (core)

    st.subheader("Gráficos Adicionales de Evolución")
    col2_3, col2_4 = st.columns(2)
    with col2_3:
        display_image(image_four_path, "Gráfico de evolución de categorías 1")
    with col2_4:
        display_image(image_seven_path, "Gráfico de evolución de categorías 2")

    st.divider()

# =========================================================================
# PESTAÑA 3
# =========================================================================
with tab3:
    st.subheader(sec_three_title)
    st.markdown(sec_three_text1)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(sec_three_text2)
        st.info(sec_three_text3)
    with col2:
        display_image(image_eight_path, image_eight_caption)

    st.markdown(sec_three_text4)
    st.markdown(sec_three_text5)    
    display_image(image_nine_path, image_nine_caption)

