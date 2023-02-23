import pandas as pd
import datetime
from utils.normalizer import Normalizer as nz

class _exer_call():
        '''
                All the functions from this class returns a dataframe corresponding to
                each question used to develop this project. You can call these functions typing
                "q" + a number desired from 1 to 8 (number of questions).
                
        '''
        df = nz._normalize_df()
        
        def q1():
                df1= nz._normalizer_1()
                
                ex_1 = df1[['state','inpatient_beds_used_covid']].groupby('state').agg({'inpatient_beds_used_covid':'sum'}).sort_values(by='inpatient_beds_used_covid', ascending= False).head()
                ex_1.reset_index(inplace=True)
                return ex_1
        
        def q2():
                df2, df2_1, df2_2 = nz._normalizer_2()
                
                max_df = pd.DataFrame(df2_1[['date','inpatient_beds_used_covid']].max()).T
                
                min_df = pd.DataFrame(df2[['date','inpatient_beds_used_covid']].min()).T
                
                df2 = df2[['date','inpatient_beds_used_covid']]        
                
                
                df2_1 = df2_1[['date','inpatient_beds_used_covid']]
                df2_2 = df2_2[['date','inpatient_beds_used_covid']]
                
                return df2, df2_1, df2_2, max_df, min_df

        def q3(): 
                df3 = nz._normalizer_3()
                df3['ICU_beds'] = df3['staffed_icu_adult_patients_confirmed_covid'] + df3['staffed_icu_pediatric_patients_confirmed_covid']
                
                df3 = df3[['state', 'ICU_beds']].groupby('state').agg({'ICU_beds':'sum'}).sort_values(by = 'ICU_beds', ascending = False).head()
                return df3.reset_index()
        
        def q4():
                df4 = nz._normalizer_3()
                
                df4 = df4[['state','staffed_icu_pediatric_patients_confirmed_covid']].groupby('state').agg({'staffed_icu_pediatric_patients_confirmed_covid' : 'sum'})
                return df4.reset_index()
        
        def q5():
                df5 = _exer_call.df
                df5['pct_covid_patiens'] = (( df5.staffed_icu_adult_patients_confirmed_covid / df5.total_staffed_adult_icu_beds ) * 100 ).round(2)
                
                df5 = df5[['state', 'total_staffed_adult_icu_beds', 'pct_covid_patiens']].groupby('state').agg({'total_staffed_adult_icu_beds' : 'sum',
                                                                                                                'pct_covid_patiens' : 'sum'})
                return df5.reset_index()
        
        def q6():
                df6 = nz._normalizer_6()
                df6 = df6 [['state', 'deaths_covid']].groupby('state').agg({'deaths_covid' : 'sum'}).sort_values('deaths_covid', ascending= False) 
                return df6.reset_index()
        
        def q7():
                df7 = nz._normalizer_6()
                df7['month'] = pd.DatetimeIndex(df7['date']).month
                
                df7 = df7[['month', 'critical_staffing_shortage_today_yes', 'critical_staffing_shortage_today_no', 'deaths_covid']].groupby('month').agg({
                        'critical_staffing_shortage_today_yes' : 'sum', 
                        'critical_staffing_shortage_today_no' : 'sum', 
                        'deaths_covid' : 'sum'}).sort_values(by= 'month')
                return df7.reset_index()
                
        def q8():
                df8 = _exer_call.df
                
                df8['date'] = pd.to_datetime(df8.date)
        
                df8['date'] = df8['date'].dt.strftime('%Y-%m')
               
                df8 = df8[[
                       'date', 
                       'inpatient_beds_used_covid',
                       'staffed_icu_adult_patients_confirmed_covid',
                       'deaths_covid',
                       'critical_staffing_shortage_today_yes'
               ]].groupby('date').agg({
                 'inpatient_beds_used_covid' : 'sum',
                 'staffed_icu_adult_patients_confirmed_covid' : 'sum',
                 'deaths_covid' : 'sum',
                 'critical_staffing_shortage_today_yes' : 'sum',
               }).sort_values(by= 'date')
                return df8.reset_index()