import streamlit as st
import pandas as pd
import plotly.express as px
import hashlib

# --- CONFIGURACIÓN DE NIVEL ENTERPRISE ---
st.set_page_config(page_title="SOC Luz del Sur - Global Security", layout="wide", initial_sidebar_state="expanded")

# Estilo CSS para que parezca una consola de Microsoft Azure/CyberArk
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ SOC Luz del Sur - Sede Miraflores")
st.write("---")

# --- NAVEGACIÓN LATERAL ---
st.sidebar.image("https://cdn-icons-png.flaticon.com", width=100)
st.sidebar.header("Cybersecurity Command Center")
modulo = st.sidebar.radio("Navegación ISO 27001:", 
    ["Dashboard KRI", "Inventario de Activos (A.8)", "Análisis de Riesgos", "Simulador VPN/Cripto (A.10)", "Operaciones SOC (Incidents)"])

# --- MODULO 1: DASHBOARD KRI (SESIÓN 4) ---
if modulo == "Dashboard KRI":
    st.header("📊 Indicadores Clave de Riesgo (KRI)")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Uptime Crítico", "99.99%", "0.01%")
    with col2: st.metric("Intentos de Intrusión", "142", "-12%", delta_color="inverse")
    with col3: st.metric("Vulnerabilidades", "3", "-2", delta_color="normal")
    with col4: st.metric("Compliance ISO 27001", "94%", "Ready")
    
    st.subheader("Tráfico de Red en Tiempo Real")
    df_grafico = pd.DataFrame({'Hora': range(10), 'Alertas': [2, 5, 1, 8, 3, 2, 4, 7, 1, 2]})
    st.line_chart(df_grafico, x='Hora', y='Alertas')

# --- MODULO 2: INVENTARIO DE ACTIVOS (SESIÓN 1) ---
elif modulo == "Inventario de Activos (A.8)":
    st.header("📦 Inventario Técnico de Activos")
    activos = pd.DataFrame({
        "Activo": ["Base de Datos SQL", "Router Borde", "Switch Core", "Laptop Admin", "Backup Cloud"],
        "Categoría": ["Información", "Hardware", "Hardware", "Endpoint", "Backup"],
        "Valor (CID)": [5, 4, 4, 3, 5],
        "Propietario": ["TI-Database", "Net-Admin", "Net-Admin", "RRHH", "TI-Security"]
    })
    st.dataframe(activos, use_container_width=True)
    st.info("Clasificación basada en la Cláusula 5.9 de la norma ISO 27001.")

# --- MODULO 3: ANÁLISIS DE RIESGOS (SESIÓN 2-3) ---
elif modulo == "Análisis de Riesgos":
    st.header("⚠️ Matriz de Riesgo Residual")
    
    # Simulación de mitigación
    mitigacion = st.slider("Nivel de Controles Implementados (%)", 0, 100, 50)
    
    riesgos = pd.DataFrame({
        "Amenaza": ["Ransomware", "Ataque DoS", "Phishing", "Falla Eléctrica"],
        "Impacto": [5, 4, 3, 5],
        "Probabilidad Original": [4, 5, 4, 2]
    })
    
    # Cálculo de Riesgo Residual
    riesgos['Probabilidad Residual'] = riesgos['Probabilidad Original'] * (1 - mitigacion/100)
    
    fig = px.scatter(riesgos, x="Probabilidad Residual", y="Impacto", text="Amenaza", 
                     size="Impacto", color="Amenaza", title="Mapa de Calor de Riesgos",
                     range_x=[0, 6], range_y=[0, 6])
    st.plotly_chart(fig, use_container_width=True)

# --- MODULO 4: CRIPTOGRAFÍA (SESIÓN 12-13) ---
elif modulo == "Simulador VPN/Cripto (A.10)":
    st.header("🔐 Módulo de Cifrado y VPN")
    st.subheader("Simulador de Integridad (Hash SHA-256)")
    texto = st.text_input("Ingresa dato sensible para transmitir vía VPN:")
    if texto:
        hash_res = hashlib.sha256(texto.encode()).hexdigest()
        st.code(f"Integridad (HASH): {hash_res}")
        st.success("✅ Dato listo para encapsulamiento en Túnel IPsec.")

# --- MODULO 5: OPERACIONES SOC (SESIÓN 14) ---
elif modulo == "Operaciones SOC (Incidents)":
    st.header("🕵️ Centro de Operaciones de Seguridad (SOC)")
    
    status = st.toggle("Activar Defensa Proactiva (IPS + Port Security)")
    
    if status:
        st.success("DEFENSA ACTIVA: IPS bloqueando firmas maliciosas.")
        st.write("---")
        st.markdown("**Logs Recientes del SIEM:**")
        st.error("🚨 19:42:01 - Intento de Brute Force bloqueado en Router Miraflores.")
        st.warning("⚠️ 19:43:15 - Escaneo de puertos detectado desde IP 192.168.1.50.")
    else:
        st.error("SISTEMA EN RIESGO: Controles de red desactivados.")
