# 🍔 PediloDespues - Sistema de Pedidos

> Trabajo práctico — Facultad de Ingeniería (UBA)  
> Introducción al Desarrollo de Software · Cátedra Lanzillotta

---

## 📌 Descripción

**PediloDespues** es una plataforma de pedidos full stack que permite a los usuarios realizar compras online, generar un ticket con ID de seguimiento, consultar el estado del pedido en tiempo real y utilizar promociones mediante códigos QR.

El sistema está compuesto por:

| Módulo | Tecnología |
|---|---|
| 🌐 Frontend Web | Flask + HTML/CSS/JS |
| ⚙️ Backend API | Flask + MySQL |
| 📱 App Móvil | Kivy |
| 🗄️ Base de datos | MySQL |

---

## 🏗️ Arquitectura

```
Frontend Web  ──┐
                ├──▶  API Flask (puerto 5001)  ──▶  MySQL
App Kivy      ──┘
```

---

## 🚀 Tecnologías

### Frontend Web
- Python · Flask · Jinja2
- HTML / CSS / JavaScript
- LocalStorage (carrito de compras)

### Backend
- Python · Flask
- MySQL · SQLAlchemy / MySQL Connector

### App móvil
- Python · Kivy

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/pedilo-despues.git
cd pedilo-despues
```

### 2. Instalar dependencias

Cada módulo tiene su propio entorno virtual y su propio `requirements.txt`. Se recomienda crear un `.venv` por separado en cada carpeta para aislar las dependencias.

```bash
# Ejemplo para el backend (repetir lo mismo en frontend-web y app-mobile-kivy)
cd backend
python -m venv .venv

# Activar el entorno virtual:
# En Windows:
.venv\Scripts\activate
# En macOS/Linux:
source .venv/bin/activate

# Instalar dependencias del módulo:
pip install -r requirements.txt
```

> 💡 Recordá activar el `.venv` correspondiente cada vez que vayas a levantar un módulo.

---

## 🗄️ Base de datos

**Configuración MySQL requerida:**

| Parámetro | Valor |
|---|---|
| Usuario | `root` |
| Contraseña | `12345678` |
| Base de datos | `proyecto` |

> ⚠️ Se recomienda cambiar las credenciales antes de desplegar en un entorno no local.

### Opción A — Crear tablas con script

```bash
python crear_base.py
```

### Opción B — Importar SQL

```bash
mysql -u root -p proyecto < database/base_datos.sql
```

### Cargar datos iniciales

Una vez levantado el backend, ejecutar:

```
GET /cargardatos
```

---

## ▶️ Ejecución

### 1. Backend (API)

```bash
cd backend
python app.py
# Escucha en http://localhost:5001
```

### 2. Frontend Web

```bash
cd frontend-web
python app.py
# Escucha en http://localhost:5000
```

### 3. App móvil (Kivy)

```bash
cd app-mobile-kivy
python main.py
```

---

## 🔗 Endpoints principales

### Productos

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/productos` | Lista todos los productos disponibles |

### Tickets

| Método | Ruta | Descripción |
|---|---|---|
| `POST` | `/ticket` | Crea un nuevo pedido y genera un ticket |
| `GET` | `/ticket/<id>` | Obtiene los detalles de un ticket |
| `GET` | `/ticket/<id>/estado` | Consulta el estado actual del pedido |
| `PUT` | `/ticket` | Actualiza el estado de un ticket |

### QR / Promociones

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/qr` | Genera o valida un código QR de promoción |

---

## 🎯 Funcionalidades

- 🛒 Carrito de compras persistido con LocalStorage
- 🎫 Generación de ticket con ID de seguimiento único
- 📡 Consulta de estado del pedido en tiempo real
- 🔄 Actualización de estados por el administrador
- 📲 App móvil para tracking de pedidos
- 🏷️ Promociones mediante códigos QR

---

## 👥 Integrantes

| Nombre |
|---|
| Juan Valentín Marcos |
| Leonel Rodrigo Rolón |
| Iván Poggio |
| Angela Alcon |
| Karel Leire Luna García |
| Agustín Beltrame |
| Jordan Ticona |
