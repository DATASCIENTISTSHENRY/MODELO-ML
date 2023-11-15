# MODELO DE PREDICCIÓN DE VARIACIÓN DE STOCK MIGRATORIO EN ARGENTINA

Repositorio para el deploy del modelo ML de migración

link al modelo https://migracion.streamlit.app/

El propósito principal del modelo consiste en estimar el impacto de las variaciones en diversos indicadores, tales como Ingresos per cápita, Acceso a electricidad, Crecimiento PBI per cápita, Importaciones de Mercadería, Personas desempleadas de educación avanzada, Pobreza y Mortalidad, en la cantidad de inmigrantes que recibe argentina.

Para la construcción de este modelo, se generó un conjunto de datos que abarca el período de 1995 a 2020, incluyendo información sobre el flujo migratorio (valor a predecir) de todos los países reconocidos por las Naciones Unidas. Este conjunto de datos también contiene los valores correspondientes a los indicadores mencionados en las columnas. Se seleccionaron las filas que contenían más del 70% de las características no nulas, y se realizaron imputaciones de valores faltantes mediante la técnica de KNN.

Se exploraron varios modelos de regresión, siendo XGBoostRegressor el que ofreció el rendimiento más óptimo, ajustando los hiperparámetros con OPTUNA.

En términos de evaluación del modelo, se logró un coeficiente de determinación (R2) de 0.97, aunque el Valor Absoluto Medio (MAE) fue de 333407. Al analizar las predicciones para Argentina, se observó que, en el conjunto de pruebas, las predicciones fueron sistemáticamente menores que los valores reales.

El análisis de la importancia de características reveló que el indicador "Importaciones de Mercadería" ejerce la mayor influencia en la variación del flujo migratorio. Con este modelo, se facilita el estudio del impacto y la relevancia de las variaciones en los indicadores sobre la inmigracion en  argentina.
