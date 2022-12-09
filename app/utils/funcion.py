import pandas as pd
import datetime
from pandasql import sqldf

def read(dataframe):
        return pd.read_csv(dataframe)

df=read('COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv')
fecha_max=datetime.date(year=2022,month=8,day=2)
df.sort_values(by='date',inplace=True)
df['date']=pd.to_datetime(df['date']).dt.date
df=df.loc[df.date<fecha_max]
pysqldf=lambda q: sqldf(q,globals())


año=datetime.date(year=2020,month=7,day=1)
df1=df.loc[df['date']<año]

pto1 = df1[['state','inpatient_beds_used_covid']].agg({'inpatient_beds_used_covid':'sum'}).groupby('state').sort_values(by='inpatient_beds_used_covid').head(5)
print(pto1)
query1='''SELECT state as Estado,SUM(inpatient_beds_used_covid) as Cantidad_camas_comunes
        FROM df1
        GROUP BY Estado
        ORDER BY Cantidad_camas_comunes DESC
        LIMIT 5
        '''
punto1=pysqldf(query1)


año3=datetime.date(year=2021,month=4,day=1)
df2=df.loc[(df['state']=='NY') & (df['date']<año3)]

query2='''SELECT date,inpatient_beds_used_covid
          FROM df2'''
punto2=pysqldf(query2) 

query2_1='''SELECT date,MAX(inpatient_beds_used_covid)
            FROM df2'''
punto2_1=pysqldf(query2_1) 

query2_2='''SELECT date,MIN(inpatient_beds_used_covid)
            FROM df2'''
punto2_2=pysqldf(query2_2)

fecha1=datetime.date(year=2020,month=3,day=14)
fecha2=datetime.date(year=2020,month=4,day=14)
fecha3=datetime.date(year=2020,month=7,day=2)
df2_1=df.loc[(df['state']=='NY') & (df['date']>=fecha1) & (df['date']<=fecha2)]
df2_2=df.loc[(df['state']=='NY') & (df['date']>=fecha2) & (df['date']<=fecha3)]

query2_3='''SELECT date,inpatient_beds_used_covid
            FROM df2_1'''
punto2_3=pysqldf(query2_3)

query2_4='''SELECT date,inpatient_beds_used_covid
            FROM df2_2'''
punto2_4=pysqldf(query2_4) 

año1=datetime.date(year=2021,month=1,day=1)
df3=df.loc[df.date<año1]

 
query3='''SELECT state as Estado,(SUM(staffed_icu_adult_patients_confirmed_covid)+SUM(staffed_icu_pediatric_patients_confirmed_covid)) as camas_UCI
        FROM df
        GROUP BY Estado
        ORDER BY camas_UCI DESC
        LIMIT 5'''
punto3=pysqldf(query3) 


query4='''SELECT state as Estado,SUM(staffed_icu_pediatric_patients_confirmed_covid) as 'N° pacientes pediátricos'
        FROM df3
        GROUP BY Estado'''
punto4=pysqldf(query4)


query5='''SELECT state as Estado,SUM(total_staffed_adult_icu_beds) as 'Total camas UCI',
        ROUND(((SUM(staffed_icu_adult_patients_confirmed_covid)/SUM(total_staffed_adult_icu_beds))*100),2) as porcentaje_pacientes_COVID
        FROM df
        GROUP BY Estado '''
punto5=pysqldf(query5)

año2=datetime.date(year=2022,month=1,day=1)
df3=df.loc[(df.date>=año1)&(df.date<año2)]

query6='''SELECT state as Estado,SUM(deaths_covid) as 'Cantidad de muertes'
        FROM df3
        GROUP BY Estado
        ORDER BY SUM(deaths_covid) DESC''' 
punto6=pysqldf(query6)


query7='''SELECT strftime('%m',date) as Mes,SUM(critical_staffing_shortage_today_yes) as si_falta_personal,
        SUM(critical_staffing_shortage_today_no) no_falta_personal,SUM(deaths_covid) as cant_muertes
        FROM df3
        GROUP BY Mes
        ORDER BY Mes ASC''' 
punto7=pysqldf(query7)

query8='''SELECT strftime('%Y-%m',date) as fecha,SUM(inpatient_beds_used_covid) as cant_camas, SUM(staffed_icu_adult_patients_confirmed_covid) as cant_UCI_camas,
        SUM(deaths_covid)as cant_muertes, SUM(critical_staffing_shortage_today_yes) as falta_personal
        FROM df
        GROUP BY fecha
        ORDER BY fecha ASC''' 
punto8=pysqldf(query8)

def get_dataframe(number,query=False):
        if number==0: return df
        elif number==1: return punto1
        elif number==2: return punto2
        elif number==21: return punto2_1
        elif number==22: return punto2_2
        elif number==23: return punto2_3
        elif number==24: return punto2_4
        elif number==3: return punto3
        elif number==4: return punto4
        elif number==5: return punto5
        elif number==6: return punto6
        elif number==7: return punto7
        elif number==8: return punto8