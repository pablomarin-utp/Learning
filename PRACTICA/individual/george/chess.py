# Caracteres para las piezas de ajedrez
# Blancas: ♔ ♕ ♖ ♗ ♘ ♙ 
# Negras: ♚ ♛ ♜ ♝ ♞ ♟

class Chess():
    def __init__():
        pass

class Piece():
    def __init__(self, type, team, position, symbol):
        self.type = type
        self.team = team
        self.position = position
        self.symbol = symbol
    
    def movements(self):
        raise NotImplementedError("manito las fichas tienen que tener movimientos")

class King(Piece):
    def __init__(self, team, position, symbol):
        super().__init__("King", team, position, symbol)
        self.moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def move(self, x, y):
        if (x, y) in self.moves:
            self.position[0] += x
            self.position[1] += y
        else:
            print("No valid movement")

class Pawn(Piece):
    def __init__(self, team, position, symbol):
        super().__init__("Pawn", team, position, symbol)
        self.moves = [(0,1),(1,1),(-1,1)]

    def move(self, x, y):
        if (x, y) in self.moves:
            self.position[0] += x
            self.position[1] += y
        else:
            print("No valid movement")

class Rook(Piece):
    def __init__(self, team, position, symbol):
        super().__init__("Rook", team, position, symbol)
        self.moves = [(x, 0) for x in range(-7, 8) if x != 0] + [(0, y) for y in range(-7, 8) if y != 0]

    def move(self, x, y):
        if (x, y) in self.moves:
            self.position[0] += x
            self.position[1] += y
        else:
            print("No valid movement")

class Bishop(Piece):
    def __init__(self, team, position, symbol):
        super().__init__("Bishop", team, position, symbol)
        self.moves = [(x, x) for x in range(-7, 8) if x != 0] + [(x, -x) for x in range(-7, 8) if x != 0]

    def move(self, x, y):
        if (x, y) in self.moves:
            self.position[0] += x
            self.position[1] += y
        else:
            print("No valid movement")

class Knight(Piece):
    def __init__(self, team, position, symbol):
        super().__init__("Knight", team, position, symbol)
        self.moves = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]

    def move(self, x, y):
        if (x, y) in self.moves:
            self.position[0] += x
            self.position[1] += y
        else:
            print("No valid movement")

class Queen(Piece):
    def __init__(self, team, position, symbol):
        super().__init__("Queen", team, position, symbol)
        self.moves = [(x, 0) for x in range(-7, 8) if x != 0] + [(0, y) for y in range(-7, 8) if y != 0] + [(x, x) for x in range(-7, 8) if x != 0] + [(x, -x) for x in range(-7, 8) if x != 0]

    def move(self, x, y):
        if (x, y) in self.moves:
            self.position[0] += x
            self.position[1] += y
        else:
            print("No valid movement")

class Board():
    def __init__(self):
        self.board = [
            [Rook("white", (0, 7), "♖"), Knight("white", (1, 7), "♘"), Bishop("white", (2, 7), "♗"), Queen("white", (3, 7), "♕"), King("white", (4, 7), "♔"), Bishop("white", (5, 7), "♗"), Knight("white", (6, 7), "♘"), Rook("white", (7, 7), "♖")],
            [Pawn("white", (0, 6), "♙"), Pawn("white", (1, 6), "♙"), Pawn("white", (2, 6), "♙"), Pawn("white", (3, 6), "♙"), Pawn("white", (4, 6), "♙"), Pawn("white", (5, 6), "♙"), Pawn("white", (6, 6), "♙"), Pawn("white", (7, 6), "♙")],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [Pawn("black", (0, 1), "♟"), Pawn("black", (1, 1), "♟"), Pawn("black", (2, 1), "♟"), Pawn("black", (3, 1), "♟"), Pawn("black", (4, 1), "♟"), Pawn("black", (5, 1), "♟"), Pawn("black", (6, 1), "♟"), Pawn("black", (7, 1), "♟")],
            [Rook("black", (0, 0), "♜"), Knight("black", (1, 0), "♞"), Bishop("black", (2, 0), "♝"), Queen("black", (3, 0), "♛"), King("black", (4, 0), "♚"), Bishop("black", (5, 0), "♝"), Knight("black", (6, 0), "♞"), Rook("black", (7, 0), "♜")]
        ]
    def show_board(self):
        board = self.board
        print("    A   B   C   D   E   F   G   H")
        print("  +---+---+---+---+---+---+---+---+")
        for i, row in enumerate(board):
            print(f"{8-i} |", end="")
            for piece in row:
                if piece == 0:
                    print("   |", end="")
                elif piece == 1:
                    print(" ■ |", end="")
                else:
                    print(f" {piece.symbol} |", end="")                
            print(f" {8-i}")
            print("  +---+---+---+---+---+---+---+---+")
        print("    A   B   C   D   E   F   G   H")

tablero = Board()
tablero.show_board()
