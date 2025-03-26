import pygame
from player import Player
from piece import Piece 

# Inicializar pygame
pygame.init()

# Diccionario de estados
estados = {
    1:(0,0), 2:(0,1), 3:(0,2), 4:(0,3),
    5:(0,0), 6:(0,1), 7:(0,2), 8:(0,3),
    1:(0,0), 2:(0,1), 3:(0,2), 4:(0,3),
    1:(0,0), 2:(0,1), 3:(0,2), 4:(0,3)
           }

# Definir constantes
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 4, 4
SQUARE_SIZE = WIDTH // COLS

# Cargar imágenes
white_square = pygame.image.load("img/white.png")  # Imagen para casillas blancas
red_square = pygame.image.load("img/red.png")  # Imagen para casillas negras

# Escalar imágenes al tamaño de cada casilla
white_square = pygame.transform.scale(white_square, (SQUARE_SIZE, SQUARE_SIZE))
red_square = pygame.transform.scale(red_square, (SQUARE_SIZE, SQUARE_SIZE))

# Crear la ventana
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tablero de Ajedrez con Imágenes")

# Crear jugadores
player1 = Player("Jugador 1", "white")
player2 = Player("Jugador 2", "black")

# Crear las piezas
def create_pieces():
    pieces = []
    # Pieza blancas
    pieces.append(Piece("white", "king", 0,0))
    # Pieza negras
    pieces.append(Piece("black", "king", 1, 0))
    
    return pieces

# Crear las piezas del juego
pieces = create_pieces()
selected_piece = None

def draw_board(win, pieces):
    """Dibuja el tablero de ajedrez con imágenes y las piezas"""
    for row in range(ROWS):
        for col in range(COLS):
            image = white_square if (row + col) % 2 == 0 else red_square
            win.blit(image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

    # Dibujar las piezas
    for piece in pieces:
        piece.draw(win)

def handle_key_movement(event):
    """Mueve la pieza seleccionada con las teclas de flecha"""
    global selected_piece
    if selected_piece:
        if event.key == pygame.K_LEFT and selected_piece.x > 0:
            selected_piece.x -= 1
        elif event.key == pygame.K_RIGHT and selected_piece.x < COLS - 1:
            selected_piece.x += 1
        elif event.key == pygame.K_UP and selected_piece.y > 0:
            selected_piece.y -= 1
        elif event.key == pygame.K_DOWN and selected_piece.y < ROWS - 1:
            selected_piece.y += 1
        elif event.key == pygame.K_RETURN:
            selected_piece = None  # Deseleccionar la pieza

def array_movement(array):
    global selected_piece
    if selected_piece:


def handle_mouse_click(pos):
    """Selecciona una pieza con el mouse"""
    global selected_piece
    x, y = pos
    col, row = x // SQUARE_SIZE, y // SQUARE_SIZE  # Convertir a coordenadas de tablero
    for piece in pieces:
        if piece.x == col and piece.y == row:
            selected_piece = piece
            break

def main():
    """Bucle principal del juego"""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(pygame.mouse.get_pos())

            elif event.type == pygame.KEYDOWN:
                handle_key_movement(event)

        draw_board(win, pieces)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
