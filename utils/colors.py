from kivy.utils import get_color_from_hex

# Tema renkleri
COLORS = {
    'background': '#1E1E1E',  # Koyu gri
    'surface': '#2D2D2D',     # Biraz daha açık gri
    'primary': '#007ACC',     # Mavi
    'secondary': '#3E3E3E',   # Orta gri
    'text': '#FFFFFF',        # Beyaz
    'text_secondary': '#BEBEBE',  # Gainsboro
    'accent': '#00B7C3',      # Turkuaz
    'error': '#FF5555',       # Kırmızı
    'success': '#50FA7B'      # Yeşil
}

def get_color(color_name):
    return get_color_from_hex(COLORS[color_name]) 