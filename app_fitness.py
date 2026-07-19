import streamlit as st

st.set_page_config(page_title="calculadora Nutricional Universal", page_icon="🍎")

st.title("🚀Plan de Nutricion Inteligente")
st.write("configura tu perfil para obtener tus macros y recomendaciones.")

#--- ENTRADA DE DATOS ---
with st.sidebar:
    st.header("tu Perfil")
    nombre = st.text_input("Nombre:",value="usuario")
    genero = st.selectbox("Genero:",["Masculino","Femenino"])
    peso = st.number_input("Peso actual(kg):", value=80.0)
    estatura = st.number_input("Estatura(cm):", value=170)
    edad = st.number_input("Edad:", value=30)
    objetivo = st.selectbox("Tu meta:",["Bajar Grasa (Cut)", "Mantener", "Subir Musculo (Bulk)"])

# --- LOGICA DE CALCULO (Formula Mifflin-St Jeor) ---
if genero == "Masculino":
    tmb = (10 * peso) + (6.25 * estatura) - (5 * edad) + 5
else:
    tmb = (10 * peso) + (6.25 * estatura) - (5 * edad) - 161

# Ajuste por actividad moderada (x 1.2 como base)
calorias_base = tmb * 1.2
if objetivo == "Bajar Grasa (Cut)":
    calorias_meta = calorias_base - 500
elif objetivo == "subir Musculo (Bulk)":
    calorias_meta = calorias_base + 300
else:
    calorias_meta = calorias_base

# Distribucion de Macros
proteina = peso * 2.0 # 2g por kg
grasas = peso * 0.8 # 0.8g por kg 
carbos = (calorias_meta - (proteina * 4) - (grasas * 9) ) / 4

# --- VIZUALIZACION ---
st.subheader(f"plan para {nombre}")
c1, c2, c3, = st.columns(3)
c1.metric("Calorias Diarias",f"{int(calorias_meta)}kcal")
c2.metric("proteina",f"{int(proteina)}g")
c3.metric("carbos",f"{int(carbos)}g / {int(grasas)}g")

st.divider()

# --- RECOMENDACIONES DE FRUTAS ---
st.subheader("🍎 Guia de Frutas recomendadas")
st.write("Para tu objetivo, estas son las mejores opciones:")

col_f1, col_f2 = st.columns(2)
with col_f1:
    if objetivo == "Bajar Grasa(cut)":
        st.info("**Frutas bajas en calorias:**")
        st.write("- Fresas (150g)\n- Sandia (200g)\n- Manzana verde (1 unidad)")
    else:
        st.success("**Frutas para energia:**")
        st.write("- Platano (1-2 unidades)\n- Mango (150g)\n- Uvas (1 taza)")

with col_f2:
    st.warning("💡 **Tip de fibra:**")
    st.write("intenta comer la fruta entera en lugar de jugos para mantenerte saciadopor mas tiempo.")
