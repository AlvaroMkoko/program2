import pygame

# Definir constantes
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 4, 4
SQUARE_SIZE = WIDTH // COLS

class Piece:
    def __init__(self, color, type, x, y):
        self.color = color  # "white" o "black"
        self.type = type    # Tipo de pieza (peón, torre, caballo, etc.)
        self.x = x          # Coordenada X (columna)
        self.y = y          # Coordenada Y (fila)
        self.image = self.load_image()  # Cargar la imagen de la pieza

    def load_image(self):
        """Carga la imagen según el tipo y color de la pieza"""
        piece_name = f"{self.type}_{self.color}.png"
        return pygame.image.load(f"img/{piece_name}")

    def draw(self, win):
        """Dibuja la pieza en su posición actual"""
        win.blit(pygame.transform.scale(self.image, (SQUARE_SIZE, SQUARE_SIZE)), (self.x * SQUARE_SIZE, self.y * SQUARE_SIZE))

    def __str__(self):
        return f"{self.color.capitalize()} {self.type.capitalize()} at ({self.x}, {self.y})"
    
    def move(self, x ,y):
        self.x = x
        self.y = y
