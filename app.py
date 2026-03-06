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
    /* Fondo principal y fuentes */
    .main { background-color: #0d1117; color: #c9d1d9; }
    
    /* Estilo para las métricas (Tarjetas Neón) */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: transform 0.3s;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        border-color: #58a6ff;
    }
    
    /* Títulos y Subtítulos */
    h1, h2, h3 { color: #58a6ff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* Sidebar Profesional */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    
    /* Botones y Toggles */
    .stCheckbox, .stToggleButton { color: #58a6ff; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL ESTRATÉGICA ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #58a6ff;'>🛡️ COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 0.8em;'>LUZ DEL SUR S.A.A. | MIRAFLORES</p>", unsafe_allow_html=True)
    st.write("---")
    
    modulo = st.radio(
        "SISTEMA DE GESTIÓN (ISO 27001):",
        ["🚀 Dashboard de Mando", 
         "📦 Activos Críticos", 
         "📊 Análisis de Riesgos", 
         "🔐 Criptografía & VPN", 
         "🕵️ Operaciones SOC"]
    )
    
    st.write("---")
    st.success("STATUS: SISTEMA EN LÍNEA")
    st.caption("Versión 2.0 - Auditoría Senior 2026")

# --- 4. LÓGICA DE MÓDULOS ---

# MODULO 1: DASHBOARD
if modulo == "🚀 Dashboard de Mando":
    st.title("📊 Ecosistema de Defensa Proactiva")
    st.markdown("Indicadores de Desempeño de Seguridad (S4)")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("DISPONIBILIDAD", "99.99%", "Optimal")
    c2.metric("THREATS BLOCKED", "1,240", "+15%", delta_color="inverse")
    c3.metric("INTEGRITY CHECK", "PASS", "Verified")
    c4.metric("COMPLIANCE ISO", "98%", "Ready")

    st.write("---")
    st.subheader("🌐 Monitoreo Global de Tráfico")
    df_chart = pd.DataFrame({'Hora': range(12), 'Paquetes Inspeccionados':})
    st.area_chart(df_chart, x='Hora', y='Paquetes Inspeccionados', color="#58a6ff")

# MODULO 2: ACTIVOS
elif modulo == "📦 Activos Críticos":
    st.title("📦 Gestión de Activos de Información")
    st.info("Clasificación de activos basada en la Cláusula 5.9 (ISO 27001)")
    
    activos = pd.DataFrame({
        "ID": ["LDS-001", "LDS-002", "LDS-003", "LDS-004"],
        "Activo Tecnológico": ["Core Database SQL", "Grid Control SCADA", "VPN Gateway", "Active Directory"],
        "Criticidad": ["CRÍTICO", "CRÍTICO", "ALTO", "ALTO"],
        "Impacto Negocio": ["Interrupción Total", "Falla Eléctrica", "Pérdida Acceso", "Suplantación Identidad"]
    })
    st.dataframe(activos, use_container_width=True)

# MODULO 3: RIESGOS
elif modulo == "📊 Análisis de Riesgos":
    st.title("📊 Matriz de Riesgo Residual")
    
    st.markdown("Ajuste de controles para visualizar la **mitigación en tiempo real**:")
    mitigacion = st.select_slider("Nivel de Madurez de Controles ISO 27002", 
                                  options=[10, 30, 50, 70, 90, 100], value=50)
    
    riesgos = pd.DataFrame({
        "Amenaza": ["Ransomware", "DDoS", "Fuga Data", "Inyección SQL"],
        "Impacto":,
        "Prob_Original":
    })
    
    riesgos["Prob_Residual"] = riesgos["Prob_Original"] * (1 - (mitigacion / 100))
    
    fig = px.scatter(riesgos, x="Prob_Residual", y="Impacto", text="Amenaza", 
                     size="Impacto", color="Amenaza", template="plotly_dark",
                     range_x=, range_y=)
    st.plotly_chart(fig, use_container_width=True)

# MODULO 4: CRIPTO
elif modulo == "🔐 Criptografía & VPN":
    st.title("🔐 Módulo de Cifrado Corporativo")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Verificación de Integridad")
        msg = st.text_area("Mensaje a Transmitir:")
        if msg:
            st.code(f"SHA-256 HASH: {hashlib.sha256(msg.encode()).hexdigest()}")
            st.caption("Garantiza el No-Repudio y la Integridad.")
    
    with col2:
        st.subheader("Estado de Conectividad")
        vpn = st.toggle("Activar Túnel IPsec con Cifrado AES-256")
        if vpn:
            st.success("TÚNEL ENCRIPTADO ACTIVO")
            st.json({"Protocol": "IKEv2", "Cipher": "AES-GCM", "KeyLength": 256})
        else:
            st.warning("ALERTA: Tráfico en texto claro detectado.")

# MODULO 5: SOC
elif modulo == "🕵️ Operaciones SOC":
    st.title("🕵️ Cyber Defense Operations (SOC)")
    
    if st.toggle("Iniciar Escaneo de Intrusión (IDS/IPS)"):
        st.toast("Iniciando Sensores Suricata...")
        st.success("SISTEMA EN ESCUCHA ACTIVA")
        
        st.markdown("### 🚨 Log de Eventos Recientes")
        st.error("19:00:15 - [BLOQUEADO] Intento de Brute Force desde IP 185.22.x.x")
        st.warning("19:02:40 - [ALERTA] Anomalía de tráfico en VLAN Miraflores")
        st.info("19:05:00 - [INFO] Backup incremental exitoso en la nube")
    else:
        st.error("DEFENSA DESACTIVADA - RIESGO DE INTRUSIÓN ALTO")
