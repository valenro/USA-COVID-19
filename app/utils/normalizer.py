import datetime
import pandas as pd
from utils.year_caller import YC

class Normalizer():
        '''
                This class contains functions with preprocessed and normalized dataframes
                to then be used in the "exer_call" class.
        '''
        def read(dataframe): return pd.read_csv(dataframe)
        
        def _normalize_df():
                dataframe = Normalizer.read('COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv')
                
                dataframe.sort_values(by='date',inplace=True)
                
                dataframe['date'] = pd.to_datetime(dataframe['date']).dt.date
                dataframe = dataframe.loc[ dataframe.date < datetime.date(year=2022,month=8,day=2) ]
                
                return dataframe
        
        def _normalizer_1():
                df = Normalizer._normalize_df()
                return df.loc[ df['date'] < YC.exer_1() ]
        
        def _normalizer_2():
                dframe = Normalizer._normalize_df()
                year_1, date_1, date_2, date_3 = YC.exer_2()
                              
                dframe_2 = dframe.loc[ (dframe['state'] == 'NY') & (dframe['date'] < year_1) ]
                dframe_2_1 = dframe.loc[ (dframe['state'] == 'NY') & (dframe['date'] >= date_1) & (dframe['date'] <= date_2) ]
                dframe_2_2 = dframe.loc[(dframe['state']=='NY') & (dframe['date']>=date_2) & (dframe['date']<=date_3)]
                
                return dframe_2, dframe_2_1, dframe_2_2
        
        def _normalizer_3():
                df = Normalizer._normalize_df()
                return df.loc[ df['date'] < YC.exer_3() ]
        
        def _normalizer_6():
                df = Normalizer._normalize_df()
                return df.loc[ ( df.date >= YC.exer_3() ) & ( df.date < YC.exer_6() ) ]
        
        def _occ_map():
                df = Normalizer._normalize_df()
                
                df = df[['state', 'inpatient_beds_used_covid']].groupby('state').agg({'inpatient_beds_used_covid' : sum}).round(2)
                return df.reset_index()

        def _deat_map():
                df = Normalizer._normalize_df()
                
                df = df[['state', 'deaths_covid']].groupby('state').agg({'deaths_covid' : sum}).round(2).sort_values(by= 'deaths_covid')
                return df.reset_index()
        
        def _icu_map():
                df = Normalizer._normalize_df()
                
                df['icu'] = df['staffed_icu_adult_patients_confirmed_covid'] + df['staffed_icu_pediatric_patients_confirmed_covid']
                df = df[['state', 'icu']].groupby('state').agg( {'icu' : 'sum' } ).sort_values(by='icu', ascending= False)
                
                return df.reset_index()