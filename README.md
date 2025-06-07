# 📋 TaskMaster - Ejemplo de Despliegue Flask
![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![Python](https://img.shields.io/badge/Python-3.13+-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple)
![Deploy](https://img.shields.io/badge/Deploy-Render.com-blueviolet)
## Video del aplicativo



https://github.com/user-attachments/assets/bf058dc8-aec2-43be-8f7f-0ffb2a427320




## Vista en celular
![image](https://github.com/user-attachments/assets/ecad070b-f704-4b33-96f0-d5351f27d506)



**Aplicación de ejemplo** para demostrar cómo crear y desplegar una aplicación Flask básica en Render.com. Incluye gestión simple de tareas con una interfaz moderna usando Bootstrap.


## 🎯 Propósito del Ejemplo

Este proyecto demuestra:
- 📁 **Estructura básica** de una aplicación Flask
- 🌐 **Templates con Jinja2** y herencia de plantillas
- 🎨 **Integración con Bootstrap** para interfaces modernas
- ⚡ **Despliegue automático** en Render.com
- 🔧 **Configuración** con `render.yaml`

## 🖥️ Funcionalidades de la Demo

- **CRUD básico**: Crear, leer y eliminar tareas (sin base de datos)
- **Templates organizados**: Base template con navegación
- **Mensajes flash**: Confirmaciones y notificaciones
- **Diseño responsive**: Compatible con móviles y desktop

## 🚀 Instalación y Prueba Local

### Prerrequisitos
- Python 3.13 o superior
- pip (gestor de paquetes de Python)

### Ejecutar el ejemplo

1. **Descarga los archivos del proyecto**
   
2. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación**
   ```bash
   python app.py
   ```

4. **Ve el resultado**
   ```
   http://localhost:5000
   ```

## 🌐 Despliegue en Render.com

### Método automático (Recomendado)

1. **Sube tu código a GitHub**
2. **Conecta con Render**:
   - Ve a [render.com](https://render.com)
   - Crea una cuenta gratuita
   - Haz clic en "New +" → "Web Service"
   - Conecta tu repositorio de GitHub

3. **Configuración automática**:
   - Render detectará el archivo `render.yaml`
   - Se configurará automáticamente
   - ¡Tu app estará en línea en minutos!

### Variables de entorno importantes

- `SECRET_KEY`: Clave secreta para Flask (se genera automáticamente en Render)
- `PORT`: Puerto de la aplicación (configurado automáticamente por Render)

## 📁 Estructura del Proyecto

```
flask-render-example/
├── app.py              # Aplicación principal Flask
├── requirements.txt    # Dependencias de Python
├── render.yaml        # Configuración para Render.com
├── README.md          # Este archivo
└── templates/         # Plantillas HTML
    ├── base.html      # Plantilla base con navegación
    ├── index.html     # Página principal
    ├── agregar.html   # Formulario para nuevas tareas
    └── about.html     # Información de la aplicación
```

## 🛠️ Stack Tecnológico

- **Backend**: Flask 3.1.1 (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.0
- **Iconos**: Font Awesome 6.4.0
- **Servidor**: Gunicorn (producción)
- **Despliegue**: Render.com
