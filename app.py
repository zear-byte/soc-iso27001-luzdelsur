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

# --- 2. DISEÑO VISUAL MODO CLARO (HIGH CONTRAST LIGHT MODE) ---
st.markdown("""
    <style>
    /* Fondo General Claro */
    .main { background-color: #f8f9fa; color: #212529; }
    
    /* Estilo de las Métricas (Tarjetas Blancas con Sombra) */
    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        border: 1px solid #dee2e6 !important;
        padding: 20px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
    }
    div[data-testid="stMetricValue"] {
        color: #007bff !important; /* Azul Corporativo */
        font-weight: bold !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #495057 !important;
        font-weight: 600 !important;
    }

    /* BARRA LATERAL (Sidebar) Azul Profesional */
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #dee2e6 !important;
    }
    section[data-testid="stSidebar"] .st-at, 
    section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] p {
        color: #212529 !important;
        font-weight: 600 !important;
    }
    
    /* Títulos y Texto */
    h1, h2, h3 { color: #0056b3 !important; font-weight: bold !important; }
    p, span, li { color: #212529 !important; }
    
    /* Botones y Toggles */
    .stButton>button { background-color: #007bff; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #0056b3;'>🛡️ SOC COMMAND</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6c757d;'>Luz del Sur - Miraflores</p>", unsafe_allow_html=True)
    st.write("---")
    modulo = st.radio(
        "MENÚ DE GESTIÓN (ISO 27001):",
        ["🚀 Dashboard de Mando", "📦 Activos Críticos", "📊 Análisis de Riesgos", "🔐 Criptografía & VPN", "🕵️ Operaciones SOC"]
    )
    st.write("---")
    st.success("SISTEMA OPERATIVO ✅")

# --- 4. LÓGICA DE MÓDULOS ---

if modulo == "🚀 Dashboard de Mando":
    st.title("📊 Dashboard Estratégico (Sesión 4)")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("DISPONIBILIDAD", "99.99%", "Óptimo")
    c2.metric("ATAQUES BLOQUEADOS", "1,240", "+15%", delta_color="normal")
    c3.metric("INTEGRIDAD DATA", "VERIFICADA", "PASS")
    c4.metric("COMPLIANCE ISO", "98%", "Ready")

    st.write("---")
    st.subheader("🌐 Monitoreo de Tráfico Inspeccionado")
    # Datos veríficados para el gráfico
    df_chart = pd.DataFrame({
        'Hora': ['08:00', '10:00', '12:00', '14:00', '16:00', '18:00'],
        'Paquetes (MB)': [120, 450, 890, 760, 920, 510]
    })
    st.area_chart(df_chart.set_index('Hora'), color="#007bff")

elif modulo == "📦 Activos Críticos":
    st.title("📦 Gestión de Activos (A.8)")
    activos = pd.DataFrame({
        "ID": ["LDS-001", "LDS-002", "LDS-003", "LDS-004"],
        "Activo": ["Core Database SQL", "Grid Control SCADA", "VPN Gateway", "Active Directory"],
        "Criticidad": ["CRÍTICO", "CRÍTICO", "ALTO", "ALTO"],
        "Impacto": ["Interrupción Total", "Falla Eléctrica", "Pérdida Acceso", "Suplantación"]
    })
    st.table(activos) 

elif modulo == "📊 Análisis de Riesgos":
    st.title("📊 Matriz de Riesgo Residual (S2-S3)")
    st.write("Ajuste el nivel de controles para visualizar la mitigación del riesgo:")
    mitigacion = st.select_slider("Madurez de Controles (%)", options=[0, 20, 40, 60, 80, 100], value=40)
    
    riesgos = pd.DataFrame({
        "Amenaza": ["Ransomware", "DDoS", "Fuga Data", "Inyección SQL"],
        "Impacto": [5, 4, 5, 3],
        "Prob_Original": [0.8, 0.9, 0.7, 0.6]
    })
    riesgos["Prob_Residual"] = riesgos["Prob_Original"] * (1 - (mitigacion / 100))
    
    fig = px.scatter(riesgos, x="Prob_Residual", y="Impacto", text="Amenaza", size="Impacto", color="Amenaza", 
                     template="plotly_white", range_x=[0, 1], range_y=[0, 6])
    st.plotly_chart(fig, use_container_width=True)

elif modulo == "🔐 Criptografía & VPN":
    st.title("🔐 Seguridad de Datos (A.10)")
    msg = st.text_input("Ingrese dato sensible para generar firma digital (Integridad):")
    if msg:
        hash_val = hashlib.sha256(msg.encode()).hexdigest()
        st.info(f"**Hash SHA-256 (Firma Digital):** {hash_val}")
        st.caption("Esta huella digital asegura que el dato no ha sido alterado.")
    
    st.write("---")
    st.subheader("Configuración de Túnel Seguro")
    vpn = st.toggle("Activar VPN Corporativa (Cifrado AES-256)")
    if vpn:
        st.success("🔒 CONEXIÓN CIFRADA ACTIVA - Túnel IPsec Establecido")
    else:
        st.warning("⚠️ ALERTA: Tráfico en texto claro detectado fuera de la VPN")

elif modulo == "🕵️ Operaciones SOC":
    st.title("🕵️ Cyber Defense Operations (SOC)")
    if st.toggle("Iniciar Escaneo IDS/IPS en tiempo real"):
        st.write("### 🚨 Log de Eventos Detectados")
        st.error("🚨 19:00:15 - [BLOQUEADO] Intento de Brute Force IP 185.22.x.x")
        st.warning("⚠️ 19:02:40 - [ALERTA] Anomalía de tráfico detectada en VLAN 10")
        st.success("ℹ️ 19:05:00 - [INFO] Backup incremental verificado con éxito")
    else:
        st.info("Active el switch de arriba para iniciar el monitoreo de incidentes.")

