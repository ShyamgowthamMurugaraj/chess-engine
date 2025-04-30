from setup_board import board
from pieces import Empty,King
import pygame
from utils import eval_pos




def make_move(to_pos,turn,selected,board,empty_pos=None):

    if to_pos==None:
        to_pos=pygame.mouse.get_pos()
        to_pos=eval_pos(to_pos)
        if to_pos in selected.valid_moves() and turn==selected.color:
            empty_pos=selected.pos
            board[empty_pos[0]][empty_pos[1]]=Empty(empty_pos)
            selected.pos=to_pos
            board[to_pos[0]][to_pos[1]] = selected
            to_pos=None
            turn=~selected

    pos=pygame.mouse.get_pos()
    pos=eval_pos(pos)
    selected=board[pos[0]][pos[1]]
    to_pos=None
    
    

    return turn


 
    
                        


                    


   