import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime
from pandasql import sqldf
from utils.funcion import get_dataframe

st.set_page_config(layout='wide')
@st.cache
def get_df(num):
    return get_dataframe(num)

pysqldf=lambda q: sqldf(q,globals())
mapa_camas= st.container()

st.markdown('# Work in progress')
header= st.container()
camas_UCI= st.container()
ranking= st.container()
camas_fechas= st.container()

with header:
    df=get_df(0)
    st.title('Dashboard análisis COVID-19 en los Estados Unidos')
    st.markdown('''El siguiente informe muestra los datos obtenidos por el CDC de Estados Unidos 
desde el comienzo de la cuarentena en Marzo de 2020 hasta Agosto de 2022. ''')

with mapa_camas:
    st.header('Personas hospitalizadas por Estado')
    st.markdown('''### En este mapa de los Estados Unidos se observa la cantidad de pacientes de COVID-19 hospitalizados en cada Estado.''')
    query10='''
        SELECT state as Estado ,ROUND(SUM(inpatient_beds_used_covid)) as 'Número de hospitalizaciones'
        FROM df
        GROUP BY state
        ORDER BY SUM(inpatient_beds_used_covid) DESC
        ''' 
    dash1=pysqldf(query10)
    dashfig1=px.choropleth(dash1,locations=dash1['Estado'],locationmode='USA-states',
                    scope='usa',color=dash1['Número de hospitalizaciones'],color_continuous_scale=px.colors.sequential.deep,
                    labels={'locations':'Estado','color':'Hospitalizaciones'})
    dashfig1.update_layout(title_text='Cantidad de hospitalizados por COVID-19',geo_scope='usa')
    st.plotly_chart(dashfig1,use_container_width=True)


    st.markdown('''Tomando los datos históricos es evidente que si solo se ven los primeros 5 Estados 
con mayor cantidad de infectados por COVID-19 no difieren tanto del Top 5 Estados 
durante los primeros 6 meses del 2020, momento más crítico de la pandemia 
a nivel global.''')

    p1fig= px.pie(get_df(11), values='Cantidad_camas_comunes',names='Estado',color_discrete_sequence=px.colors.qualitative.Prism,
            title='5 Estados con mayor ocupación hospitalaria hasta Junio de 2020',hole=.3)
    p1fig.update_traces(marker=dict(line=dict(color='#000000', width=1)),textposition='inside', textinfo='percent+label'
)
    p1fig.update_layout(showlegend=False)
    st.plotly_chart(p1fig,use_container_width=True)



with camas_UCI:
    st.header('Unidades de cuidados intensivos por Estado')
    st.markdown('''Para obtener los resultados de este apartado también se incluyeron las camas UCI
de pediatría''')
    
    query11='''
        SELECT state as Estado,(SUM(staffed_icu_adult_patients_confirmed_covid)+SUM(staffed_icu_pediatric_patients_confirmed_covid)) as Unidades_de_Cuidados_Intensivos
        FROM df
        GROUP BY Estado
        ORDER BY Unidades_de_Cuidados_Intensivos DESC
        '''
    dash2=pysqldf(query11)
    dash2fig=px.choropleth(dash2,locations=dash2['Estado'],locationmode='USA-states',
                    scope='usa',color=dash2['Unidades_de_Cuidados_Intensivos'],color_continuous_scale=px.colors.sequential.deep,
                    labels={'Unidades_de_Cuidados_Intensivos':'Unidades de Cuidados Intensivos'})
    dash2fig.update_layout(title_text='Cantidad de Unidades de Cuidados Intensivos por COVID-19',geo_scope='usa')
    st.plotly_chart(dash2fig,use_container_width=True)




with camas_fechas:
    st.header('Cantidad de camas ocupadas entre un rango de fechas')

    d=st.sidebar.date_input(
        'Seleccione una fecha de inicio:',
        datetime.date(2020,1,1))
    d1=st.sidebar.date_input(
        'Seleccione una fecha limite:',
        datetime.date(2022,8,1))
