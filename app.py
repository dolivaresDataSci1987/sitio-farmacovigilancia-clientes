import streamlit as st
from datetime import date

st.set_page_config(
    page_title="SITIO Farmacovigilancia",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.block-container {max-width: 1100px; padding-top: 1.6rem; padding-bottom: 3rem;}
h1, h2, h3 {letter-spacing: -0.02em;}
[data-testid="stSidebar"] {border-right: 1px solid #e9ecef;}
.estado {
    padding: 22px 24px; border-radius: 16px; border: 1px solid #b7dfc3;
    background: #f1fbf4; margin: 0.5rem 0 1.2rem 0;
}
.accion {
    padding: 18px 20px; border-radius: 14px; border: 1px solid #f0cf7a;
    background: #fff9e8; margin: 0.6rem 0;
}
.trabajo {
    padding: 16px 18px; border-radius: 14px; border: 1px solid #e5e7eb;
    background: #ffffff; margin: 0.5rem 0 1rem 0;
}
.muted {color: #667085;}
.kicker {font-size: 0.78rem; font-weight: 700; letter-spacing: .08em; color: #667085;}
</style>
""", unsafe_allow_html=True)

# Protección simple para la DEMO del portal cliente.
# Configure CLIENT_APP_PASSWORD en Streamlit Cloud > Settings > Secrets.
clave_cliente = st.secrets.get("CLIENT_APP_PASSWORD", "")
if clave_cliente:
    if "cliente_autorizado" not in st.session_state:
        st.session_state.cliente_autorizado = False
    if not st.session_state.cliente_autorizado:
        st.title("SITIO Farmacovigilancia")
        st.subheader("Acceso al portal")
        entrada = st.text_input("Contraseña", type="password", key="clave_cliente")
        if st.button("Entrar", type="primary"):
            if entrada == clave_cliente:
                st.session_state.cliente_autorizado = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta.")
        st.stop()
else:
    st.warning("DEMO PÚBLICA: no hay contraseña configurada. No use datos reales.")

# Datos 100% ficticios para la demo pública.
empresa = "Demo Pharma Paraguay S.A."
trabajos = [
    {
        "nombre": "Implementación de BPFV",
        "progreso": 82,
        "estado": "SITIO está trabajando",
        "detalle": "Estamos preparando la documentación para la presentación ante DINAVISA.",
        "siguiente": "Presentación y seguimiento ante DINAVISA",
        "necesita_cliente": False,
    },
    {
        "nombre": "PGR · GLUCOX 5 mg",
        "progreso": 54,
        "estado": "Esperando información",
        "detalle": "El borrador está en preparación.",
        "siguiente": "Completar revisión y pasar al RFV",
        "necesita_cliente": True,
    },
]
pendientes_rfv = [
    {"asunto": "PGR · GLUCOX 5 mg", "accion": "Revisar borrador preparado por SITIO"},
    {"asunto": "Caso FV-DEMO-004", "accion": "Confirmar evaluación final"},
]

st.sidebar.markdown("## 🛡️ SITIO")
st.sidebar.caption("Farmacovigilancia")
pagina = st.sidebar.radio(
    "Ir a",
    ["Inicio", "Mis trabajos", "Documentos", "Soporte al RFV", "Necesito ayuda"],
)
st.sidebar.divider()
st.sidebar.caption("DEMO PÚBLICA · Datos ficticios")

st.title("SITIO Farmacovigilancia")
st.caption(f"{empresa} · Plataforma y servicio gestionado")

if pagina == "Inicio":
    st.markdown(
        """
        <div class="estado">
          <div class="kicker">ESTADO DE FARMACOVIGILANCIA</div>
          <h2 style="margin:.25rem 0;">🟢 En regla</h2>
          <div>SITIO está gestionando su sistema de farmacovigilancia.</div>
          <div class="muted">Si necesitamos una decisión, documento o firma, aparecerá aquí.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Acciones pendientes", "1")
    col2.metric("Trabajos en curso", "2")
    col3.metric("Casos abiertos", "0")

    st.subheader("Necesitamos de usted")
    st.markdown(
        """
        <div class="accion">
          <b>🟠 GLUCOX 5 mg</b><br>
          Necesitamos la información de seguridad vigente para continuar el PGR.
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Resolver ahora", type="primary", use_container_width=True):
        st.info("En la versión conectada, aquí podrá subir el documento o responder directamente a SITIO.")

    st.subheader("Trabajos que SITIO está realizando")
    for t in trabajos:
        st.markdown(f'<div class="trabajo"><b>{t["nombre"]}</b><br><span class="muted">{t["estado"]}</span></div>', unsafe_allow_html=True)
        st.progress(t["progreso"] / 100, text=f'{t["progreso"]}% completado')
        st.write(t["detalle"])
        st.caption("Siguiente paso: " + t["siguiente"])

    st.subheader("Próximas obligaciones")
    st.dataframe(
        [
            {"Obligación": "Revisión del sistema BPFV", "Fecha": "14/11/2026", "Responsable": "SITIO"},
            {"Obligación": "Revisión PGR GLUCOX", "Fecha": "30/11/2026", "Responsable": "SITIO + RFV"},
        ],
        use_container_width=True,
        hide_index=True,
    )

    a, b = st.columns(2)
    with a:
        if st.button("⚠️ Me llegó una posible reacción adversa", use_container_width=True):
            st.session_state["ir_evento"] = True
    with b:
        if st.button("💬 Necesito ayuda de SITIO", use_container_width=True):
            st.session_state["ir_ayuda"] = True

    if st.session_state.get("ir_evento"):
        st.divider()
        st.subheader("Enviar posible reacción adversa")
        st.write("No necesita decidir si realmente es una reacción adversa. Envíenos lo que recibió.")
        st.text_area("Pegue aquí el WhatsApp, correo o descripción")
        st.file_uploader("O suba una captura, PDF o documento")
        if st.button("Enviar a SITIO", key="enviar_evento_inicio"):
            st.success("Demo: información recibida. En producción quedará registrada y llegará al equipo SITIO.")

    if st.session_state.get("ir_ayuda"):
        st.divider()
        st.subheader("¿Qué necesita?")
        st.selectbox(
            "Seleccione la opción más parecida",
            [
                "DINAVISA me pidió algo",
                "Quiero poner mi farmacovigilancia en regla",
                "Necesito registrar o incorporar un medicamento",
                "Necesito PGR / IPS / PSUR",
                "Necesito un estudio post-autorización",
                "No sé qué necesito",
            ],
        )
        st.text_area("Cuéntenos brevemente el problema")
        if st.button("Pedir ayuda a SITIO", key="ayuda_inicio"):
            st.success("Demo: solicitud enviada a SITIO.")

elif pagina == "Mis trabajos":
    st.header("Mis trabajos")
    st.write("Aquí ve únicamente lo que SITIO está haciendo para su empresa.")
    for t in trabajos:
        st.markdown(f'<div class="trabajo"><b>{t["nombre"]}</b><br><span class="muted">{t["estado"]}</span></div>', unsafe_allow_html=True)
        st.progress(t["progreso"] / 100, text=f'{t["progreso"]}%')
        st.write(t["detalle"])
        st.write("**Siguiente paso:**", t["siguiente"])
        if t["necesita_cliente"]:
            st.warning("Necesitamos información de su empresa para continuar.")

elif pagina == "Documentos":
    st.header("Documentos")
    st.write("Documentos y evidencias que SITIO ha preparado o puesto a disposición de su empresa.")
    st.dataframe(
        [
            {"Documento": "Expediente BPFV", "Estado": "En preparación", "Fecha": "—"},
            {"Documento": "PGR · GLUCOX 5 mg", "Estado": "Borrador", "Fecha": "25/09/2026"},
            {"Documento": "Resumen mensual de farmacovigilancia", "Estado": "Disponible", "Fecha": "31/08/2026"},
        ],
        use_container_width=True,
        hide_index=True,
    )
    st.caption("En producción, los documentos disponibles tendrán botón de descarga.")

elif pagina == "Soporte al RFV":
    st.header("Soporte al Responsable de Farmacovigilancia")
    st.write(
        "SITIO prepara el trabajo técnico. El RFV conserva el control y revisa, aprueba o firma cuando corresponde."
    )
    st.metric("Asuntos para revisar", len(pendientes_rfv))
    for p in pendientes_rfv:
        st.markdown(f'<div class="accion"><b>{p["asunto"]}</b><br>{p["accion"]}</div>', unsafe_allow_html=True)
        if st.button("Abrir para revisar", key=p["asunto"]):
            st.info("Demo: aquí aparecerán el documento, el resumen de SITIO y la acción requerida al RFV.")

elif pagina == "Necesito ayuda":
    st.header("Necesito ayuda de SITIO")
    opcion = st.selectbox(
        "¿Qué necesita?",
        [
            "DINAVISA me pidió algo",
            "Quiero poner mi farmacovigilancia en regla",
            "Necesito renovar o actualizar BPFV",
            "Quiero incorporar un medicamento",
            "Necesito PGR / IPS / PSUR",
            "Necesito un estudio post-autorización",
            "Me llegó una posible reacción adversa",
            "Necesito soporte para mi RFV",
            "No sé qué necesito",
        ],
    )
    st.text_area("Cuéntenos brevemente qué ha ocurrido o qué necesita")
    st.file_uploader("Adjuntar documento, correo, captura o PDF (opcional)")
    if st.button("Enviar a SITIO", type="primary"):
        st.success("Demo: solicitud enviada. SITIO la clasificará y le indicará el siguiente paso.")

st.divider()
st.caption("SITIO BioMedical Solutions · Demo pública con datos totalmente ficticios")
