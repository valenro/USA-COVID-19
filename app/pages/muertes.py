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
p6 = get_df(66)
p7 = get_df(77)
p8 = get_df(88)
date_slide=st.sidebar.date_input('',value=min(df.date),min_value=min(df.date),max_value=max(df.date))

st.markdown('# Work in progress')
deaths = st.container()

dfMC=df.copy()
dfMC['date']=date_slide
query10='''
        SELECT date,state as Estado ,SUM(deaths_covid) as cant_muertes
        FROM dfMC
        GROUP BY state,date
        ORDER BY cant_muertes DESC
        ''' 
dash1=pysqldf(query10)


with deaths:
    dash2fig=px.choropleth(dash1,locations=dash1['Estado'],locationmode='USA-states',
                    scope='usa',color=dash1['cant_muertes'],color_continuous_scale=px.colors.sequential.deep,
                    labels={'cant_muertes':'Muertes por COVID-19'})
    dash2fig.update_layout(title_text='Cantidad de muertes por COVID-19',geo_scope='usa')
    st.plotly_chart(dash2fig,use_container_width=True)

    fig=px.bar(p6,y='Estado',x='Cantidad de muertes',color='Cantidad de muertes',
            orientation='h')
    fig.update_layout(title_text='Cantidad de muertes por COVID-19 durante 2021')
    fig.update_xaxes(title_text='<b>Cantidad</b>')
    fig.update_yaxes(title_text='<b>Estado</b>')
    st.plotly_chart(fig)

    
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=p7['Mes'],y=p7['cant_muertes'],name='Muertes por COVID-19',line=dict(color='black',width=2)))
    fig1.add_trace(go.Bar(x=p7['Mes'],y=p7['no_falta_personal'],name='No falta personal médico'))
    fig1.add_trace(go.Bar(x=p7['Mes'],y=p7['si_falta_personal'],name='Falta personal médico'))

    fig1.update_layout(title_text='Relación entre la escasez de personal médico con las muertes por COVID-19 durante 2021')
    fig1.update_xaxes(title_text="Mes 2021")
    st.plotly_chart(fig1)

    st.markdown('''Se pueden observar dos picos en los meses de Enero y Septiembre, aunque este último 
no sea el mayor con falta de personal médico, se debe tener en cuenta que es uno de los meses con menor 
cantidad de reportes.''')

    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    fig2.add_trace(go.Bar(x=p8['fecha'],y=p8['cant_UCI_camas'],name='Cantidad camas UCI'),secondary_y=False)
    fig2.add_trace(go.Scatter(x=p8['fecha'],y=p8['cant_muertes'],name='Muertes por COVID-19'),secondary_y=True)
    fig2.add_trace(go.Bar(x=p8['fecha'],y=p8['cant_camas'],name='Cantidad camas comunes'),secondary_y=False)
    fig2.add_trace(go.Scatter(x=p8['fecha'],y=p8['falta_personal'],name='Falta de personal médico'),secondary_y=True)

    fig2.update_layout(title_text='Peor mes para los Estados Unidos durante la pandemia')
    fig2.update_xaxes(title_text="Fecha")
    fig2.update_yaxes(title_text="<b>Barras</b>", secondary_y=False)
    fig2.update_yaxes(title_text="<b>Lineas</b>", secondary_y=True)
    st.plotly_chart(fig2)

    st.markdown('''En conclusión, Enero de 2021 fue el peor mes de pandemia para Estados Unidos ya que como 
    se puede ver en el gráfico fue el mes con un pico de muertes y alta ocupación de camas tanto comunes 
como Unidades de Terapia Intensiva. Si bien el pico de falta de personal médico fue durante el mes de Diciembre
de 2020, tal vez esto influyó en los resultados.''')
