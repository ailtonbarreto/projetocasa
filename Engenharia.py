import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


#----------------------------------------------------------------------------------------------------
#page config

st.set_page_config(layout="wide",page_title="Projeto 3D Custos",page_icon="💒")

tab1, tab2 = st.tabs(["Custos","Projeto"])


#----------------------------------------------------------------------------------------------------
#dados
link_projeto = "https://sketchfab.com/3d-models/5843-701c706d2af6416a863099e55981e218"
link_planilha = "https://docs.google.com/spreadsheets/d/e/2PACX-1vST4hynvdLNKaV0sVyg_vTtLGQmCnPPRgq8-TEztlYhG_rqVtlCjlOEbekBOufGVbbJDI5FMmJ6zhFZ/pub?output=csv"

df = pd.read_csv(link_planilha)

with tab1:
    df

#----------------------------------------------------------------------------------------------------



with tab2:
    st.title("Projeto em 3d",anchor= False)
    components.iframe(link_projeto, height=800)