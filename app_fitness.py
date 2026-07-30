import streamlit as st 

st.set_page_config(page_title="Calculadora Nutricional Universal", page_icon="🍎")

st.title("💪🏻 Plan de Nutricion Inteligente")
st.write("Configura tu perfil para obtener tus macros y recomendaciones exactas.")

# --- ENTRADA DE DATOS ---
with st.sidebar:
    st.header("Tu perfil")
    nombre = st.text_input("Nombre:", value="Usuario")
    genero = st.selectbox("Genero:", ["Masculino","Femenino"])
    peso = st.number_input("Peso actual (kg):", value=80.0)
    estatura = st.number_input("Estatura (cm):", value=170)
    edad = st.number_input("Edad:", value=30)
    
    #NUEVO:factor de actividad fisica real
    actividad = st.selectbox(
        "Nivel de actividad:",
        [
            "Sedentario (Poco o nada de ejercicio)"
            "ligero (Ejecicio 1-3 dias/semana)",
            "Moderado (Ejercicio intenso 3-5 dias/semana)",
            "Fuerte (Entrenamiento pesado 6-7 dias/semana)"
            ]
    )
    objetivo = st.selectbox("Tu meta:", ["Bajar Grasa (Cut)", "Mantener","Subir musculo (Bulk)"])

# --- LOGICA DE CALCULO (Formula mifflin-St jeor) ---
if genero == "Masculino":
    tmb = (10 * peso) + (6.25 * estatura) - (5 * edad) + 5
else:
    tmb = (10 * peso) + (6.25 * estatura) - (5 * edad) - 161

# asignacion del multiplicador segun la actividad elegida
if "Sedentario" in actividad:
    multiplicador = 1.2
elif "ligero" in actividad:
    multiplicador = 1.375
elif"moderado" in actividad:
    multiplicador = 1.55
else:
    multiplicador = 1.725

# Calorias de mantenimiento reales 
calorias_base = tmb * multiplicador 

# Ajuste segun el objetivo
if objetivo ==  "Bajar Grasa (cut)":
    calorias_meta = calorias_base - 500
elif objetivo == "Subir musculo (bulk)":
    calorias_meta = calorias_base + 300
else:
    calorias_meta = calorias_base

# Distribucion de Macros Profesional 
proteina = peso * 2.2 #Ajustado a 2.2g por kg para proteger masa mascular 
grasas = peso * 0.9    #0.9g por kg para soporte hormonal estable 
carbos = (calorias_meta - (proteina * 4) - (grasas * 9)) / 4

# Si los cabos dan negativos por un deficit muy agresivo, poner un piso minimo
if carbos < 0:
    carbos = 0

# ---VISUALIZACION---
st.sunheader(f"Plan pesonalizado para:{nombre}")
c1, c2, c3 = st.columns(3)
c1.metric("⚡️ Calorias Diarias", f"{int(calorias_meta)}kcal")
c2.metric("🍗 Proteina", f"{int(proteina)}g")
c3.metric("🍞 Carbos / 🥑 Grasas", f"{int(carbos)}g / {int(grasas)}g")

st.divider()

# ---RECOMENDACION DE FRUTAS CORREGIDAS---
st.subheader("🍎 Guia de Frutas Recomendadas")
st.write("Para tu objetivo actual, estas son las mejores opciones estrategicas:")

col_f1, col_f2 = st.columns(2)
with col_f1:
    if objetivo == "Bajar Grasa (Cut)":
        st.info("**📉 Frutas de alta saciedad y pocas calorias:**")
        st.write("- Fresas (200g - Super Volumen!)")
        st.write("- Sandia (250g - Alta en agua)")
        st.write("- Manzana verde (1 unidad mediana)")
    else:
        st.succes("**🚀 Frutas densas para energia y glucogeno:**")
        st.write("- Platano (1-2 unidades grandes)")
        st.write("- Mango (150g en cubos)")
        st.write("- Uvas (1 taza completa)")

with col_f2:
    st.warning("💡 **Consejo de alimentacion:**")
    if objetivo == "Bajar Grasa(Cut)":
        st.write("Evita los jugosde frutas por completo. Al comer la fruta entera aprovechas la fibra, lo que retrasa el hambre por horas.")
    else:
        st.write("Puedes usar el platano o el mango directamente en tu batido de pre-entrenamiento o post-entrenamiento para recargar energia rapido.")