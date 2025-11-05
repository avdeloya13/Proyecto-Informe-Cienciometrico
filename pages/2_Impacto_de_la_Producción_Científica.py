#SECCION 2

import streamlit as st
import os

st.set_page_config(
    page_title="Reporte Cienciométrico - Sección 2",
    layout="wide",
    initial_sidebar_state="collapsed"
)

main_title = "Impacto de la Producción Científica"

# --- Subsección 1
sec_one_title = "Análisis Comparativo"
sec_one_text = "La siguiente tabla presenta un análisis comparativo de diversos indicadores bibliométricos de impacto del Instituto de Ciencias Nucleares (ICN) de la UNAM para los artículos con y sin grandes colaboraciones y considerando todo el periodo y los últimos 4 años."
image_one_path = "assets/images/sec_2_img_1.png"
image_one_caption = "Tabla 2. Indicadores de impacto"

sec_one_text2 = "A continuación, se describen los indicadores y se resumen las tendencias observadas en la tabla:"
sec_one_text3 = "Times Cited (Veces Citado): Las publicaciones con grandes colaboraciones acumulan un número significativamente mayor de citas en comparación con aquellas sin grandes colaboraciones. En el periodo reciente (2020-2024), esta tendencia se mantiene, aunque con cifras menores debido al menor tiempo para acumular citas. Aunque el número total de citas para los artículos sin grandes colaboraciones es menor, sigue siendo considerable."
sec_one_text4 = "% Docs Cited (Porcentaje de Documentos Citados): Un alto porcentaje de los documentos con grandes colaboraciones son citados (84.09 porciento en todo el periodo y 77.41 prociento en 2020-2024). Las publicaciones sin grandes colaboraciones muestran un porcentaje de citación aún mayor en todo el periodo (90.32%). Como es de esperar, este porcentaje disminuye ligeramente en el periodo reciente (78.41%), superando ligeramente a las GC en este último lapso."
sec_one_text5 = "Category Normalized Citation Impact (Impacto de Citación Normalizado por Categoría): Este indicador compara el promedio de citas de las publicaciones con el promedio mundial en su respectiva categoría temática. Un valor de 1 indica que el impacto es igual al promedio mundial. Las publicaciones con grandes colaboraciones muestran un impacto ligeramente superior al promedio mundial (1.01 en todo el periodo y 0.98 en 2020-2024). Las publicaciones sin grandes colaboraciones se sitúan por debajo del promedio mundial en todo el periodo (0.78), pero muestran una mejora en el periodo reciente (0.84)."
sec_one_text6 = "% Documents in Top 1% (Porcentaje de Documentos en el 1% Más Citado): Un mayor porcentaje de documentos con grandes colaboraciones se encuentra en el selecto grupo del 1% más citado a nivel mundial (1.54 porciento en todo el periodo y 1.38 porciento en 2020-2024). El porcentaje es menor para los artículos sin grandes colaboraciones (0.8 porciento en todo el periodo), pero muestra un incremento notable en el periodo reciente (1.14%)."
sec_one_text7 = "% Documents in Top 10% (Porcentaje de Documentos en el 10% Más Citado): Consistentemente, un mayor porcentaje de documentos con grandes colaboraciones se ubica en el 10% más citado (11.38 porciento en todo el periodo y 11.41 porciento en 2020-2024). En el otro subconjunto los porcentajes son menores (7.54 porciento en todo el periodo y 6.82 porciento en 2020-2024)."
sec_one_text8 = '% Highly Cited Papers (Porcentaje de Artículos Altamente Citados): El porcentaje de GC altamente citados es mayor en el periodo reciente (0.69%) comparado con todo el periodo (0.34%). En el caso de los artículos sin GC se observa una tendencia similar, con un incremento significativo en el periodo reciente (0.72%) respecto a todo el periodo (0.22%). Notablemente, en el periodo 2020-2024, los artículos sinGC superan a las GC en este indicador.'
sec_one_text9 = "Average Percentile (Percentil Promedio): Indica la posición promedio de las publicaciones en relación con todas las demás en su campo. Un percentil más alto sugiere un mejor rendimiento. Los percentiles promedio de artículo con GC son 47.92 para todo el periodo y 43.76 para 2020-2024. Para los artículos sin GC, los percentiles son 45.05 y 40.28 respectivamente. En general, las publicaciones con grandes colaboraciones se sitúan en percentiles ligeramente más altos."
sec_one_text10 = '% Hot Papers (Porcentaje de Artículos "Calientes" o de Tendencia): Se refiere a artículos recientes que han sido citados muy rápidamente después de su publicación. Con respecto a las GC, el porcentaje aumenta del 0.02 porciento en todo el periodo al 0.08 porciento en 2020-2024. Los artículos sin GC también muestran un incremento, pasando del 0.02 porciento al 0.1 porciento en el periodo reciente, superando ligeramente a las GC en este último periodo.'
sec_one_text11 = "Journal Normalized Citation Impact (Impacto de Citación Normalizado por Revista): Este índice compara el impacto de citación de los artículos con el promedio de la revista donde fueron publicados. Con GC, los valores son 0.99 para todo el periodo y 0.93 para 2020-2024. En el caso de los artículos sin GC, los valores son ligeramente inferiores, 0.92 y 0.88 respectivamente. En general, el impacto está cerca del promedio de las revistas."
sec_one_text12 = "H-Index (Índice H): Este indicador mide tanto la productividad como el impacto de las citas de un conjunto de publicaciones. Con GC, el índice H es considerablemente más alto (141 en todo el periodo y 46 en 2020-2024) que sin GC con valores de 108 y 36 respectivamente."
sec_one_text13 = "% Documents in Q1 Journals (Porcentaje de Documentos en Revistas del Cuartil 1): Indica el porcentaje de publicaciones en revistas que se encuentran en el 25 porciento superior de su categoría según el impacto. Con GC, aproximadamente la mitad de las publicaciones se encuentran en revistas Q1 (50.7 porciento en todo el periodo y 50.72 porciento en 2020-2024). Sin GC, el porcentaje es ligeramente menor (46.99 porciento en todo el periodo y 44.46 porciento en 2020-2024)."
sec_one_text14 = "% Documents in Q2 Journals (Porcentaje de Documentos en Revistas del Cuartil 2): Porcentaje de publicaciones en revistas del segundo cuartil (entre el 25% y el 50 porciento superior). Con GC, los porcentajes son 27.78% (todo el periodo) y 32.66% (2020-2024), mientras que sin GC los porcentajes son 29.03% y 35.41 porciento respectivamente. En el periodo reciente, las publicaciones sin grandes colaboraciones tienen una mayor proporción en Q2."
sec_one_text15 = "% Documents in Q3 Journals (Porcentaje de Documentos en Revistas del Cuartil 3): Con GC, 13.96% (todo el periodo) y 11.43% (2020-2024). Sin GC, 15.27% y 14.52 porciento respectivamente."
sec_one_text16 = "% Documents in Q4 Journals (Porcentaje de Documentos en Revistas del Cuartil 4): Con GC, 7.56% (todo el periodo) y 5.19% (2020-2024). Sin GC, 8.7% y 5.61% respectivamente. En ambos casos, se observa una disminución en la proporción de artículos en Q4 en el periodo reciente."
sec_one_text17 = "En términos globales, la mayor parte de la producción científica del ICN se concentra en revistas de alto impacto (Q1 y Q2), tanto si se incluyen las grandes colaboraciones (GC) como si se excluyen. Incluso sin considerar colaboraciones masivas, casi 8 de cada 10 artículos del ICN se publican en revistas del primer y segundo cuartil, lo que refleja un posicionamiento sostenido en revistas de calidad y alto impacto."
image_one_path = "assets/images/sec_2_img_1.png"
image_one_caption = "Tabla 1. Indicadores de impacto"

