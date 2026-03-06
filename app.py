import streamlit as st
import pandas as pd
import plotly.express as px
import hashlib

# --- 1. CONFIGURACIÓN DE NIVEL "MICROSOFT AZURE" ---
st.set_page_config(
    page_title="SOC Luz del Sur - ISO 27001", 
    page_icon="🛡️", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Estilo CSS Personalizado para entorno de Ciberseguridad
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div[data-testid="stMetricValue"] { font-size: 24px; color: #00ff41; }
    .stAlert { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BARRA LATERAL (NAVEGACIÓN TÉCNICA) ---
with st.sidebar:
    st.title("🛡️ SOC Command")
    st.markdown("### **Luz del Sur S.A.A.**")
    st.write("Sede: Miraflores | Año: 2026")
    st.write("---")
    
    modulo = st.radio(
        "Módulos del Sistema (ISO 27001):",
        ["Dashboard de Control (KRI)", 
         "Inventario de Activos (A.8)", 
         "Matriz de Riesgos (6.1.2)", 
         "Criptografía y VPN (A.10)", 
         "Centro de Incidentes (SOC)"]
    )
    
    st.write("---")
    st.info("Desarrollado bajo estándares NIST y ISO 27001 para Auditoría Senior.")

# --- 3. LÓGICA DE LOS MÓDULOS ---

# MODULO 1: DASHBOARD ESTRATÉGICO
if modulo == "Dashboard de Control (KRI)":
    st.title("📊 Ecosistema de Defensa Proactiva")
    st.markdown("### Indicadores Clave de Riesgo (Sesión 4)")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Disponibilidad Red", "99.98%", "Estable")
    c2.metric("Alertas Bloqueadas", "42", "+12 hoy")
    c3.metric("Integridad (PKI)", "Activa", "Seguro")
    c4.metric("Compliance Global", "96%", "Optimizado")

    st.write("---")
    st.subheader("Análisis de Tráfico y Amenazas (Tiempo Real)")
    # Datos simulados de ataques detenidos
    df_ataques = pd.DataFrame({
        'Hora': ['10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm'],
        'Ataques Detenidos': [5, 12, 8, 15, 22, 10, 4, 18]
    })
    st.area_chart(df_ataques.set_index('Hora'), color="#00ff41")

# MODULO 2: GESTIÓN DE ACTIVOS
elif modulo == "Inventario de Activos (A.8)":
    st.title("📦 Gestión de Activos de Información")
    st.markdown("#### Inventario basado en la Cláusula 5.9 de ISO 27001")
    
    activos_data = {
        "ID": ["ACT-01", "ACT-02", "ACT-03", "ACT-04", "ACT-05"],
        "Activo": ["Base de Datos Clientes", "Servidores SCADA", "Gateway VPN", "Switches Core", "Backup Off-site"],
        "Categoría": ["Información", "Hardware", "Software", "Hardware", "Servicio"],
        "Criticidad": ["Crítica", "Crítica", "Alta", "Alta", "Media"],
        "Propietario": ["Ciberseguridad", "Operaciones", "Redes", "Redes", "TI"]
    }
    df_activos = pd.DataFrame(activos_data)
    st.table(df_activos)
    st.success("✅ Inventario auditado y clasificado según impacto al negocio.")

# MODULO 3: MATRIZ DE RIESGOS DINÁMICA
elif modulo == "Matriz de Riesgos (6.1.2)":
    st.title("⚠️ Evaluación y Tratamiento de Riesgos")
    
    # Slider de mitigación para simular Riesgo Residual
    nivel_control = st.slider("Implementación de Controles (%)", 0, 100, 40)
    
    datos_riesgo = pd.DataFrame({
        "Amenaza": ["Ransomware", "Ataque DoS", "Fuga de Datos", "Inyección SQL", "Fuerza Bruta"],
        "Impacto": [5, 4, 5, 4, 3],
        "Probabilidad_Original": [4, 5, 3, 4, 5]
    })
    
    # Lógica de Riesgo Residual
    datos_riesgo["Probabilidad_Residual"] = datos_riesgo["Probabilidad_Original"] * (1 - (nivel_control / 100))
    
    fig = px.scatter(
        datos_riesgo, x="Probabilidad_Residual", y="Impacto", 
        text="Amenaza", size="Impacto", color="Amenaza",
        title="Mapa de Calor de Riesgos (Riesgo Residual vs Impacto)",
        range_x=[0, 6], range_y=[0, 6]
    )
    st.plotly_chart(fig, use_container_width=True)
    st.info(f"Con un {nivel_control}% de controles, el riesgo residual se reduce proporcionalmente.")

# MODULO 4: CRIPTOGRAFÍA
elif modulo == "Criptografía y VPN (A.10)":
    st.title("🔐 Seguridad de la Información (Cifrado)")
    st.markdown("#### Simulación de Integridad y Confidencialidad (Sesión 12-13)")
    
    col_izq, col_der = st.columns(2)
    
    with col_izq:
        st.subheader("Cifrado de Mensajes")
        msj = st.text_input("Dato sensible (ej. Password o Token):")
        if msj:
            hash_obj = hashlib.sha256(msj.encode())
            st.code(f"Hash SHA-256: {hash_obj.hexdigest()}")
            st.caption("Este hash garantiza la integridad del dato en tránsito.")
            
    with col_der:
        st.subheader("Estado del Túnel VPN")
        vpn_status = st.toggle("Activar VPN IPsec / TLS")
        if vpn_status:
            st.success("Túnel Encriptado: AES-256-GCM Activo")
            st.image("https://img.icons8.com")
        else:
            st.warning("Tráfico en texto claro (Vulnerable)")

# MODULO 5: OPERACIONES SOC
elif modulo == "Centro de Incidentes (SOC)":
    st.title("🕵️ Centro de Operaciones de Seguridad (SOC)")
    st.markdown("#### Monitoreo Proactivo de Incidentes (Sesión 14)")
    
    defensa = st.toggle("Activar Defensa Perimetral (IDS/IPS)")
    
    if defensa:
        st.success("SISTEMA PROTEGIDO - Sensores en escucha activa.")
        st.write("---")
        st.markdown("**Logs del SIEM (Últimos 5 minutos):**")
        st.error("🚨 [BLOQUEADO] Intento de Inyección SQL desde IP 190.12.44.1")
        st.warning("⚠️ [ALERTA] Escaneo de puertos detectado en VLAN Miraflores.")
        st.info("ℹ️ [INFO] Backup diario completado con éxito.")
    else:
        st.error("SISTEMA VULNERABLE - Controles deshabilitados.")


