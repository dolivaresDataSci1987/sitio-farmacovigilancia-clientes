# SITIO Farmacovigilancia · Clientes

Demo en Streamlit del portal para empresas farmacéuticas y sus Responsables de Farmacovigilancia (RFV).

## Objetivo
Que el cliente pueda responder rápidamente:
- ¿Estoy en regla?
- ¿Necesita SITIO algo de mí?
- ¿Qué está haciendo SITIO?
- ¿Qué debe revisar o aprobar mi RFV?
- ¿Cómo envío una posible reacción adversa o pido ayuda?

## Ejecutar
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Contraseña de demo
En Streamlit Cloud añada en **Settings > Secrets**:

```toml
CLIENT_APP_PASSWORD = "una-contraseña-larga"
```

La contraseña no debe guardarse en GitHub.

## Seguridad
Este repositorio es público y contiene exclusivamente código y datos ficticios. No subir secretos, credenciales, documentos reales, datos de pacientes ni información confidencial.

La contraseña simple es adecuada solo para la demo. La versión de producción requerirá autenticación real, aislamiento por cliente y controles de acceso antes de utilizar datos reales.
