"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re
from datetime import datetime

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    
    strings = [df[col].name for col in df.columns if df[col].dtype == 'object' and col != 'barrio' ]
    df = df.replace('-', ' ', regex=True).replace('_',' ', regex=True)
    
    for i in strings:
        df[i] = df[i].str.lower().str.strip()


    df['barrio'] = df['barrio'].str.lower().replace('_', ' ', regex=True).replace('-', ' ', regex=True)
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df["estrato"] = df["estrato"].astype(int)
    
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='%d/%m/%Y', errors='coerce').fillna(pd.to_datetime(df['fecha_de_beneficio'], format='%Y/%m/%d', errors='coerce'))

    df['monto_del_credito'] = df['monto_del_credito'].str.strip(' ').str.replace('[ ,$]', '').str.replace('\.00','').astype(float)

    df = df.dropna()
    df = df.drop_duplicates()
    
    return df
