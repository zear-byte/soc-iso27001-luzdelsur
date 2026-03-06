import streamlit as st
import pandas as pd
import plotly.express as px
import hashlib

# --- 1. CONFIGURACIÓN DE INTERFAZ DE ALTO NIVEL ---
st.set_page_config(
    page_title="SOC Luz del Sur | Enterprise Security", 
    page_icon="🛡️", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- 2. DISEÑO VISUAL AVANZADO (CSS CUSTOM) ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    h1, h2, h3 { color: #58a6ff; }
    section[data-testid="stSidebar"] { background-color: #161b22; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🛡️ COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.write("---")
    modulo = st.radio(
        "SISTEMA DE GESTIÓN (ISO 27001):",
        ["🚀 Dashboard de Mando", "📦 Activos Críticos", "📊 Análisis de Riesgos", "🔐 Criptografía & VPN", "🕵️ Operaciones SOC"]
    )
    st.write("---")
    st.success("STATUS: SISTEMA EN LÍNEA")

# --- 4. LÓGICA DE MÓDULOS ---

if modulo == "🚀 Dashboard de Mando":
    st.title("📊 Dashboard Estratégico (Sesión 4)")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("DISPONIBILIDAD", "99.99%", "Optimal")
    c2.metric("ATAQUES BLOQUEADOS", "1,240", "+15%", delta_color="inverse")
    c3.metric("INTEGRIDAD DATA", "VERIFIED", "PASS")
    c4.metric("COMPLIANCE ISO", "98%", "Ready")

    st.write("---")
    st.subheader("🌐 Monitoreo de Tráfico Inspeccionado")
    # CORREGIDO: Datos para el gráfico
    df_chart = pd.DataFrame({
        'Hora': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'Paquetes (MB)': [45, 52, 48, 60, 55, 70, 85, 90, 88, 100, 110, 120]
    })
    st.area_chart(df_chart.set_index('Hora'), color="#58a6ff")

elif modulo == "📦 Activos Críticos":
    st.title("📦 Gestión de Activos (A.8)")
    activos = pd.DataFrame({
        "ID": ["LDS-001", "LDS-002", "LDS-003", "LDS-004"],
        "Activo": ["Core Database SQL", "Grid Control SCADA", "VPN Gateway", "Active Directory"],
        "Criticidad": ["CRÍTICO", "CRÍTICO", "ALTO", "ALTO"],
        "Impacto": ["Interrupción Total", "Falla Eléctrica", "Pérdida Acceso", "Suplantación"]
    })
    st.dataframe(activos, use_container_width=True)

elif modulo == "📊 Análisis de Riesgos":
    st.title("📊 Matriz de Riesgo Residual (S2-S3)")
    mitigacion = st.select_slider("Nivel de Madurez de Controles (%)", options=[0, 20, 40, 60, 80, 100], value=40)
    
    riesgos = pd.DataFrame({
        "Amenaza": ["Ransomware", "DDoS", "Fuga Data", "Inyección SQL"],
        "Impacto": [5, 4, 5, 4],
        "Prob_Original": [4, 5, 3, 4]
    })
    riesgos["Prob_Residual"] = riesgos["Prob_Original"] * (1 - (mitigacion / 100))
    
    fig = px.scatter(riesgos, x="Prob_Residual", y="Impacto", text="Amenaza", size="Impacto", color="Amenaza", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif modulo == "🔐 Criptografía & VPN":
    st.title("🔐 Seguridad de Datos (A.10)")
    msg = st.text_input("Ingrese dato para verificar integridad:")
    if msg:
        st.code(f"SHA-256 HASH: {hashlib.sha256(msg.encode()).hexdigest()}")
    
    vpn = st.toggle("Activar Túnel IPsec AES-256")
    if vpn:
        st.success("CONEXIÓN CIFRADA ACTIVA")
    else:
        st.warning("TRÁFICO NO CIFRADO")

elif modulo == "🕵️ Operaciones SOC":
    st.title("🕵️ Cyber Defense Operations (SOC)")
    if st.toggle("Iniciar Escaneo IDS/IPS"):
        st.error("🚨 19:00:15 - [BLOQUEADO] Intento de Brute Force IP 185.22.x.x")
        st.warning("⚠️ 19:02:40 - [ALERTA] Anomalía de tráfico VLAN Miraflores")
        st.info("ℹ️ 19:05:00 - [INFO] Backup incremental exitoso")
