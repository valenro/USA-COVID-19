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

camas_UCI= st.container()

with camas_UCI:
    st.header('Intensive Care Units by State')
    st.markdown('''To obtain the results of this section, pediatric ICU beds were also included.''')
    
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
    dash2fig.update_layout(title_text="<span style='font-size:22px'><b>Number of Intensive Care Units for COVID-19<b></span>",
                        geo_scope='usa',
                        font=dict(size=14),
                        title={
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})

    st.plotly_chart(dash2fig,use_container_width=True)

    p3=get_df(3)
    fig= px.pie(p3, values='camas_UCI',names='Estado',color_discrete_sequence=colorq,
            )
    fig.update_traces(textinfo='none',marker=dict(line=dict(color='#000000', width=1)))
    fig.update_layout(legend=dict(font=dict(size= 20)),
                        title_text="<span style='font-size:22px'><b>Top 5 States with the highest occupancy of ICU beds during 2020<b></span>",
                        font=dict(size=14),
                        title={
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})
    st.plotly_chart(fig,use_container_width=True)

    p5=get_df(5)
    fig1=px.bar(p5,x='Estado',y='Total camas UCI',color='porcentaje_pacientes_COVID')
    fig1.update_layout(bargap=0.4,title_text="<span style='font-size:22px'><b>Total Intensive Care Units with percentage of COVID-19 patients<b></span>",
                        font=dict(size=14),
                        title={
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})
    
    fig1.update_xaxes(title_text='<b>State</b>',ticks='outside',ticklen=8,color='white')
    fig1.update_yaxes(title_text='<b>Total number of ICU beds</b>',ticks='outside',ticklen=8,color='white')
    st.plotly_chart(fig1,use_container_width=True)
