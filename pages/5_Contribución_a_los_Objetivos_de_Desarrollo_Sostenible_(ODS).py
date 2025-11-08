#SECCION 5

import streamlit as st
import os

st.set_page_config(
    page_title="Reporte Cienciométrico - Sección 5",
    layout="wide",
    initial_sidebar_state="collapsed"
)

main_title = "Contribución a los Objetivos de Desarrollo Sostenible (ODS)"

# --- Subsección 1
sec_one_title = "Patentes"
sec_one_text1 = "Citations From Patents (Citas Provenientes de Patentes): Los artículos que corresponden a GC han recibido 125 citas de patentes en todo el periodo, pero ninguna en el periodo 2020-2024. Los artículos sin GC registran 106 citas de patentes en todo el periodo, y tampoco ninguna en el periodo reciente."
sec_one_text2 = "De acuerdo con datos registrados en SIGI y corroborados en Lens.org se identificaron 7 patentes registradas pertenecientes a dos familias de patentes con autoría de investigadores del ICN."
image_one_path = "assets/images/sec_5_img_1.png"
image_one_caption = "Citas desde patentes a la producción científica del ICN"
image_two_path = "assets/images/sec_5_img_2.png"
image_two_caption = " "
sec_one_text3 = "De acuerdo con el sistema de clasificación CPC (Cooperative Patent Classification) desarrollado por la Oficina Europea de Patentes (EPO) y la Oficina de Patentes de EE.UU. (USPTO), donde cada código representa un área técnica o tecnológica específica, las patentes analizadas se clasifican en Necesidades Humanas y Química Metalúrgica."
image_three_path = "assets/images/sec_5_img_3.png"
image_three_caption = " "

# --- Subsección 2
sec_two_title = '''Objetivos de Desarrollo Sostenible (ODS)'''
sec_two_text1 = '''En la Tabla se muestra la distribución de documentos según su contribución a los Objetivos de Desarrollo Sostenible (ODS) de la Agenda 2030, tal como son clasificados por WoS (Sustainable Development Goals mapping). El 19.8% de los documentos contribuyen a algún ODS. El ODS más representado en la producción científica es Salud y bienestar (ODS 3), lo que sugiere un fuerte enfoque de investigación en temas médicos, biomédicos o de salud pública. Le siguen Acción por el clima (ODS 13) y Energía asequible y no contaminante (ODS 7), que también muestran una importante contribución.'''
image_four_path = "assets/images/sec_5_img_4.png"
image_four_caption = "Documentos según su contribución a los Objetivos de Desarrollo Sostenible (ODS)"
image_five_path = "assets/images/sec_5_img_5.png"
image_five_caption = "Evolución de la proporción de artículos en los diferentes ODS"


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


#PESTAÑAS
tab1, tab2 = st.tabs([f"1. {sec_one_title}", f"Distribución de Documentos"])

# =========================================================================
# PESTAÑA 1
# =========================================================================
with tab1:
    st.subheader(sec_one_title)

    # Fila 1: Texto y Fig. 19 (Distribución ODS)
    col1, col2 = st.columns([0.6, 1.4])
    with col1:
        st.info(sec_one_text1)
    with col2:
        display_image(image_one_path, image_one_caption)
    
    st.markdown(sec_one_text2)
    display_image(image_two_path, image_two_caption)

    st.markdown(sec_one_text3)
    display_image(image_three_path, image_three_caption)

# =========================================================================
# PESTAÑA 2
# =========================================================================
with tab2:
    st.subheader(sec_two_title)

    col1, col2 = st.columns([0.6, 1.4])
    with col1:
        st.markdown(sec_two_text1)
    with col2:
        display_image(image_four_path, image_four_caption)

    st.markdown("---")

    st.markdown("#### Evolución de la Contribución a ODS")
    col_vacia_2, col_img_5, col_vacia_3 = st.columns([1, 4, 1])
    with col_img_5:
        display_image(image_five_path, image_five_caption)