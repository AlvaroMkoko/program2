class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color  # "white" o "black"
        self.pieces = []  # Aquí puedes almacenar las piezas del jugador

    def add_piece(self, piece):
        """Agrega una pieza a la lista de piezas del jugador"""
        self.pieces.append(piece)

    def remove_piece(self, piece):
        """Elimina una pieza cuando es capturada"""
        if piece in self.pieces:
            self.pieces.remove(piece)

    def __str__(self):
        return f"Jugador {self.name} ({self.color})"
