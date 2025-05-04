
from pieces import Empty,King,Pawn
import pygame
from utils import eval_pos

move_counter=0




def make_move(to_pos,turn,selected,board,empty_pos=None):
    global move_counter
    
    if to_pos==None:
        to_pos=pygame.mouse.get_pos()
        to_pos=eval_pos(to_pos)
        
        if type(selected)==King and to_pos==(selected.pos[0],selected.pos[1]+2) and selected.color==turn:
            selected.king_castled=True
        if type(selected)==King and to_pos==(selected.pos[0],selected.pos[1]-2) and selected.color==turn:
            selected.queen_castled=True
        
        
        if type(selected) == Pawn and abs(to_pos[0]-selected.pos[0])==2 and selected.color == turn:
            selected.just_moved_two = True
            selected.move_moved_2=move_counter



        if to_pos in selected.valid_moves() and turn==selected.color:
            
            empty_pos=selected.pos
            board[empty_pos[0]][empty_pos[1]]=Empty(empty_pos,board)
            old_pos=selected.pos
            selected.pos=to_pos
            board[to_pos[0]][to_pos[1]] = selected
            if type(selected) == Pawn and selected.color == turn:
                if to_pos==(old_pos[0]-1,old_pos[1]-1) and board[old_pos[0]][old_pos[1]-1].move_moved_2==move_counter-1:
                    selected.en_passanted=True 
                    selected.en_passantobe=(old_pos[0],old_pos[1]-1)
            if type(selected) == Pawn and selected.color == turn and board[old_pos[0]][old_pos[1]+1].move_moved_2==move_counter-1:
                if to_pos==(old_pos[0]+1,old_pos[1]+1):
                    selected.en_passanted=True 
                    selected.en_passantobe=(old_pos[0],old_pos[1]+1)  
            if type(selected) == Pawn and selected.color == turn and board[old_pos[0]][old_pos[1]-1].move_moved_2==move_counter-1:
                if to_pos==(old_pos[0]+1,old_pos[1]-1):
                    selected.en_passanted=True 
                    selected.en_passantobe=(old_pos[0],old_pos[1]-1)  

            if type(selected) == Pawn and selected.color == turn and board[old_pos[0]][old_pos[1]+1].move_moved_2==move_counter-1:
                if to_pos==(old_pos[0]-1,old_pos[1]+1):
                    selected.en_passanted=True 
                    selected.en_passantobe=(old_pos[0],old_pos[1]+1)                

            to_pos=None
            turn=~selected
            move_counter+=1
    for i in board:
        for j in i:
            if type(j)==Pawn:
                j.move=move_counter
    
    for i in board:
        for j in i:
            if type(j)==Pawn and j.move-1!=j.move_moved_2:
                j.just_moved_two=False


    
    

    return turn


 
    
                        


                    


   