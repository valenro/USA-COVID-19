import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils.exer_call import _exer_call as ec
from utils.normalizer import Normalizer as nz

'''
    These classes were created to make the plots for each page from 
    the streamlit app. Calling any function it returns a plot by calling
    the dataframes from the "exer_call" class.
'''
class _occupancy():   
    def bed_map(): 
        map_df = nz._occ_map()
        map_fig = px.choropleth(    map_df, locations=map_df.state,locationmode='USA-states',
                                    scope='usa', color=map_df['inpatient_beds_used_covid'],
                                    color_continuous_scale=px.colors.sequential.deep,
                                    labels={'locations':'State','color':'Hospitalizaciones',})
        
        map_fig.update_layout(  title_text="<span style='font-size:22px'><b>Total number of hospitalized by COVID-19<b></span>",
                                font=dict(size=14),
                                geo_scope='usa',
                                title={
                                    'y':0.99,
                                    'x':0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'})
        return map_fig
    
    def state_pie():
        pie_occ = px.pie(ec.q1(), values='inpatient_beds_used_covid',
                                names='state',
                                color_discrete_sequence=px.colors.qualitative.Prism,
                                labels={'state':'State','inpatient_beds_used_covid':'N° common beds'})
        
        pie_occ.update_layout(    title_text="<span style='font-size:22px'><b>Top 5 States with the highest hospital occupancy until June 2020<b></span>",
                                font=dict(size=14),
                                title={
                                    'y':0.98,
                                    'x':0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                                showlegend=False)
        pie_occ.update_traces(marker=dict(line=dict(color='#000000', width=1)),
                            textposition='inside', textinfo='label')
        
        return pie_occ

    def nyc():
        plt_nyc = go.Figure()
        p2, p2_3, p2_4, p2_1, p2_2 = ec.q2() 
        
        plt_nyc.add_trace(go.Scatter(
            x= p2['date'],
            y= p2['inpatient_beds_used_covid'],
            name= 'inpatien beds COVID-19', line=dict(width=3)
        ))
        plt_nyc.add_trace(go.Scatter(
            x= p2_3['date'],
            y= p2_3['inpatient_beds_used_covid'],
            name= 'Growth interval', line=dict(width=4)
        ))
        plt_nyc.add_trace(go.Scatter(
            x= p2_4['date'], 
            y= p2_4['inpatient_beds_used_covid'],
            name= 'Decrease interval', line=dict(width=4)
        ))
        plt_nyc.add_trace(go.Scatter(
            x= p2_1['date'],
            y= p2_1['inpatient_beds_used_covid'],
            name= 'Maximum critical point', marker=dict(size=12),line=dict(width=3)
        ))
        plt_nyc.add_trace(go.Scatter(
            x= p2_2['date'],
            y= p2_2['inpatient_beds_used_covid'],
            name='Minimum critical point', marker=dict(size=12),line=dict(width=3)
        ))

        plt_nyc.update_layout(  bargap=0.4,title_text="<span style='font-size:22px'><b>Occupancy of common beds in New York during quarantine<b></span>",
                                font=dict(size=14),
                                title={
                                    'y':0.9,
                                    'x':0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'})

        plt_nyc.update_xaxes(title_text='<b>Date</b>', ticks='outside', ticklen=8, color='white')
        plt_nyc.update_yaxes(title_text='<b>Number of beds</b>', ticks='outside', ticklen=8, color='white')
        
        return plt_nyc
    
    def bar_ped():
        p4 = ec.q4()
        ped_bar = px.bar(p4,  x='state',
                        y='staffed_icu_pediatric_patients_confirmed_covid',
                        color='staffed_icu_pediatric_patients_confirmed_covid',
                        color_continuous_scale=px.colors.sequential.deep,
                        labels = {  'staffed_icu_pediatric_patients_confirmed_covid' : 'Pediatric patients number',
                                    'state':'State '})
        
        ped_bar.update_layout(  bargap=0.4,
                                title_text="<span style='font-size:22px'><b>Number of pediatric patients by State during 2020<b></span>",
                                font=dict(size=14),
                                title={
                                    'y':0.98,
                                    'x':0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},)

        ped_bar.update_xaxes(title_text='<b>State</b>', ticks='outside', ticklen=8, color='white')
        ped_bar.update_yaxes(title_text='<b>Number of pediatric common beds</b>', ticks='outside', ticklen=8, color='white')
        
        return ped_bar
                
class _deaths():
    def death_map():
        map_df = nz._deat_map()
        
        map_fig = px.choropleth(map_df,locations=map_df['state'],locationmode='USA-states',
                    scope='usa',color=map_df['deaths_covid'],color_continuous_scale=px.colors.sequential.deep,
                    labels={'deaths_covid':'COVID-19 deaths','state':'State'})
        map_fig.update_layout(title_text="<span style='font-size:22px'><b>Number of deaths by COVID-19<b></span>",
                            geo_scope='usa',
                            font=dict(size=14),
                            title={
                                'y':0.98,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'})
        map_fig.update_xaxes(ticks='outside',ticklen=8,color='white')
        map_fig.update_yaxes(ticks='outside',ticklen=8,color='white')
        return map_fig
    
    def state_deaths():
        death_bar = px.bar(ec.q6(),  y='state',
                        x='deaths_covid',
                        color='deaths_covid',
                        orientation='h',
                        color_continuous_scale=px.colors.sequential.deep,
                        labels={'deaths_covid':'Number of deaths',
                                'state':'State'})
        death_bar.update_layout(title_text="<span style='font-size:22px'><b>Number of deaths by COVID-19 during 2021<b></span>",
                            font=dict(size=14),
                            title={
                                'y':0.98,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'})
        death_bar.update_xaxes(title_text='<b>Number of deaths</b>',ticks='outside',ticklen=8,color='white')
        death_bar.update_yaxes(title_text='<b>State</b>',ticks='outside',ticklen=8,color='white')    
        return death_bar
    
    def short_medics():
        p7 = ec.q7()
        compar_plot = go.Figure()
        
        compar_plot.add_trace(go.Scatter( x=p7['month'], y=p7['deaths_covid'], name='COVID-19 deaths', line=dict(color='black',width=2)) )
        compar_plot.add_trace(go.Bar( x=p7['month'], y=p7['critical_staffing_shortage_today_no'], name='No shortage medical staff') )
        compar_plot.add_trace(go.Bar( x=p7['month'], y=p7['critical_staffing_shortage_today_yes'] ,name='Shortage medical staff') )

        compar_plot.update_layout(title_text="<span style='font-size:22px'><b>Relationship between the shortage of medical personnel and deaths from COVID-19 during 2021<b></span>",
                            font=dict(size=14),
                            title={
                                'y':0.98,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'})
        compar_plot.update_xaxes(title_text="<b>Month 2021<b/>",ticks='outside',ticklen=8,color='white')
        compar_plot.update_yaxes(title_text="<b>Quantity<b/>",ticks='outside',ticklen=8,color='white')
        
        return compar_plot
    
    def worst_month():
        p8 = ec.q8()
        month_plot = make_subplots(specs=[[{"secondary_y": True}]])
        
        month_plot.add_trace(go.Bar(x= p8['date'], y= p8['staffed_icu_adult_patients_confirmed_covid'], name= 'Number of UCI beds'), secondary_y=False)
        month_plot.add_trace(go.Scatter(x=p8['date'],y= p8['deaths_covid'], name= 'COVID-19 deaths'), secondary_y=True)
        month_plot.add_trace(go.Bar(x= p8['date'], y= p8['inpatient_beds_used_covid'], name= 'Number of common beds'), secondary_y=False)
        month_plot.add_trace(go.Scatter(x= p8['date'], y= p8['critical_staffing_shortage_today_yes'], name= 'Shortage medical staff'), secondary_y=True)

        month_plot.update_layout(title_text="<span style='font-size:22px'><b>Worst month for USA during the pandemic<b></span>",
                            font=dict(size=14),
                            title={
                                'y':0.98,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'})

        month_plot.update_xaxes(title_text= "<b>Date", ticks= 'outside', ticklen= 8, color='white')
        month_plot.update_yaxes(title_text= "<b>Bars quantity", secondary_y= False, ticks= 'outside', ticklen= 8, color= 'white')
        month_plot.update_yaxes(title_text= "Lines quantity", secondary_y= True, ticks= 'outside', ticklen= 8, color= 'white')
        
        return month_plot

class _icu_beds():
    def icu_map():
        map_df = nz._icu_map()
        
        map_plot = px.choropleth(map_df, locations= map_df['state'], locationmode='USA-states',
                    scope='usa' ,color= map_df['icu'],
                    color_continuous_scale=px.colors.sequential.deep,
                    labels={'icu':'Intensive Care Units',
                            'state':'State'})
        map_plot.update_layout( title_text="<span style='font-size:22px'><b>Number of Intensive Care Units for COVID-19<b></span>",
                                geo_scope='usa',
                                font=dict(size=14),
                                title={
                                    'y':0.98,
                                    'x':0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'})
        return map_plot
    
    def icu_pie():
        pie_plot = px.pie(ec.q3(),
                values= 'ICU_beds',
                names= 'state',
                color_discrete_sequence=px.colors.qualitative.Prism,
                labels = {
                    'ICU_beds':'ICU beds',
                    'state':'State'
                }
            )
        pie_plot.update_layout(  title_text= "<span style='font-size:22px'><b>Top 5 States with the highest ICU beds occupancy<b></span>",
                            font= dict(size=14),
                            title={
                                'y':0.98,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'},
                            showlegend=False)
        pie_plot.update_traces(  marker=dict(line=dict(color='#000000', width=1)),
                            textposition='inside', 
                            textinfo='label')
        return pie_plot
    
    def icu_bar():
        bar_plot= px.bar(ec.q5(), x='state',
                        y='total_staffed_adult_icu_beds',
                        color='pct_covid_patiens',
                        color_continuous_scale=px.colors.sequential.deep,
                        labels = {
                            'pct_covid_patiens' : 'COVID-19 inpacient percentage',
                            'state':'State',
                            'total_staffed_adult_icu_beds': 'Total ICU beds'
                        })
        bar_plot.update_layout( bargap=0.4,title_text="<span style='font-size:22px'><b>Total Intensive Care Units with percentage of COVID-19 patients<b></span>",
                            font=dict(size=14),
                            title={
                                'y':0.98,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'})
        bar_plot.update_xaxes(title_text='<b>State</b>',ticks='outside',ticklen=8,color='white')
        bar_plot.update_yaxes(title_text='<b>Total number of ICU beds</b>',ticks='outside',ticklen=8,color='white')
        return bar_plot