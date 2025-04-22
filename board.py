import pygame

pygame.init()

WHITE=(238,238,210)
BLACK=(118,150,86)

SQUARE_WIDTH=80

WIDTH=8*SQUARE_WIDTH
HEIGHT=8*SQUARE_WIDTH

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("COOL CHESS BOARD")

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    for row in range(8):
        for col in range(8):
            color = WHITE if (row+col)%2==0 else BLACK
            pygame.draw.rect(screen,color,(col*SQUARE_WIDTH,row*SQUARE_WIDTH,SQUARE_WIDTH,SQUARE_WIDTH))
    pygame.display.flip()

pygame.quit()

class Piece:
    def __init__(self,color,p_type):
        self.p_type=p_type
        self.color=color
    def __repr__(self):
        return f"{self.color}{self.p_type}"
    def valid_moves(self,pos,board):
        if self.p_type=="p":
            


board=[
       ["-","-","-","-","-","-","-","-"],
       ["-","-","-","-","-","-","-","-"],
       ["-","-","-","-","-","-","-","-"],
       ["-","-","-","-","-","-","-","-"],
       ["-","-","-","-","-","-","-","-"],
       ["-","-","-","-","-","-","-","-"],
       ["-","-","-","-","-","-","-","-"],
       ["-","-","-","-","-","-","-","-"]
       ]

piece_index=["R","N","B","Q","K","B","N","R"]


for i,j in enumerate(board[0]):
    board[0][i]=Piece("b",piece_index[i])
for i,j in enumerate(board[7]):
    board[7][i]=Piece("w",piece_index[i])


board[1]=[Piece("b","P") for _ in range(8)]
board[6]=[Piece("w","P") for _ in range(8)]


for i in board:
    print(i)