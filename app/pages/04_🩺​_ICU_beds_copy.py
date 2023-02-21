import streamlit as st
from utils.plotter import _icu_beds as icu

st.set_page_config(layout='wide')

camas_UCI= st.container()

with camas_UCI:
    st.header('Intensive Care Units by State')
    st.markdown('''To obtain the results of this section, pediatric ICU beds were also included.''')
    
    st.plotly_chart(icu.icu_map(), use_container_width=True)
    st.plotly_chart(icu.icu_pie(), use_container_width=True)
    st.plotly_chart(icu.icu_bar(), use_container_width=True)