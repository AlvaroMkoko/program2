import pygame
from player import Player
from piece import Piece 

# Inicializar pygame
pygame.init()

# Diccionario de estados
estados = {
    1:(0,0), 2:(0,1), 3:(0,2), 4:(0,3),
    5:(1,0), 6:(1,1), 7:(1,2), 8:(1,3),
    9:(2,0), 10:(2,1), 11:(2,2), 12:(2,3),
    13:(3,0), 14:(3,1), 15:(3,2), 16:(3,3)
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
selected_index = 0

def draw_board(win, pieces):
    """Dibuja el tablero de ajedrez con imágenes y las piezas"""
    for row in range(ROWS):
        for col in range(COLS):
            image = white_square if (row + col) % 2 == 0 else red_square
            win.blit(image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

    # Dibujar las piezas
    for piece in pieces:
        piece.draw(win)

def state_movement(estado):
    global selected_index
    if estado in estados:
        coordenada = estados[estado]
        pieces[selected_index].x = coordenada[1]
        pieces[selected_index].y = coordenada[0]


def change_piece(index):
    global selected_index
    if 0 <= index < len(pieces):
        selected_index = index

def main():
    """Bucle principal del juego"""
    running = True
    estado_actual = 0
    ficha_actual = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ficha_actual = (ficha_actual + 1) % len(pieces)
        change_piece(ficha_actual)

        estado_actual = (estado_actual % len(estados)) + 1
        state_movement(estado_actual)


        draw_board(win, pieces)
        pygame.display.flip()

        pygame.time.delay(400)

    pygame.quit()

if __name__ == "__main__":
    main()
