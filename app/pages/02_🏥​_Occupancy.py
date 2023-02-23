import streamlit as st
from utils.plotter import _occupancy as occ

st.set_page_config(layout='wide')
mapa_camas = st.container()
pedcama= st.container()
nyc = st.container()


with mapa_camas:
    st.subheader('People hospitalized by state')
    st.markdown(''' 
                    > This map of the United States shows the number of 
                    > hospitalized COVID-19 patients in each state.
                    ''')
    
    st.plotly_chart(occ.bed_map(),use_container_width=True)
    
    st.markdown(''' 
                    > Taking historical data, it is evident that if only the first 5 States with the highest 
                    > number of people infected by COVID-19 are seen, they do not differ so much from 
                    > the Top 5 States during the first 6 months of 2020, the most critical moment 
                    > of the global pandemic.
                    ''')
    
    st.plotly_chart(occ.state_pie(),use_container_width=True)

with nyc:
    st.markdown(
        '''
        > In the below graphic, you will see the number of occupied beds until the last days of March 
        > approximately when quarantine was declared over in New York state.
        ''')
    st.plotly_chart(occ.nyc(),use_container_width=True)

with pedcama:
    st.plotly_chart(occ.bar_ped(),use_container_width=True)
    