# --- Subsección 2
sec_two_title = "Conclusiones Generales"
sec_two_text1 = "Las publicaciones con GC tienden a tener un mayor número bruto de citas, un mayor porcentaje de documentos en el top 1% y 10% más citado, y un índice H más alto. También publican ligeramente más en revistas Q1. Su impacto normalizado por categoría y por revista tiende a ser cercano o ligeramente superior al promedio."
sec_two_text2 = "Las publicaciones sin grandes colaboraciones (Sin GC), aunque con un volumen de citas menor, muestran un porcentaje de documentos citados muy alto, especialmente en todo el periodo. En el periodo reciente (2020-2024), muestran un notable incremento en el porcentaje de artículos altamente citados y 'hot papers', superando en estos aspectos a las publicaciones con grandes colaboraciones."

# --- Subsección 3
sec_three_title = "Evolución del Impacto"
sec_three_text1 = "Se muestran dos métricas relacionadas con el impacto de las publicaciones científicas:"
sec_three_text2 = "- MeanTCperArt (línea azul, eje izquierdo): Promedio de citas totales por artículo."
sec_three_text2_2= "- MeanTCperYear (línea verde, eje derecho): Promedio de citas por artículo por año."
image_two_path = "assets/images/sec_2_img_2.png"
image_two_caption = "Citas recibidas por la producción científica del ICN en todo el periodo"

