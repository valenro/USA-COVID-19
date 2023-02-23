import datetime

class YC():
        '''
                Auxiliary class to return different datetimes which were
                used to filter the dataframes by date.
        '''
        def exer_1(): return datetime.date( year = 2020, month = 7, day = 1 )
        
        def exer_2(): 
                return datetime.date( year = 2021, month = 4, day = 1 ),  datetime.date( year = 2020, month = 3, day = 14 ),  datetime.date( year = 2020, month = 4, day = 14 ), datetime.date( year = 2020, month = 7, day = 2 )

        def exer_3(): return datetime.date( year = 2021, month = 1, day = 1 )
        
        def exer_6(): return datetime.date( year = 2022, month = 1, day = 1 )