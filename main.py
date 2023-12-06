
import xgboost as xgb
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler

import streamlit as st
from PIL import Image


#st.set_page_config(layout="wide")
st.title('Modelo de predicción de variación de stock migratorio Argentina')


st.markdown(
    """
    <style>
        .stApp {
            background-image: url('https://static.vecteezy.com/system/resources/previews/007/080/746/non_2x/grey-map-of-the-world-high-detail-world-map-vector.jpg');
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)






#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('xgb_model_final_3.json')
#anio = st.selectbox('Año:',[2025,2030,2035])




st.sidebar.markdown("<h1 style='text-align: center; color:#893395 ; font-size: 30px;'>Indicadores</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 div style='text-align: center; font-size: 16px;'>Valores en 2020, máximo y mínimo históricos</h3>", unsafe_allow_html=True)

ingresos = st.sidebar.slider("Ingresos per cápita", 5.516, 35.280000, 31.334)
electricidad = st.sidebar.slider('Acceso a electricidad', 92.154800, 100.00, 100.000000)
crecimiento_pbi = st.sidebar.slider('Crecimiento PBI per cápita', -11.845950, 9.844296, -10.812611)
importaciones = st.sidebar.slider('Importaciones de Mercadería', 9.810000e+08, 8.152200e+10, 4.235400e+10)
pobreza = st.sidebar.slider('Pobreza', 25.700000, 50.000000, 42.00)
mortalidad = st.sidebar.slider('Mortalidad', 7.369000, 9.478000, 8.509)
desempleados = st.sidebar.slider('Desempleados con educación avanzada', 2.920000, 13.780000, 4.720)





st.markdown("<h2 style='text-align: center; font-size: 23px;'>Porcentaje de variación de indicadores respecto a 2020</h2>", unsafe_allow_html=True)



# Crear las columnas
columna1, columna2, columna3, columna4, columna5, columna6, columna7 = st.columns(7)

# Definir una función para aplicar el formato según el cambio
def formato_cambio(nombre, cambio):
    if cambio < 0:
        color = "red"
    elif cambio > 0:
        color = "green"
    else:
        color = "#893395"
    return f"<div style='border: 1px solid #893395; padding: 10px; border-radius: 5px; color: {color};'>{nombre} {cambio}%</div>"

# Ingresos
cambio_ingresos = round(((ingresos - 31.334) * 100) / 31.334, 1)
columna1.markdown(formato_cambio("Ingresos", cambio_ingresos), unsafe_allow_html=True)

# Electricidad
cambio_electricidad = round(((electricidad - 100.000000) * 100) / 100.000000, 1)
columna2.markdown(formato_cambio("Electric.", cambio_electricidad), unsafe_allow_html=True)

# Crecimiento PBI
cambio_crecimiento_pbi = round(((crecimiento_pbi - (-10.812611)) * 100) / (10.812611), 1)
columna3.markdown(formato_cambio("Crec. PBI", cambio_crecimiento_pbi), unsafe_allow_html=True)

# Importaciones
cambio_importaciones = round(((importaciones - 4.235400e+10) * 100) / (4.235400e+10), 1)
columna4.markdown(formato_cambio("Import. ", cambio_importaciones), unsafe_allow_html=True)

# Desempleados
cambio_desempleados = round(((desempleados - 4.720) * 100) / (4.720), 1)
columna5.markdown(formato_cambio("Desempl.", cambio_desempleados), unsafe_allow_html=True)

# Pobreza
cambio_pobreza = round(((pobreza - 42.00) * 100) / (42.00), 1)
columna6.markdown(formato_cambio("Pobreza ", cambio_pobreza), unsafe_allow_html=True)

# Mortalidad
cambio_mortalidad = round(((mortalidad - 8.509) * 100) / (8.509), 1)
columna7.markdown(formato_cambio("Mort.   ", cambio_mortalidad), unsafe_allow_html=True)




X = pd.read_csv('para_llenar_2')
X.drop(columns='Unnamed: 0',inplace=True)
X['Year']=2020
X['Ingresos']=ingresos
X['Electricidad']= electricidad
X['Crecimiento PBI per cápita']=crecimiento_pbi
X['Importaciones']=importaciones
X['Desempleados con educación avanzada']=desempleados
X['Pobreza']=pobreza
X['Mortalidad']=mortalidad
X['ISO3_dest_ARG']=1

st.text("") 
st.text("") 
st.text("")
st.text("")  


col1, col2, col3 = st.columns([2, 4, 2])

# Colocar el botón en la columna central
with col2:
    if st.button('Predecir porcentaje de variación en stock migratorio', key='predict_button'):
        migrantes = model.predict(X)
        referencia = ((migrantes[0] - 1859386.375) * 100) / 1859386.375
        if referencia < 0:
            st.markdown(f"<div style='background-color: rgba(255, 0, 0, 0.5); padding: 15px; border-radius: 10px; text-align: center; font-size: 24px;'>{referencia:.2f}%</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background-color: rgba(46, 204, 113, 0.5); padding: 15px; border-radius: 10px; text-align: center; font-size: 24px;'>{referencia:.2f}%</div>", unsafe_allow_html=True)


