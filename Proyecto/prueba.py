import pyodbc as podbc
import pandas as pd


def sql():
    connection = podbc.connect(
        DRIVER= '{SQL Server}',
        Server= 'DESKTOP-SDEUJ3C\SQLEXPRESS',
        Database= 'Proyecto',
        Trusted_Connection= 'Yes'
    )
    return connection


def select_to_df(sql_query, connection):
    try:
        df= pd.read_sql(sql_query, connection)
    except Exception as e:
        print(e)
    connection.close()
    return df


conexion= sql()
df= select_to_df("select * from Autor", conexion)
df
