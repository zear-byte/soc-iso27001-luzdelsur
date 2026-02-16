import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="SOC Luz del Sur - Miraflores", layout="wide")

st.title("🛡️ Ecosistema de Defensa Proactiva - ISO 27001")
st.markdown("### Empresa Eléctrica - Miraflores (Año 2026)")

# --- NAVEGACIÓN LATERAL ---
st.sidebar.header("Módulos del Sistema")
opcion = st.sidebar.selectbox("Selecciona una sección:", 
    ["Resumen Ejecutivo (KRI)", "Inventario de Activos (S1)", "Matriz de Riesgos (S2-S3)", "Operaciones SOC (S5)"])

if opcion == "Resumen Ejecutivo (KRI)":
    st.header("📊 Indicadores Clave de Riesgo (Sesión 4)")
    c1, c2, c3 = st.columns(3)
    c1.metric("Disponibilidad de Red", "99.98%", "Estable")
    c2.metric("Integridad (VPN-PKI)", "Activo", "Seguro")
    c3.metric("Alertas Bloqueadas", "24", "+5 hoy")
    
    st.info("Estos indicadores permiten la toma de decisiones según la Cláusula 9 de la ISO 27001.")

elif opcion == "Inventario de Activos (S1)":
    st.header("📦 Gestión de Activos de Información")
    activos = pd.DataFrame({
        "Activo": ["Base de Datos Clientes", "Servidores VLAN 10", "Gateway VPN", "Switches Capa 2"],
        "Categoría": ["Información", "Hardware", "Software", "Hardware"],
        "Criticidad": ["Alta", "Alta", "Media", "Alta"]
    })
    st.table(activos)

elif opcion == "Matriz de Riesgos (S2-S3)":
    st.header("⚠️ Análisis de Riesgos")
    datos_riesgo = pd.DataFrame({
        "Amenaza": ["MAC Flooding", "Ransomware", "DoS", "ARP Spoofing"],
        "Impacto": [4, 5, 4, 3],
        "Probabilidad": [3, 2, 4, 5]
    })
    fig = px.scatter(datos_riesgo, x="Probabilidad", y="Impacto", text="Amenaza", 
                     size=[30,30,30,30], color="Amenaza")
    st.plotly_chart(fig)

elif opcion == "Operaciones SOC (S5)":
    st.header("🕵️ Control de Operaciones SOC")
    st.subheader("Hardening de Red (Reporte Técnico)")
    
    col_a, col_b = st.columns(2)
    with col_a:
        hardening = st.toggle("Activar Port Security (A.12.1.2)")
        vpn = st.toggle("Activar Cifrado PKI (A.13.1.2)")
    
    with col_b:
        if hardening and vpn:
            st.success("✅ DEFENSA PROACTIVA ACTIVADA")
            st.code("LOG: [BLOQUEADO] Intento de intrusión en VLAN Miraflores.")
        else:
            st.warning("⚠️ SISTEMA VULNERABLE - Active los controles.")