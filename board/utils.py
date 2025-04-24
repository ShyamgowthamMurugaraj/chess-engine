from constants import SQUARE_SIZE

def eval_pos(pos:tuple)->tuple:
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return row, col

def filter_moves(moves:list)->list:
    new_moves=[]
    for row,col in moves:
        if row>=0 and col>=0:
            new_moves.append((row,col))
    
    return new_moves