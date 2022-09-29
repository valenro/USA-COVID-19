import streamlit as st
import plotly.express as px
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
camas_UCI= st.container()

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

    p3=get_df(33)
    fig= px.pie(p3, values='camas_UCI',names='Estado',color_discrete_sequence=colorq,
            title='5 Estados con mayor ocupación de camas UCI durante 2020',hole=.3)
    fig.update_traces(textinfo='none',marker=dict(line=dict(color='#000000', width=1)))
    fig.update_layout(legend=dict(font=dict(size= 20)))
    st.plotly_chart(fig)

    p5=get_df(55)
    fig1=px.bar(p5,x='Estado',y='Total camas UCI',color='porcentaje_pacientes_COVID')
    fig1.update_layout(title_text='Total Unidades de Cuidados Intensivos con porcentaje de pacientes de COVID-19')
    fig1.update_xaxes(title_text='<b>Estado</b>')
    fig1.update_yaxes(title_text='<b>Cantidad</b>')
    st.plotly_chart(fig1)
