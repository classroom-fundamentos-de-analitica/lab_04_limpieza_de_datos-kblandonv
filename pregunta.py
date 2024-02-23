"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    # Cargar el DataFrame desde el archivo CSV
    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    # Tratar datos faltantes
    # Eliminar filas con datos faltantes en cualquier columna
    df.dropna(inplace=True)

    # Tratar duplicados
    # Eliminar filas duplicadas
    df.drop_duplicates(inplace=True)

    # Restablecer el índice después de eliminar filas
    df.reset_index(drop=True, inplace=True)

    return df

# Llamar a la función clean_data para obtener el DataFrame limpio
df_cleaned = clean_data()
print(df_cleaned)