import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pandasql import sqldf
from utils.funcion import get_dataframe

st.set_page_config(layout='wide')
@st.cache
def get_df(num):
    return get_dataframe(num)

pysqldf = lambda q: sqldf(q,globals())
df = get_df(0)
colorq=px.colors.qualitative.Prism
p6 = get_df(6)
p7 = get_df(7)
p8 = get_df(8)

deaths = st.container()

dfMC=df.copy()
query10='''
        SELECT state as Estado ,SUM(deaths_covid) as cant_muertes
        FROM dfMC
        GROUP BY state
        ORDER BY cant_muertes DESC
        ''' 
dash1=pysqldf(query10)

with deaths:
    dash2fig=px.choropleth(dash1,locations=dash1['Estado'],locationmode='USA-states',
                    scope='usa',color=dash1['cant_muertes'],color_continuous_scale=px.colors.sequential.deep,
                    labels={'cant_muertes':'COVID-19 deaths','Estado':'State'})
    dash2fig.update_layout(title_text="<span style='font-size:22px'><b>Number of deaths by COVID-19<b></span>",
                        geo_scope='usa',
                        font=dict(size=14),
                        title={
                            'y':0.98,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})
    dash2fig.update_xaxes(ticks='outside',ticklen=8,color='white')
    dash2fig.update_yaxes(ticks='outside',ticklen=8,color='white')

    st.plotly_chart(dash2fig,use_container_width=True)

    fig=px.bar(p6,  y='Estado',
                    x='Cantidad de muertes',
                    color='Cantidad de muertes',
                    orientation='h',
                    color_continuous_scale=px.colors.sequential.deep,
                    labels={'Cantidad de muertes':'Number of deaths',
                            'Estado':'State'})
    fig.update_layout(title_text="<span style='font-size:22px'><b>Number of deaths by COVID-19 during 2021<b></span>",
                        font=dict(size=14),
                        title={
                            'y':0.98,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})
    fig.update_xaxes(title_text='<b>Number of deaths</b>',ticks='outside',ticklen=8,color='white')
    fig.update_yaxes(title_text='<b>State</b>',ticks='outside',ticklen=8,color='white')
    st.plotly_chart(fig,use_container_width=True)

    
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=p7['Mes'],y=p7['cant_muertes'],name='COVID-19 deaths',line=dict(color='black',width=2)))
    fig1.add_trace(go.Bar(x=p7['Mes'],y=p7['no_falta_personal'],name='No shortage medical staff'))
    fig1.add_trace(go.Bar(x=p7['Mes'],y=p7['si_falta_personal'],name='Shortage medical staff'))

    fig1.update_layout(title_text="<span style='font-size:22px'><b>Relationship between the shortage of medical personnel and deaths from COVID-19 during 2021<b></span>",
                        font=dict(size=14),
                        title={
                            'y':0.98,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})
    fig1.update_xaxes(title_text="Month 2021",ticks='outside',ticklen=8,color='white')
    fig1.update_yaxes(title_text="Quantity",ticks='outside',ticklen=8,color='white')
    st.plotly_chart(fig1,use_container_width=True)

    st.markdown('''Two peaks can be observed in the months of January and September, although the latter is not the highest due to 
                    the lack of medical personnel, it should be taken into account that it is one of the months with the fewest reports.''')

    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    fig2.add_trace(go.Bar(x=p8['fecha'],y=p8['cant_UCI_camas'],name='Number of UCI beds'),secondary_y=False)
    fig2.add_trace(go.Scatter(x=p8['fecha'],y=p8['cant_muertes'],name='COVID-19 deaths'),secondary_y=True)
    fig2.add_trace(go.Bar(x=p8['fecha'],y=p8['cant_camas'],name='Number of common beds'),secondary_y=False)
    fig2.add_trace(go.Scatter(x=p8['fecha'],y=p8['falta_personal'],name='Shortage medical staff'),secondary_y=True)

    fig2.update_layout(title_text="<span style='font-size:22px'><b>Worst month for USA during the pandemic<b></span>",
                        font=dict(size=14),
                        title={
                            'y':0.98,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'})

    fig2.update_xaxes(title_text="Date",ticks='outside',ticklen=8,color='white')
    fig2.update_yaxes(title_text="Bars quantity", secondary_y=False,ticks='outside',ticklen=8,color='white')
    fig2.update_yaxes(title_text="Lines quantity", secondary_y=True,ticks='outside',ticklen=8,color='white')
    st.plotly_chart(fig2,use_container_width=True)

    st.markdown('''In conclusion, January 2021 was the worst month of the pandemic for the United States since, as can be seen in the graph, 
    it was the month with a peak in deaths and high occupancy of both common beds and Intensive Care Units. Although the peak in the lack of 
    medical personnel was during the month of December 2020, this may have influenced the results.''')
