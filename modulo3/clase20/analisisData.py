import pandas as pd
import os 
ARCHIVO = 'datos.csv'

def leer_datos():
    if not os.path.exists(ARCHIVO):
        print('⚠️ No existe el archivo a analizar. Crealo')
        return None
    try:
        df = pd.read_csv(ARCHIVO)
        return df
    except Exception as e:
        print('⚠️ Error al leer el archivo')
        return None
    
def analizar_data(df):
    if df is None or df.empty:
        print('⚠️ No hay datos para analizar')
        return
    print('📊 RESULTADOS DEL ANALISIS 📊')
    print(f'Cantidad de Registros {len(df)}')
    print(f'🗃️ DataFrame')
    print(df)
    
    print('📈 ESTADISTICA BASICAS DE LOS DATOS')
    print(df.describe())
    
    print('PROMEDIO DE LAS NOTAS')
    print(df['nota'].mean())
    
    print('🥇MAYOR NOTA')
    mayorNota =  df.loc[df['nota'].idxmax()] #*.idxmax() retorna de la tabla, el indice del valor max de esa columna "nota"
    print(mayorNota) #*.id .loc[] accede a la fila del indice dado por parametro q es el registro deseado, lo retorna compelto
    
    
    
def main():
    print(' =============== ANALITICAS ===============')
    df = leer_datos()
    analizar_data(df)
    
main()