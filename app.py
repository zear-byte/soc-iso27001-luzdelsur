import streamlit as st
import pandas as pd
import plotly.express as px
import hashlib

# --- 1. CONFIGURACIÓN DE INTERFAZ ---
st.set_page_config(
    page_title="SOC Luz del Sur | Enterprise Security", 
    page_icon="🛡️", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- 2. DISEÑO VISUAL CORREGIDO (ALTO CONTRASTE) ---
st.markdown("""
    <style>
    /* Fondo General */
    .main { background-color: #0e1117; }
    
    /* Texto de las Métricas (Cuadros de Disponibilidad, etc.) */
    div[data-testid="stMetricValue"] {
        color: #00ff41 !important; /* Verde Neón para los números */
        font-weight: bold;
    }
    div[data-testid="stMetricLabel"] {
        color: #ffffff !important; /* Blanco puro para los títulos de los cuadros */
        font-size: 1.2rem !important;
    }
    div[data-testid="stMetric"] {
        background-color: #161b22;
        border: 2px solid #30363d;
        padding: 15px;
        border-radius: 12px;
    }

    /* BARRA LATERAL (Sidebar) - Forzar Texto Blanco */
    section[data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 1px solid #58a6ff;
    }
    section[data-testid="stSidebar"] .st-at, section[data-testid="stSidebar"] label {
        color: #ffffff !important; /* Texto de los radio buttons en blanco */
        font-weight: 500;
    }
    
    /* Títulos Principales */
    h1, h2, h3 { color: #58a6ff !important; }
    
    /* Texto general en blanco */
    p, span, li { color: #e6edf3 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #58a6ff;'>🛡️ SOC COMMAND</h1>", unsafe_allow_html=True)
    st.write("---")
    modulo = st.radio(
        "SISTEMA DE GESTIÓN (ISO 27001):",
        ["🚀 Dashboard de Mando", "📦 Activos Críticos", "📊 Análisis de Riesgos", "🔐 Criptografía & VPN", "🕵️ Operaciones SOC"]
    )
    st.write("---")
    st.success("SISTEMA ONLINE")

# --- 4. LÓGICA DE MÓDULOS ---

if modulo == "🚀 Dashboard de Mando":
    st.title("📊 Dashboard Estratégico (Sesión 4)")
    c1, c2, c3, c4 = st.columns(4)
    # Los valores ahora serán legibles y resaltarán
    c1.metric("DISPONIBILIDAD", "99.99%", "Optimal")
    c2.metric("ATAQUES BLOQUEADOS", "1,240", "+15%", delta_color="inverse")
    c3.metric("INTEGRIDAD DATA", "VERIFIED", "PASS")
    c4.metric("COMPLIANCE ISO", "98%", "Ready")

    st.write("---")
    st.subheader("🌐 Monitoreo de Tráfico Inspeccionado")
    df_chart = pd.DataFrame({
        'Hora':,
        'Paquetes (MB)':
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
    st.table(activos) # Cambiado de dataframe a table para mejor lectura

elif modulo == "📊 Análisis de Riesgos":
    st.title("📊 Matriz de Riesgo Residual (S2-S3)")
    mitigacion = st.select_slider("Nivel de Madurez de Controles (%)", options=, value=40)
    
    riesgos = pd.DataFrame({
        "Amenaza": ["Ransomware", "DDoS", "Fuga Data", "Inyección SQL"],
        "Impacto":,
        "Prob_Original":
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
        st.warning("TRÁFICO NO CIFRADO (TEXTO CLARO)")

elif modulo == "🕵️ Operaciones SOC":
    st.title("🕵️ Cyber Defense Operations (SOC)")
    if st.toggle("Iniciar Escaneo IDS/IPS"):
        st.error("🚨 19:00:15 - [BLOQUEADO] Intento de Brute Force IP 185.22.x.x")
        st.warning("⚠️ 19:02:40 - [ALERTA] Anomalía de tráfico VLAN Miraflores")
        st.info("ℹ️ 19:05:00 - [INFO] Backup incremental exitoso")
    else:
        st.info("Active el switch para ver los logs en tiempo real.")
