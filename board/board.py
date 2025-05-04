import pygame
from constants import WHITE,BLACK,SQUARE_SIZE,WIDTH,HEIGHT,SCALE,HIGHLIGHT_COLOR
from pieces import Empty,King,Rook,Pawn
from utils import eval_pos
from setup_board import board
from moves import make_move

pygame.init()



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard with Pieces")


try:
    white_pawn = pygame.image.load("assets/wP.png").convert_alpha()
    white_rook = pygame.image.load("assets/wR.png").convert_alpha()
    white_knight = pygame.image.load("assets/wN.png").convert_alpha()
    white_bishop = pygame.image.load("assets/wB.png").convert_alpha()
    white_queen = pygame.image.load("assets/wQ.png").convert_alpha()
    white_king = pygame.image.load("assets/wK.png").convert_alpha()

    black_pawn = pygame.image.load("assets/bP.png").convert_alpha()
    black_rook = pygame.image.load("assets/bR.png").convert_alpha()
    black_knight = pygame.image.load("assets/bN.png").convert_alpha()
    black_bishop = pygame.image.load("assets/bB.png").convert_alpha()
    black_queen = pygame.image.load("assets/bQ.png").convert_alpha()
    black_king = pygame.image.load("assets/bK.png").convert_alpha()
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    exit()


  
white_pawn = pygame.transform.scale(white_pawn, (SCALE, SCALE))
white_rook = pygame.transform.scale(white_rook, (SCALE, SCALE))
white_knight = pygame.transform.scale(white_knight, (SCALE, SCALE))
white_bishop = pygame.transform.scale(white_bishop, (SCALE, SCALE))
white_queen = pygame.transform.scale(white_queen, (SCALE, SCALE))
white_king = pygame.transform.scale(white_king, (SCALE, SCALE))

black_pawn = pygame.transform.scale(black_pawn, (SCALE, SCALE))
black_rook = pygame.transform.scale(black_rook, (SCALE, SCALE))
black_knight = pygame.transform.scale(black_knight, (SCALE, SCALE))
black_bishop = pygame.transform.scale(black_bishop, (SCALE, SCALE))
black_queen = pygame.transform.scale(black_queen, (SCALE, SCALE))
black_king = pygame.transform.scale(black_king, (SCALE, SCALE))


piece_images = {
    "wP": white_pawn, "wR": white_rook, "wN": white_knight, "wB": white_bishop, "wQ": white_queen, "wK": white_king,
    "bP": black_pawn, "bR": black_rook, "bN": black_knight, "bB": black_bishop, "bQ": black_queen, "bK": black_king,
}

running = True
selected=None
to_pos=""
empty_pos=""
turn="w"
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

 
            turn = make_move(to_pos,turn,selected,board)
            

            pos=pygame.mouse.get_pos()
            pos=eval_pos(pos)
            selected=board[pos[0]][pos[1]]
            print(selected.pos)
            
            to_pos=None
    if type(selected) in [Rook,King]:
            
            if type(selected)==King:
                if selected.pos not in [(0,4),(7,4)]:
                    selected.moved=True
            if type(selected)==Rook:
                if selected.pos not in [(0,0),(7,0),(0,7),(7,7)]:
                    selected.moved=True
    


           

    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


            if (selected!=None) and ((row, col) in selected.valid_moves()) :
                center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
                center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

            piece = board[row][col]
            if type(piece) != Empty:
                image = piece_images[str(piece)]
                piece_x = col * SQUARE_SIZE + (SQUARE_SIZE - image.get_width()) // 2
                piece_y = row * SQUARE_SIZE + (SQUARE_SIZE - image.get_height()) // 2
                screen.blit(image, (piece_x, piece_y))

    pygame.display.flip()

pygame.quit()
