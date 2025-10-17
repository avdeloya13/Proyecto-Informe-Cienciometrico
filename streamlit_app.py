# streamlit_app.py
import streamlit as st

st.set_page_config(page_title="Panel Cienciométrico", layout="wide")

st.title("📚 Reportes Cienciométricos")
st.markdown("---")

st.markdown("""
Bienvenida al **Panel Cienciométrico**, una aplicación desarrollada en Python que organiza y presenta
de forma interactiva los principales indicadores y reportes sobre la producción científica.
""")

st.image("assets/images/evolucion_produccion.png", caption="Ejemplo de visualización general", use_container_width=True)

st.info("Utiliza el menú lateral para navegar entre las diferentes secciones del informe.")
