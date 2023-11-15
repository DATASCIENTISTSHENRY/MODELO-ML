
import xgboost as xgb
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler

st.title('Modelo de predicción de variación de stock migratorio Argentina')

#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('xgb_model_final_1.json')


anio = st.selectbox('Año:',[2025,2030,2035])
ingresos = st.slider('Ingresos per cápita',5.516,35.280000,31.334)
electricidad = st.slider('Acceso a electricidad',92.154800,100.00,100.000000)
crecimiento_pbi = st.slider('Crecimiento PBI per cápita',-11.845950	,9.844296,-10.812611)
importaciones = st.slider('Importaciones de Mercadería',9.810000e+08,8.152200e+10,4.235400e+10)
desempleados = st.slider('Personas desempleadas de educación avanzada',2.920000,13.780000,4.720)
pobreza = st.slider('Pobreza',25.700000,42.000000,42.00)
mortalidad = st.slider('Mortalidad',7.369000,9.478000,8.509)

X = pd.read_csv('para_llenar_2')
X.drop(columns='Unnamed: 0',inplace=True)
X['Year']=anio
X['Ingresos']=ingresos
X['Electricidad']= electricidad
X['Crecimiento PBI per cápita']=crecimiento_pbi
X['Importaciones']=importaciones
X['Desempleados con educación avanzada']=desempleados
X['Pobreza']=pobreza
X['Mortalidad']=mortalidad
X['ISO3_dest_ARG']=1


if st.button('Predecir porcentaje de variación en stock migratorio'):
    migrantes = model.predict(X)
    referencia = ((migrantes[0]-1851345.75)*100)/1851345.75
    st.success(f'% de variacion de stock migratorio {referencia:.2f}')

