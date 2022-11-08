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
p2=get_df(2)
p2_1=get_df(21)
p2_2=get_df(22)
p2_3=get_df(23)
p2_4=get_df(24)

pedcama= st.container()
p4 = get_df(4)

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

    st.header('People hospitalized by state')
    st.markdown('''### This map of the United States shows the number of hospitalized COVID-19 patients in each state.''')
    

    dashfig1=px.choropleth(dash1,locations=dash1['Estado'],locationmode='USA-states',
                    scope='usa',color=dash1['Número de hospitalizaciones'],color_continuous_scale=px.colors.sequential.deep,
                    labels={'locations':'State','color':'Hospitalizaciones'})
    dashfig1.update_layout(title_text="<span style='font-size:22px'><b>Number of hospitalized by COVID-19<b></span>",
                        font=dict(size=14),
                        geo_scope='usa',
                        title={
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})
    
    st.plotly_chart(dashfig1,use_container_width=True)


    st.markdown('''Taking historical data, it is evident that if only the first 5 States with the highest number of people infected by COVID-19
                   are seen, they do not differ so much from the Top 5 States during the first 6 months of 2020, the most critical moment of 
                   the global pandemic.''')

    p1fig= px.pie(get_df(1), values='Cantidad_camas_comunes',names='Estado',color_discrete_sequence=px.colors.qualitative.Prism)
    p1fig.update_layout(title_text="<span style='font-size:22px'><b>Top 5 States with the highest hospital occupancy until June 2020'<b></span>",
                        font=dict(size=14),
                        title={
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})
    p1fig.update_traces(marker=dict(line=dict(color='#000000', width=1)),textposition='inside', textinfo='percent+label')
    p1fig.update_layout(showlegend=False)
    st.plotly_chart(p1fig,use_container_width=True)

with nyc:
    fig=go.Figure()

    fig.add_trace(go.Scatter(x=p2['date'],y=p2['inpatient_beds_used_covid'],name='inpatien beds COVID-19', line=dict(width=3)))
    fig.add_trace(go.Scatter(x=p2_3['date'],y=p2_3['inpatient_beds_used_covid'],name='Growth interval', line=dict(width=4)))
    fig.add_trace(go.Scatter(x=p2_4['date'],y=p2_4['inpatient_beds_used_covid'],name='Decrease interval', line=dict(width=4)))
    fig.add_trace(go.Scatter(x=p2_1['date'],y=p2_1['MAX(inpatient_beds_used_covid)'],name='Maximum critical point', marker=dict(size=12),line=dict(width=3)))
    fig.add_trace(go.Scatter(x=p2_2['date'],y=p2_2['MIN(inpatient_beds_used_covid)'],name='Minimum critical point', marker=dict(size=12),line=dict(width=3)))

    fig.update_layout(bargap=0.4,title_text="<span style='font-size:22px'><b>Occupancy of common beds in New York during quarantine<b></span>",
                        font=dict(size=14),
                        title={
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})

    fig.update_xaxes(title_text='<b>Date</b>',ticks='outside',ticklen=8,color='white')
    fig.update_yaxes(title_text='<b>Number of beds</b>',ticks='outside',ticklen=8,color='white')
    st.plotly_chart(fig,use_container_width=True)

with pedcama:
    fig=px.bar(p4,x='Estado',y='N° pacientes pediátricos',color='N° pacientes pediátricos',)
    
    fig.update_layout(bargap=0.4,title_text="<span style='font-size:22px'><b>Number of pediatric patients by State during 2020<b></span>",
                        font=dict(size=14),
                        title={
                            'y':0.9,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})

    fig.update_xaxes(title_text='<b>State</b>',ticks='outside',ticklen=8,color='white')
    fig.update_yaxes(title_text='<b>Number of pediatric common beds</b>',ticks='outside',ticklen=8,color='white')
    st.plotly_chart(fig,use_container_width=True)