import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")
font = pygame.font.SysFont('freesansbold.ttf', 20)
big_font = pygame.font.SysFont('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
# game variables

white_pieces = ["King", "Queen", "Rook", "Bishop", "Knight", 
                "Rook", "Bishop", "Knight", 
                "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ["King", "Queen", "Rook", "Bishop", "Knight", 
                "Rook", "Bishop", "Knight", 
                "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn", "Pawn"]
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_white = []
captured_black = []

#0=white, 1=white moves, 2=black, 3=black moves
turn_step = 0
selection = 100


# load in images
white_king = pygame.image.load("Chess/Chess/Assets/whiteking.png")
white_queen = pygame.image.load("Chess/Chess/Assets/white queen.png")
white_rook = pygame.image.load("Chess/Chess/Assets/white rook.png")
white_bishop = pygame.image.load("Chess/Chess/Assets/white bishop.png")
white_knight = pygame.image.load("Chess/Chess/Assets/white knight.png")
white_pawn = pygame.image.load("Chess/Chess/Assets/white pawn.png")
black_king = pygame.image.load("Chess/Chess/Assets/black king.png")
black_queen = pygame.image.load("Chess/Chess/Assets/black queen.png")
black_rook = pygame.image.load("Chess/Chess/Assets/black rook.png")
black_bishop = pygame.image.load("Chess/Chess/Assets/black bishop.png")
black_knight = pygame.image.load("Chess/Chess/Assets/black knight.png")
black_pawn = pygame.image.load("Chess/Chess/Assets/black pawn.png")

# scale images
white_king = pygame.transform.scale(white_king, (80, 80))
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
black_king = pygame.transform.scale(black_king, (80, 80))
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_pawn = pygame.transform.scale(black_pawn, (65, 65))

white_king_discard = pygame.transform.scale(white_king, (45, 45))
white_queen_discard = pygame.transform.scale(white_queen, (45, 45))
white_rook_discard = pygame.transform.scale(white_rook, (45, 45))
white_bishop_discard = pygame.transform.scale(white_bishop, (45, 45))
white_knight_discard = pygame.transform.scale(white_knight, (45, 45))
white_pawn_discard = pygame.transform.scale(white_pawn, (45, 45))
black_king_discard = pygame.transform.scale(black_king, (45, 45))
black_queen_discard = pygame.transform.scale(black_queen, (45, 45))
black_rook_discard = pygame.transform.scale(black_rook, (45, 45))
black_bishop_discard = pygame.transform.scale(black_bishop, (45, 45))
black_knight_discard = pygame.transform.scale(black_knight, (45, 45))
black_pawn_discard = pygame.transform.scale(black_pawn, (45, 45))

white_images = [white_king, white_queen, white_rook, white_bishop, white_knight, white_pawn]
black_images = [black_king, black_queen, black_rook, black_bishop, black_knight, black_pawn]
white_discard_images = [white_king_discard, white_queen_discard, white_rook_discard, white_bishop_discard, white_knight_discard, white_pawn_discard]
black_discard_images = [black_king_discard, black_queen_discard, black_rook_discard, black_bishop_discard, black_knight_discard, black_pawn_discard]

piece_list = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']

#draw Main Game Board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, "light gray", [600 - (column * 200), row*100, 100, 100])
        else:
            pygame.draw.rect(screen, "light gray", [700 - (column * 200), row*100, 100, 100])
        pygame.draw.rect(screen, 'gray', [800, 0, 200, HEIGHT])
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        
        status_text = ['White! Select A Soldier, Priest Or Royalty To Send Out!', 'White! Give Them A Command!',
                        'Black! Select A Soldier, Priest Or Royalty To Send Out!', 'Black! Give Them A Command!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (10, 820))

        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)


def def_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == "Pawn":
            screen.blit()

# Main Game Loop

run=True
while run:
    timer.tick(fps)
    screen.fill("black")
    draw_board()
    draw_pieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()