import pygame
# from pieces import Piece
from constants import *

pygame.init()

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



