# 📇 Contactos Web

Una aplicación web CRUD para gestionar contactos, desarrollada con **Flask** y **SQLite** usando **SQLAlchemy** como ORM.

---

## 📝 Descripción

Este proyecto permite al usuario **crear, leer, actualizar y eliminar contactos** desde una interfaz web sencilla.  
Es un ejercicio práctico para aplicar conocimientos de:
- Desarrollo web con Python
- Base de datos con SQLite gestionado por SQLAlchemy
- Formularios HTML
- Estilización básica con CSS y Bootstrap

---

## 🔧 Funcionalidades

- ✅ Agregar nuevos contactos con nombre, correo y teléfono.
- ✅ Listar todos los contactos registrados.
- ✅ Editar la información de un contacto existente.
- ✅ Eliminar contactos.
- ✅ Interfaz básica con HTML y CSS.

---

## 🛠 Tecnologías utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- SQLite
- HTML5 y CSS3
- Bootstrap (opcional)

---

## ▶️ Cómo ejecutar el proyecto en local

1. **Clona el repositorio**
```bash
git clone https://github.com/Arock900/contactos_web.git
cd contactos_web
Crea un entorno virtual (opcional pero recomendado)

bash
Copiar código
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instala las dependencias

bash
Copiar código
pip install -r requirements.txt
Ejecuta la aplicación

bash
Copiar código
python app.py
Abre el navegador en:

arduino
Copiar código
http://localhost:5000
🗄️ Configuración de la base de datos
El proyecto usa SQLAlchemy para la gestión de la base de datos.

El archivo de configuración crea automáticamente la base contactos.db si no existe.

No necesitas crear manualmente la base; se genera al iniciar el proyecto.

🚀 Despliegue en Render
Para desplegar el proyecto en Render:

Sube tu repositorio a GitHub.

Crea una nueva Web Service en Render.

Configura el Build Command:

nginx
Copiar código
pip install -r requirements.txt
Configura el Start Command:

nginx
Copiar código
gunicorn app:app
Asegúrate de que el archivo requirements.txt contenga:

nginx
Copiar código
Flask
SQLAlchemy
gunicorn
✅ Aquí puedes ver el proyecto desplegado en Render:
https://contactos-web-render.onrender.com

📁 Estructura del proyecto
cpp
Copiar código
contactos_web/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── edit.html
├── static/
│   └── styles.css
├── contactos.db
👨‍💻 Autor
Andrés Rojas

GitHub: https://github.com/Arock900


