# ⛽ GasofaBot - Bot de Telegram para Gasolineras

Bot de Telegram que encuentra las gasolineras más baratas cerca de tu ubicación utilizando datos oficiales del Ministerio de Transportes de España.

## 🚀 Características

- **📍 Búsqueda por ubicación**: Envía tu ubicación y encuentra gasolineras cercanas
- **📏 Radio personalizable**: Elige la distancia máxima de búsqueda (5km a 25km+)
- **⛽ Múltiples carburantes**: Gasolina 95, Gasolina 98 y Diésel
- **💰 Precios actualizados**: Datos oficiales en tiempo real
- **🗺️ Enlaces a Maps**: Dirección directa a Google Maps
- **⚡ Respuesta rápida**: Sistema de cache inteligente
- **🎯 Interfaz intuitiva**: Menús interactivos y teclados personalizados

## 🛠️ Tecnologías

- **Python 3.12** - Lenguaje principal
- **python-telegram-bot** - Framework de bots de Telegram
- **Flask** - Servidor web para mantener el bot activo
- **Requests** - Peticiones HTTP a la API
- **Haversine Formula** - Cálculo de distancias geográficas

## 📦 Instalación

1. **Clona el repositorio**:
```bash
git clone https://github.com/tuusuario/gasofabot.git
cd gasofabot
```

2. **Instala dependencias**:
```bash
pip install -r requirements.txt
```

3. **Configura las variables de entorno**:
```bash
nano config.py
# Edita config.py con tu TOKEN de Telegram y la API
```

## 🚀 Deployment

Coming soon...