import xgboost as xgb
import streamlit as st
import pandas as pd

st.title('Modelo')

#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('xgb_model_final.json')


anio = st.selectbox('Año:',[2025,2030,2035])
ingresos = st.slider('ingreso',24.77000	,28.14000,26.45500)
electricidad = st.slider('electricidad',92.154800,100.00,96.835889)
crecimiento_pbi = st.slider('crecimiento PBI per capita',-11.845950,9.844296,1.049743)
importaciones = st.slider('importaciones',9.810000e+08,8.152200e+10,2.252089e+10)
desempleados = st.slider('desempleados',2.920000,13.780000,4.838235)
pobreza = st.slider('pobreza',25.700000,42.000000,34.571429)
mortalidad = st.slider('mortalidad',7.369000,9.478000,8.221274)

X = pd.read_csv('para_llenar_1')
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

if st.button('Predecir Migrantes'):
    migrantes = model.predict(X)
    migrantes_redondeados = round(migrantes[0])
    st.success(f'Cantidad de inmigrantes predicha por el modelo: {migrantes_redondeados} en {anio}')