sec_three_text3 = "Se muestra el comportamiento del Category Normalized Citation Impact (CNCI) de la producción científica del ICN entre 1980 y 2024; este indicador compara el número de citas que recibe una publicación con el promedio de citas de publicaciones similares (por año, tipo de documento y categoría temática). Un valor de 1 indica impacto promedio, mayor que 1 implica impacto por encima del promedio, y menor que 1 indica un impacto por debajo del promedio."
sec_three_text4 = "En esta figura se observa un aumento sostenido del impacto normalizado a partir de 2005, con varios picos entre 2011 y 2016, incluso superando un CNCI de 1.5, lo que indica que, en esos años, las publicaciones del ICN fueron categóricamente más citadas que el promedio internacional de su campo. A partir de 2019, el CNCI disminuye, aunque se mantiene mayormente en torno a 1."
image_three_path = "assets/images/sec_2_img_3.png"
image_three_caption = "Category Normalized Citation Impact (CNCI) de la producción científica del ICN entre 1980 y 2024"

sec_three_text5 = "Se presenta la evolución del porcentaje de documentos del ICN ubicados en el top 1% más citado a nivel mundial dentro de su categoría temática y año de publicación, durante el periodo comprendido entre 1980 y 2024. Aunque durante las décadas de 1980 y 1990 no se registran documentos en este rango de excelencia, a partir del año 2000 comienzan a observarse publicaciones altamente citadas. Este comportamiento se intensifica entre 2008 y 2014, con picos notables en 2010 y 2012, años en los que más del 5% de los artículos publicados por el instituto se situaron entre el 1% más citado del mundo. Si bien el volumen de publicaciones de altísimo impacto ha disminuido ligeramente en la última década, el ICN ha mantenido una presencia destacada en la frontera de la investigación científica global."
image_four_path = "assets/images/sec_2_img_4.png"
image_four_caption = "Porcentaje de documentos en top 1 de la producción científica del ICN entre 1980 y 2024"

sec_three_text6 = "A diferencia de la distribución de artículos en el top 1%, sí aparecen artículos en el top 10% desde las décadas de los 80 aunque el comportamiento es irregular, con fluctuaciones marcadas y picos aislados (por ejemplo, en 1984 y 1991), lo que puede deberse al volumen relativamente bajo de publicaciones. A partir de mediados de los años 2000 se observa una tendencia sostenida al alza, alcanzando sus valores más altos entre 2010 y 2015, donde en algunos años más del 20% de los documentos del ICN se situaron en el top 10% más citado del mundo. Aunque en los últimos años (posteriores a 2019) se percibe un descenso, este puede estar relacionado con el menor tiempo de exposición de los documentos recientes a ser citados. En conjunto, esta figura confirma que una proporción significativa y creciente de la producción del ICN ha logrado destacarse por su impacto internacional."
image_five_path = "assets/images/sec_2_img_5.png"
image_five_caption = "Porcentaje de documentos en top 100 de la producción científica del ICN entre 1980 y 2024"

image_six_path = "assets/images/sec_2_img_6.png"
image_six_caption = "Average Percentile de la producción científica del ICN entre 1980 y 2024"

image_seven_path = "assets/images/sec_2_img_7.png"
image_seven_caption = "Evolución del perfil multidimensional de desempeño"

#Para mostrar imagenes con caption centrada y manejo de error.
def display_image(path, caption):
    if not os.path.exists(path):
        st.warning(f"⚠️ Imagen no encontrada en: {path}. Asegúrate de que el directorio 'assets/images/' exista y contenga las imágenes.")
        st.info(f"Placeholder para: {caption}")
        st.image("https://placehold.co/600x460/cccccc/333333?text=IMAGEN+FALTANTE", caption=caption, width="stretch")
    else:
        st.image(path, caption=caption, width="stretch")


def format_description_list(texts):
    st.markdown(sec_one_text2)

    cols_descriptions = st.columns(2)
    
    list_items = [
        sec_one_text3, sec_one_text4, sec_one_text5.replace('<br />', ''), sec_one_text6, sec_one_text7,
        sec_one_text8, sec_one_text9, sec_one_text10, sec_one_text11, sec_one_text12, sec_one_text13, 
        sec_one_text14, sec_one_text15, sec_one_text16
    ]
    
    #Punto de división para 7 elementos por columna
    split_point = 7 
    
    #Columna 1: elementos 0 a 6 (7 elementos)
    with cols_descriptions[0]:
        st.markdown("---")
        for i in range(split_point):

            if i < len(list_items):
                title, value = list_items[i].split(':', 1)
                st.markdown(f"**{title.strip()}:** {value.strip()}")
                st.markdown("---")
            
    #Columna 2: elementos 7 a 13 (7 elementos)
    with cols_descriptions[1]:
        st.markdown("---")
        #Empieza en 7 y termina en el final de la lista (14)
        for i in range(split_point, len(list_items)): 

            if i < len(list_items):
                title, value = list_items[i].split(':', 1)
                st.markdown(f"**{title.strip()}:** {value.strip()}")
                st.markdown("---")

