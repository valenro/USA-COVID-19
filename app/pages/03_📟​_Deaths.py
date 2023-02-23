import streamlit as st
from utils.plotter import _deaths as d

st.set_page_config(layout='wide')
cont_death = st.container()

with cont_death:
    
    st.plotly_chart(d.death_map(), use_container_width=True)
    
    st.plotly_chart(d.state_deaths(), use_container_width=True)
    
    st.plotly_chart(d.short_medics(), use_container_width=True)
    
    st.markdown('''Two peaks can be observed in the months of January and September, although the latter is not the highest due to 
                    the lack of medical personnel, it should be taken into account that it is one of the months with the fewest reports.''')
    
    st.plotly_chart(d.worst_month(), use_container_width=True)
    
    st.markdown('''In conclusion, January 2021 was the worst month of the pandemic for the United States since, as can be seen in the graph, 
    it was the month with a peak in deaths and high occupancy of both common beds and Intensive Care Units. Although the peak in the lack of 
    medical personnel was during the month of December 2020, this may have influenced the results.''')