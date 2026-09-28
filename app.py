import streamlit as st
from datetime import date

st.set_page_config(
    page_title="SITIO-SurveillanceHelper",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.block-container {max-width: 1180px; padding-top: 1.5rem; padding-bottom: 3rem;}
[data-testid="stSidebar"] {border-right: 1px solid #E5E7EB;}
h1, h2, h3 {letter-spacing: -0.025em;}
.hero {padding: 24px 26px; border-radius: 18px; background: #F4F8F7; border: 1px solid #D7E6E1; margin-bottom: 18px;}
.card {padding: 18px 20px; border: 1px solid #E5E7EB; border-radius: 15px; background: white; margin: 8px 0 14px;}
.ok {padding: 18px 20px; border-radius: 15px; background: #F0FAF3; border: 1px solid #BFE2C8;}
.warn {padding: 18px 20px; border-radius: 15px; background: #FFF8E8; border: 1px solid #F2D58B;}
.info {padding: 18px 20px; border-radius: 15px; background: #F4F7FB; border: 1px solid #D8E2EF;}
.label {font-size: 0.78rem; font-weight: 700; letter-spacing: .08em; color: #667085; text-transform: uppercase;}
.muted {color:#667085;}
</style>
""", unsafe_allow_html=True)

EMPRESA = "Demo Pharma Paraguay S.A."
PRODUCTOS = ["CARDIOMAX 10 mg", "GLUCOX 5 mg", "MED-X 100 mg"]

if "rfv_aprobados" not in st.session_state:
    st.session_state.rfv_aprobados = set()
if "reportes_demo" not in st.session_state:
    st.session_state.reportes_demo = []

# -------------------------------------------------------------------
# CANAL DE SEGURIDAD COMPARTIBLE (sin acceso al portal)
# Ejemplo: https://TU-APP.streamlit.app/?canal=demo-pharma
# -------------------------------------------------------------------
canal = st.query_params.get("canal")
if canal:
    st.title("SITIO-SurveillanceHelper")
    st.caption(f"Canal de seguridad de {EMPRESA}")
    st.markdown(
        """
        <div class="hero">
        <div class="label">Reporte simple</div>
        <h2 style="margin:.25rem 0;">¿Recibió información sobre un posible efecto adverso?</h2>
        <div>No necesita saber si realmente es una reacción adversa ni completar un formulario técnico.
        Cuéntenos lo que sabe y SITIO hará la evaluación inicial.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.warning("DEMO: no introduzca datos reales de pacientes ni información confidencial.")

    with st.form("reporte_publico"):
        quien = st.selectbox(
            "¿Quién está reportando?",
            ["Visitador médico", "Profesional sanitario", "Farmacia", "Colaborador del laboratorio", "Paciente / familiar", "Otro"],
        )
        producto = st.selectbox("Producto relacionado", PRODUCTOS + ["No lo sé / Otro"])
        relato = st.text_area(
            "¿Qué ocurrió?",
            placeholder="Ejemplo: Un médico me comentó que un paciente presentó mareos intensos después de iniciar el medicamento...",
            height=150,
        )
        contacto = st.text_input("Nombre o contacto para poder ampliar la información (opcional)")
        archivo = st.file_uploader("Adjuntar captura, fotografía o documento (opcional)")
        enviar = st.form_submit_button("Enviar a SITIO", type="primary", use_container_width=True)

    if enviar:
        if not relato.strip():
            st.error("Cuéntenos brevemente qué ocurrió.")
        else:
            st.session_state.reportes_demo.append(
                {"quien": quien, "producto": producto, "relato": relato, "contacto": contacto}
            )
            st.success("Información recibida. SITIO la evaluará y contactará con usted si necesita algún dato adicional.")
            st.caption("En producción, el reporte quedará trazado y llegará automáticamente al Centro de Operaciones SITIO.")

    st.divider()
    st.caption("SITIO BioMedical Solutions · Canal de farmacovigilancia")
    st.stop()

# -------------------------------------------------------------------
# ACCESO AL PORTAL CLIENTE
# -------------------------------------------------------------------
clave = st.secrets.get("CLIENT_APP_PASSWORD", "")
if clave:
    if not st.session_state.get("cliente_autorizado", False):
        st.title("SITIO-SurveillanceHelper")
        st.subheader("Acceso al portal del cliente")
        entrada = st.text_input("Contraseña", type="password")
        if st.button("Entrar", type="primary"):
            if entrada == clave:
                st.session_state.cliente_autorizado = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta.")
        st.stop()
else:
    st.warning("DEMO PÚBLICA: no hay contraseña configurada. No utilice datos reales.")

trabajos = [
    {
        "nombre": "Implementación de BPFV",
        "progreso": 82,
        "estado": "SITIO trabajando",
        "detalle": "Preparación del expediente y evidencias para el proceso ante DINAVISA.",
        "siguiente": "Revisión final y presentación",
    },
    {
        "nombre": "PGR · GLUCOX 5 mg",
        "progreso": 54,
        "estado": "Pendiente de información",
        "detalle": "SITIO está preparando el borrador técnico.",
        "siguiente": "Recibir información de seguridad vigente y pasar a revisión del RFV",
    },
]

pendientes_rfv = [
    {
        "id": "RFV-01",
        "asunto": "PGR · GLUCOX 5 mg",
        "accion": "Revisar borrador preparado por SITIO",
        "resumen": "SITIO completó la estructura inicial del PGR. Se solicita al RFV revisar el documento y confirmar la información local.",
    },
    {
        "id": "RFV-02",
        "asunto": "Caso FV-DEMO-004",
        "accion": "Confirmar evaluación final",
        "resumen": "Caso procesado por SITIO y listo para la revisión final del RFV antes del siguiente paso regulatorio.",
    },
]

st.sidebar.markdown("## SITIO-SurveillanceHelper")
st.sidebar.caption("SITIO BioMedical Solutions")
pagina = st.sidebar.radio(
    "Portal del cliente",
    [
        "Inicio",
        "Estado regulatorio",
        "Trabajo de SITIO",
        "Soporte al RFV",
        "Canal de seguridad",
        "Casos y seguimiento",
        "Documentos y evidencias",
        "Solicitar servicio",
    ],
)
st.sidebar.divider()
st.sidebar.caption("DEMO · Datos ficticios")

st.title("SITIO-SurveillanceHelper")
st.caption(f"{EMPRESA} · Plataforma y servicio gestionado de farmacovigilancia")

if pagina == "Inicio":
    st.markdown(
        """
        <div class="hero">
          <div class="label">Estado general</div>
          <h2 style="margin:.25rem 0;">🟢 Farmacovigilancia bajo control</h2>
          <div>SITIO está gestionando las actividades operativas de farmacovigilancia.</div>
          <div class="muted">Su equipo interviene únicamente cuando necesitamos información, una decisión, revisión o firma.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("BPFV", "En curso", "82%")
    c2.metric("Acciones cliente", "1")
    c3.metric("Pendientes RFV", "2")
    c4.metric("Casos abiertos", "1")

    st.subheader("Necesitamos de usted")
    st.markdown(
        """
        <div class="warn"><b>🟠 GLUCOX 5 mg</b><br>
        Necesitamos la información de seguridad vigente para continuar el PGR.</div>
        """,
        unsafe_allow_html=True,
    )
    st.button("Resolver ahora", type="primary", use_container_width=True)

    st.subheader("Qué está haciendo SITIO")
    for t in trabajos:
        st.markdown(f'<div class="card"><b>{t["nombre"]}</b><br><span class="muted">{t["estado"]}</span></div>', unsafe_allow_html=True)
        st.progress(t["progreso"] / 100, text=f'{t["progreso"]}% completado')
        st.write(t["detalle"])
        st.caption("Siguiente paso: " + t["siguiente"])

    st.subheader("Próximas obligaciones")
    st.dataframe(
        [
            {"Obligación": "Revisión del sistema BPFV", "Fecha": "14/11/2026", "Gestión": "SITIO"},
            {"Obligación": "Revisión PGR GLUCOX", "Fecha": "30/11/2026", "Gestión": "SITIO + RFV"},
            {"Obligación": "Revisión mensual de alertas", "Fecha": "Mensual", "Gestión": "SITIO"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Estado regulatorio":
    st.header("Estado regulatorio")
    a, b, c = st.columns(3)
    a.success("BPFV\n\nEn implementación")
    b.success("RFV\n\nDesignado")
    c.success("Vigilancia regulatoria\n\nActiva")

    st.subheader("Mapa de cumplimiento")
    st.dataframe(
        [
            {"Área": "Sistema BPFV", "Estado": "🟠 En implementación", "Quién lo gestiona": "SITIO"},
            {"Área": "Responsable de Farmacovigilancia", "Estado": "🟢 Designado", "Quién lo gestiona": "Cliente + SITIO"},
            {"Área": "Casos de seguridad", "Estado": "🟢 Sistema activo", "Quién lo gestiona": "SITIO"},
            {"Área": "Vigilancia regulatoria", "Estado": "🟢 Activa", "Quién lo gestiona": "SITIO"},
            {"Área": "PGR / IPS / PSUR", "Estado": "🟠 1 trabajo activo", "Quién lo gestiona": "SITIO + RFV"},
            {"Área": "Evidencias y documentación", "Estado": "🟢 Organizadas", "Quién lo gestiona": "SITIO"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Trabajo de SITIO":
    st.header("Trabajo de SITIO")
    st.write("Aquí puede ver el trabajo que SITIO está realizando por su empresa.")
    for t in trabajos:
        st.markdown(f'<div class="card"><b>{t["nombre"]}</b><br><span class="muted">{t["detalle"]}</span></div>', unsafe_allow_html=True)
        st.progress(t["progreso"] / 100, text=f'{t["progreso"]}%')
        st.write("**Siguiente paso:**", t["siguiente"])

    st.subheader("Actividades recurrentes")
    st.dataframe(
        [
            {"Actividad": "Revisión de alertas regulatorias", "Frecuencia": "Continua", "Estado": "🟢 Gestionado"},
            {"Actividad": "Revisión de literatura", "Frecuencia": "Periódica", "Estado": "🟢 Gestionado"},
            {"Actividad": "Control de vencimientos", "Frecuencia": "Continua", "Estado": "🟢 Gestionado"},
            {"Actividad": "Archivo de evidencias", "Frecuencia": "Continua", "Estado": "🟢 Gestionado"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Soporte al RFV":
    st.header("Soporte al Responsable de Farmacovigilancia")
    st.write("SITIO prepara el trabajo técnico. El RFV revisa, aprueba o firma cuando corresponde.")

    for p in pendientes_rfv:
        aprobado = p["id"] in st.session_state.rfv_aprobados
        estado = "🟢 Revisado" if aprobado else "🟠 Pendiente"
        st.markdown(f'<div class="card"><b>{p["asunto"]}</b><br>{p["accion"]}<br><span class="muted">{estado}</span></div>', unsafe_allow_html=True)
        with st.expander("Ver resumen preparado por SITIO"):
            st.write(p["resumen"])
            if not aprobado and st.button("Marcar como revisado / aprobado", key=p["id"], type="primary"):
                st.session_state.rfv_aprobados.add(p["id"])
                st.rerun()

elif pagina == "Canal de seguridad":
    st.header("Canal SITIO de seguridad")
    st.write("Comparta este enlace con visitadores médicos, colaboradores, profesionales sanitarios o cualquier persona que pueda recibir información de seguridad.")
    st.markdown(
        """
        <div class="info">
        <b>El reportante no necesita completar un formulario técnico.</b><br>
        Puede escribir en lenguaje libre qué ocurrió. SITIO realizará la evaluación inicial y solicitará los datos que falten.
        </div>
        """,
        unsafe_allow_html=True,
    )

    base_url = st.secrets.get("PUBLIC_APP_URL", "https://TU-APP.streamlit.app")
    enlace = base_url.rstrip("/") + "/?canal=demo-pharma"
    st.code(enlace, language=None)
    st.caption("En producción, cada cliente tendrá su propio enlace/QR identificable.")

    st.subheader("Ejemplo de reporte recibido")
    st.markdown(
        """
        > “El Dr. Pérez comentó que un paciente con MED-X tuvo mareos y vómitos dos días después de iniciar el tratamiento. No tengo más información todavía.”
        """
    )
    st.write("SITIO recibe esto, determina qué información falta y realiza el seguimiento.")

elif pagina == "Casos y seguimiento":
    st.header("Casos y seguimiento")
    st.dataframe(
        [
            {"Caso": "FV-DEMO-004", "Producto": "MED-X 100 mg", "Origen": "Visitador médico", "Estado": "Revisión RFV", "Gestión": "SITIO"},
            {"Caso": "FV-DEMO-003", "Producto": "CARDIOMAX 10 mg", "Origen": "Profesional sanitario", "Estado": "Cerrado", "Gestión": "SITIO"},
        ],
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Recorrido de FV-DEMO-004")
    st.write("✅ Información recibida → ✅ Evaluación inicial → ✅ Seguimiento solicitado → ✅ Caso preparado → 🟠 Revisión RFV → ○ Siguiente paso regulatorio → ○ Cierre y evidencia")

elif pagina == "Documentos y evidencias":
    st.header("Documentos y evidencias")
    st.dataframe(
        [
            {"Documento": "Expediente BPFV", "Tipo": "BPFV", "Estado": "En preparación", "Responsable": "SITIO"},
            {"Documento": "PGR · GLUCOX 5 mg", "Tipo": "PGR", "Estado": "Borrador", "Responsable": "SITIO + RFV"},
            {"Documento": "Resumen mensual de farmacovigilancia", "Tipo": "Evidencia", "Estado": "Disponible", "Responsable": "SITIO"},
            {"Documento": "Registro de revisión de alertas", "Tipo": "Evidencia", "Estado": "Disponible", "Responsable": "SITIO"},
        ],
        use_container_width=True,
        hide_index=True,
    )
    st.info("En producción, los documentos destinados al cliente estarán disponibles para descarga. La documentación interna de SITIO no será visible.")

elif pagina == "Solicitar servicio":
    st.header("Solicitar ayuda o un nuevo servicio")
    with st.form("solicitud"):
        tipo = st.selectbox(
            "¿Qué necesita?",
            [
                "DINAVISA me pidió algo",
                "Quiero poner mi farmacovigilancia en regla",
                "Necesito implementar o renovar BPFV",
                "Necesito soporte para mi RFV",
                "Quiero incorporar un medicamento",
                "Necesito PGR / IPS / PSUR",
                "Necesito un estudio post-autorización",
                "Tengo una posible reacción adversa",
                "No sé qué necesito",
            ],
        )
        detalle = st.text_area("Cuéntenos brevemente qué ocurre")
        st.file_uploader("Adjuntar documento (opcional)")
        if st.form_submit_button("Enviar a SITIO", type="primary", use_container_width=True):
            st.success("Solicitud registrada en la demo. SITIO la clasificaría y definiría el siguiente paso.")

st.divider()
st.caption("SITIO BioMedical Solutions · SITIO-SurveillanceHelper · Demo con datos ficticios")
