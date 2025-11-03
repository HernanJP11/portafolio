from enum import Enum
import reflex as rx

# Constantes de diseño
MAX_WIDTH = "1100px"        # Ancho máximo del contenido
IMAGE_HEIGHT = "200px"     # Altura estándar para imágenes

# Tamaños en em (relativos al font-size)
class EmSize(Enum):
    DEFAULT = "1em"  # 16px - Tamaño base
    MEDIUM = "2em"   # 32px - Para títulos
    BIG = "4em"      # 64px - Para elementos destacados

# Tamaños en sistema de Reflex (8px = 1 unidad)
class Size(Enum):
    ZERO = "0"       # 0px - Sin espacio
    SMALL = "2"      # 8px - Espaciado pequeño
    DEFAULT = "4"    # 16px - Espaciado normal
    MEDIUM = "6"     # 32px - Espaciado medio
    BIG = "8"        # 48px - Espaciado grande
    BIG_2 = "9"
    
    
    
# Hojas de estilo externas
STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"  # Íconos de tecnologías
]

# Estilos base aplicados globalmente
BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer"  # Cursor pointer en todos los botones
    }
}