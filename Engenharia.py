import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

#----------------------------------------------------------------------------------------------------
#page config

st.set_page_config(layout="wide",page_title="Projeto 3D Custos",page_icon="💒")

tab1, tab2 = st.tabs(["Custos","Projeto"])


#----------------------------------------------------------------------------------------------------
#dados
link_projeto = "https://sketchfab.com/3d-models/5772-7636e807e8994849af58b1078c83bb66/embed"

#----------------------------------------------------------------------------------------------------



with tab2:
    st.title("Projeto em 3d",anchor= False)
    components.iframe(link_projeto, height=800)