st.title(main_title)
st.markdown("---")

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

#PESTAÑAS
tab1, tab2, tab3 = st.tabs([f"1. {sec_one_title}", f"2. {sec_two_title}", f"3. {sec_three_title}"])

# =========================================================================
# PESTAÑA 1
# =========================================================================
with tab1:
    st.subheader("Métricas Relacionadas con el Impacto de las Publicaciones Científicas")
    st.markdown(sec_one_text)          
    display_image(image_one_path, image_one_caption)

    #Descripción de indicadores
    format_description_list([sec_one_text3, sec_one_text4, sec_one_text5, sec_one_text6, sec_one_text7,
                         sec_one_text8, sec_one_text9, sec_one_text10, sec_one_text11, sec_one_text12,
                         sec_one_text13, sec_one_text14, sec_one_text15, sec_one_text16])

    #Conclusión
    st.info(sec_one_text17)
    st.markdown("---")

# =========================================================================
# PESTAÑA 2
# =========================================================================
with tab2:
    st.subheader("Conclusiones Generales de la Descripción")

    st.markdown(f"**Conclusiones sobre publicaciones con Grandes Colaboraciones (GC):** {sec_two_text1}")
    st.markdown(f"**Conclusiones sobre publicaciones Sin Grandes Colaboraciones (Sin GC):** {sec_two_text2}")
    st.markdown("---")

# =========================================================================
# PESTAÑA 3
# =========================================================================
with tab3:

    st.markdown("### CNCI: Impacto Normalizado por Categoría")
    cols_fig9 = st.columns([2, 3]) #2/5 partes para texto, 3/5 para imagen

    with cols_fig9[0]:
        st.markdown(sec_three_text3)
        st.markdown(sec_three_text4)
        st.success(" El impacto normalizado experimentó un crecimiento sostenido post-2005, superando consistentemente el promedio mundial (CNCI > 1) entre 2011 y 2016.")

    with cols_fig9[1]:
        display_image(image_three_path, image_three_caption)

    st.markdown("---")

    st.markdown("### Top 1%: Artículos de Máxima Excelencia")
    cols_fig10 = st.columns([3, 2])

    with cols_fig10[0]:
        display_image(image_four_path, image_four_caption)

    with cols_fig10[1]:
        st.markdown(sec_three_text5)
        st.info(" Aunque la presencia fue nula en los 80/90, el instituto registró picos de más del 5% de artículos en el Top 1% mundial entre 2010 y 2012.")

    st.markdown("---")

    st.markdown("### Perspectiva Global: Tendencia de Citas y Top 10%")
    st.markdown("Esta sección agrupa la evolución de la tendencia de citas brutas y el porcentaje en el Top 10%, permitiendo una visión comparativa del impacto amplio.")

    col_f8, col_f11 = st.columns(2) #1:1 Columnas para las figuras

    with col_f8:
        st.markdown("#### ⭐ **Citas Recibidas**")
        display_image(image_two_path, image_two_caption)
        with st.expander("Ver Definiciones de Métricas"):
            st.markdown(sec_three_text1)
            st.markdown(sec_three_text2.replace('. ', '\n- ').strip()) #Formato de lista
            st.markdown(sec_three_text2_2)

    with col_f11:
        st.markdown("#### 🏆 **Documentos en Top 10%**")
        display_image(image_five_path, image_five_caption)
        st.markdown(sec_three_text6)

    st.markdown("---")


    # ---AGRUPACIÓN FINAL 1:1 ---
    st.markdown("### Resumen y Perfil de Desempeño Final")
    st.markdown("Las últimas dos figuras ofrecen una visión de resumen: el percentil promedio (rendimiento relativo) y un perfil multidimensional (integración de métricas).")

    col_f12, col_f13 = st.columns(2) #1:1 Columnas para las figuras de resumen

    with col_f12:
        st.markdown("#### 📈 **Evolución del Percentil Promedio**")
        display_image(image_six_path, image_six_caption)

    with col_f13:
        st.markdown("#### 📊 **Perfil Multidimensional de Desempeño**")
        display_image(image_seven_path, image_seven_caption)

