# SITIO-SurveillanceHelper · Portal del cliente

Demo pública de **SITIO-SurveillanceHelper**, plataforma y servicio gestionado de farmacovigilancia de SITIO BioMedical Solutions.

## Qué demuestra
- Estado regulatorio y BPFV.
- Trabajo que SITIO realiza por el cliente.
- Soporte al Responsable de Farmacovigilancia (RFV).
- Casos y seguimiento.
- Documentos y evidencias.
- Solicitud de servicios.
- Canal compartible para que visitadores, colaboradores o profesionales reporten información de seguridad en texto libre.

## Canal de seguridad
La misma aplicación muestra un formulario simplificado si se abre con:

```
https://TU-APP.streamlit.app/?canal=demo-pharma
```

En producción cada cliente tendrá un enlace/QR propio.

## Secrets de la demo
En Streamlit Cloud > Settings > Secrets:

```toml
CLIENT_APP_PASSWORD = "una-contraseña-larga"
PUBLIC_APP_URL = "https://TU-APP.streamlit.app"
```

## Ejecutar localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Seguridad
Repositorio público + datos ficticios. No subir secretos, datos de pacientes, documentos regulatorios reales ni información confidencial. La contraseña simple es solo para demostración.
