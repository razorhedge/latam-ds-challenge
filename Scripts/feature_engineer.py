import pandas as pd
import datetime as dt

t_alta1 = pd.date_range(start='01/01/2017', end='3/03/2017') 
t_alta2 = pd.date_range(start='07/15/2017', end='07/31/2017') 
t_alta3 = pd.date_range(start='9/11/2017', end='09/30/2017')
t_alta4 = pd.date_range(start='12/15/2017', end='01/01/2018')
t_alta = t_alta1.append([t_alta2, t_alta3, t_alta4])

def create_season_feature(data, target:str='Fecha-I', column_name:str='temporada_alta')-> None:
    data[column_name] = pd.to_datetime(data[target]).apply(lambda x: 1 if x.strftime('%m/%d/%Y') in t_alta else 0)


def create_time_diff_feature(data:pd.DataFrame, 
                            column1:str='Fecha-O', 
                            column2:str='Fecha-I', 
                            column_name:str='dif_min')-> None:

    data[column_name]=data[column1]-data[column2]


def create_late_marker_feature(data:pd.DataFrame, target:str='dif_min', column_name:str='atraso_15')-> None:
    data[column_name] = data[target].apply(lambda x: 1 if x>dt.timedelta(minutes=15) else 0)


def create_day_period_feature(data:pd.DataFrame, target:str='Fecha-I', column_name:str='periodo_dia')-> None:
    
    def periodo_dia(hora:int)->str:
        if(5<hora<12):
            return 'mañana'
        elif(12<hora<19):
            return 'tarde'
        elif(hora>19 or hora<5):
            return 'noche'

    data[column_name]= data[target].apply(lambda x: periodo_dia(x.hour))


def create_all_features(data:pd.DataFrame)->pd.DataFrame:
    create_season_feature(data)
    create_time_diff_feature(data)
    create_late_marker_feature(data)
    create_day_period_feature(data)
    return data

    
