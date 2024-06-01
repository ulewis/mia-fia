import streamlit as st

# Función para verificar las reglas de diagnóstico
def diagnosticar_diabetes(datos):
    resultado = 0
    if datos['edad'] >= 20 and datos['edad'] <= 79 and datos['poliuria'] == 1 and datos['polidipsia'] == 1 and datos['perdida_peso'] == 1:
        resultado = 1
    elif datos['edad'] >= 20 and datos['edad'] <= 79 and datos['poliuria'] == 1 and datos['polidipsia'] == 1 and datos['obesidad'] == 1 and datos['paresia_parcial'] == 0 and datos['polifagia'] == 0:
        resultado = 1
    elif datos['edad'] >= 20 and datos['edad'] <= 79 and datos['poliuria'] == 1 and datos['polidipsia'] == 1 and datos['paresia_parcial'] == 1 and datos['obesidad'] == 0 and datos['polifagia'] == 0:
        resultado = 1
    elif datos['edad'] >= 20 and datos['edad'] <= 79 and datos['poliuria'] == 1 and datos['polidipsia'] == 1 and datos['polifagia'] == 1 and datos['obesidad'] == 0 and datos['paresia_parcial'] == 0:
        resultado = 1
    elif datos['poliuria'] == 0 and datos['polidipsia'] == 0 and datos['obesidad'] == 0 and datos['alopecia'] == 1 and datos['picazon'] == 1:
        resultado = 0
    elif datos['rigidez_muscular'] == 0 or datos['perdida_peso'] == 0:
        resultado = 0
    return resultado

# Interfaz de usuario con Streamlit
st.title("Diagnóstico de Diabetes Asistido")

# Entrada de datos
col1, col2, col3 = st.columns(3)

with col1:
    edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
    genero = st.selectbox("Género", ["Masculino", "Femenino"], index=0)
    poliuria = st.selectbox("Poliuria (orinar en exceso)", [0, 1])
    obesidad = st.selectbox("Obesidad", [0, 1])
    debilidad = st.selectbox("Debilidad", [0, 1])
    picazon = st.selectbox("Picazón", [0, 1])

with col2:
    vision_borrosa = st.selectbox("Visión borrosa", [0, 1])
    irritabilidad = st.selectbox("Irritabilidad", [0, 1])
    polidipsia = st.selectbox("Polidipsia (sed excesiva)", [0, 1])
    perdida_peso = st.selectbox("Pérdida súbita de peso", [0, 1])
    polifagia = st.selectbox("Polifagia (hambre excesiva)", [0, 1])

with col3:
    candidiasis_genital = st.selectbox("Candidiasis genital", [0, 1])
    cicatrizacion_tardia = st.selectbox("Cicatrización tardía", [0, 1])
    paresia_parcial = st.selectbox("Paresia parcial", [0, 1])
    rigidez_muscular = st.selectbox("Rigidez muscular", [0, 1])
    alopecia = st.selectbox("Alopecia (pérdida de cabello)", [0, 1])
  

# Botón para diagnóstico
if st.button("Diagnosticar"):
    datos = {
        "edad": edad,
        "genero": genero,
        "poliuria": poliuria,
        "polidipsia": polidipsia,
        "perdida_peso": perdida_peso,
        "debilidad": debilidad,
        "polifagia": polifagia,
        "candidiasis_genital": candidiasis_genital,
        "vision_borrosa": vision_borrosa,
        "picazon": picazon,
        "irritabilidad": irritabilidad,
        "cicatrizacion_tardia": cicatrizacion_tardia,
        "paresia_parcial": paresia_parcial,
        "rigidez_muscular": rigidez_muscular,
        "alopecia": alopecia,
        "obesidad": obesidad
    }

    resultado = diagnosticar_diabetes(datos)
    if resultado == 1:
        st.write("El resultado del diagnóstico es: *Positivo para Diabetes*.")
    else:
        st.write("El resultado del diagnóstico es: *Negativo para Diabetes*.")
