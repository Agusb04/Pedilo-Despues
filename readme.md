# 🍔 PediloDespues

> Plataforma de pedidos online con seguimiento en tiempo real, app móvil y promociones por QR.

**Trabajo Práctico · Facultad de Ingeniería (UBA)**  
Introducción al Desarrollo de Software · Cátedra Lanzillotta

---

## 👥 Integrantes

| Nombre |
|--------|
| Juan Valentín Marcos |
| Leonel Rodrigo Rolón |
| Iván Poggio |
| Angela Alcon |
| Karel Leire Luna García |
| Agustín Beltrame |
| Jordan Ticona |

---

## 📌 Descripción

PediloDespues es una plataforma de pedidos full stack que permite a los usuarios realizar compras online, generar un ticket con ID de seguimiento, consultar el estado del pedido en tiempo real y utilizar promociones mediante códigos QR.

El sistema está diseñado con interfaz responsive, adaptándose automáticamente según el dispositivo utilizado (navegador de escritorio o móvil).

---

## 🏗️ Arquitectura

```
Frontend Web  (puerto 5000) ──┐
                              ├──▶  API Flask (puerto 5001)  ──▶  MySQL
App Kivy                    ──┘
```

| Módulo | Tecnología |
|--------|------------|
| 🌐 Frontend Web | Flask + HTML/CSS/JS |
| ⚙️ Backend API | Flask + MySQL |
| 📱 App Móvil | Kivy |
| 🗄️ Base de datos | MySQL |

---

## 🚀 Tecnologías

**Frontend Web**
- Python · Flask · Jinja2
- HTML / CSS / JavaScript
- LocalStorage (carrito de compras)
- Diseño responsive (desktop + mobile)

**Backend**
- Python · Flask
- MySQL · SQLAlchemy / MySQL Connector

**App móvil**
- Python · Kivy

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/pedilo-despues.git
cd pedilo-despues
```

### 2. Instalar dependencias

Cada módulo tiene su propio entorno virtual y su propio `requirements.txt`. Se recomienda crear un `.venv` por separado en cada carpeta.

```bash
cd backend
python -m venv .venv

# Activar entorno:
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

Repetir el proceso para `frontend-web` y `app-mobile-kivy`.

---

## 🗄️ Base de datos

| Parámetro | Valor |
|-----------|-------|
| Usuario | `root` |
| Contraseña | `12345678` |
| Base de datos | `proyecto` |

Crear las tablas ejecutando:

```bash
python crear_base.py
```

O importar desde el archivo SQL:

```bash
mysql -u root -p proyecto < database/base_datos.sql
```

---

## ▶️ Ejecución

**Backend** (puerto 5001)

```bash
cd backend
python app.py
```

**Frontend Web** (puerto 5000)

```bash
cd frontend-web
python app.py
```

**App móvil**

```bash
cd app-mobile-kivy
python main.py
```

---

## 🎯 Funcionalidades

- 🛒 Carrito de compras persistente
- 🎫 Tickets con ID único de seguimiento
- 📡 Estado del pedido en tiempo real
- 🔄 Panel de administración de pedidos
- 📲 App móvil para tracking
- 🏷️ Promociones con QR
- 📱💻 Interfaz responsive (mobile + desktop)