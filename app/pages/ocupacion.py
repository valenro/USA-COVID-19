import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from pandasql import sqldf
from utils.funcion import get_dataframe

st.set_page_config(layout='wide')
@st.cache
def get_df(num):
    return get_dataframe(num)

df = get_df(0)

pysqldf = lambda q: sqldf(q,globals())
colorq=px.colors.qualitative.Prism

st.markdown('# Work in progress')
mapa_camas = st.container()

nyc = st.container()
p2=get_df(22)
p2_1=get_df(221)
p2_2=get_df(222)
p2_3=get_df(223)
p2_4=get_df(224)

pedcama= st.container()
p4 = get_df(44)

date_slide=st.sidebar.date_input('',value=min(df.date),min_value=min(df.date),max_value=max(df.date))

with mapa_camas:
    dfMC=df.copy()
    dfMC['date']=date_slide
    query10='''
            SELECT date,state as Estado ,ROUND(SUM(inpatient_beds_used_covid)) as 'Número de hospitalizaciones'
            FROM dfMC
            GROUP BY state,date
            ORDER BY SUM(inpatient_beds_used_covid) DESC
            ''' 
    dash1=pysqldf(query10)

    st.header('Personas hospitalizadas por Estado')
    st.markdown('''### En este mapa de los Estados Unidos se observa la cantidad de pacientes de COVID-19 hospitalizados en cada Estado.''')
    

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

with nyc:
    fig=go.Figure()

    fig.add_trace(go.Scatter(x=p2['date'],y=p2['inpatient_beds_used_covid'],name='Camas pacientes COVID-19', line=dict(width=3)))
    fig.add_trace(go.Scatter(x=p2_3['date'],y=p2_3['inpatient_beds_used_covid'],name='Intervalo de Crecimiento', line=dict(width=4)))
    fig.add_trace(go.Scatter(x=p2_4['date'],y=p2_4['inpatient_beds_used_covid'],name='Intervalo de Decrecimiento', line=dict(width=4)))
    fig.add_trace(go.Scatter(x=p2_1['date'],y=p2_1['MAX(inpatient_beds_used_covid)'],name='Punto crítico máximo', marker=dict(size=12),line=dict(width=3)))
    fig.add_trace(go.Scatter(x=p2_2['date'],y=p2_2['MIN(inpatient_beds_used_covid)'],name='Punto crítico mínimo', marker=dict(size=12),line=dict(width=3)))

    fig.update_xaxes(title_text='<b>Fecha</b>')
    fig.update_yaxes(title_text='<b>Cantidad</b>')
    st.plotly_chart(fig)

with pedcama:
    fig=px.bar(p4,x='Estado',y='N° pacientes pediátricos',color='N° pacientes pediátricos',)

    fig.update_layout(title_text='Cantidad de pacientes pediátricos por Estado durante 2020')
    fig.update_xaxes(title_text='<b>Estado</b>')
    fig.update_yaxes(title_text='<b>Cantidad</b>')
    st.plotly_chart(fig)