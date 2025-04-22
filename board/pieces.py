class Empty:
    def __init__(self,pos:tuple):
        self.pos=pos

    def valid_moves(self):
        return [self.pos]
    def __repr__(self):
        return f"-"
    
class Piece:
    def __init__(self,color:str,value:int):
        self.color=color
        self.value=value
    
class Pawn(Piece):
    def __init__(self, color:str , pos:tuple , board:list):
        super().__init__(color,value=1)
        self.pos=pos
        self.board=board
    
    def valid_moves(self) -> list:
        valid_moves=[]
        if self.color=="b":
            if self.pos[0]+1<8 and type(self.board[self.pos[0]+1][self.pos[1]])==Empty:
                valid_moves.append((self.pos[0]+1,self.pos[1]))
            if self.pos[0]+2==3 and type(self.board[self.pos[0]+2][self.pos[1]])==Empty and type(board[self.pos[0]+1][self.pos[1]]=="-")==Empty:
                valid_moves.append((self.pos[0]+2,self.pos[1]))
        if self.color=="w":
            if self.pos[0]-1>0 and type(self.board[self.pos[0]-1][self.pos[1]])==Empty:
                valid_moves.append((self.pos[0]-1,self.pos[1]))
            if self.pos[0]-2==4 and type(self.board[self.pos[0]-2][self.pos[1]])==Empty and type(board[self.pos[0]-1][self.pos[1]])==Empty:
                valid_moves.append((self.pos[0]-2,self.pos[1]))
        
        return valid_moves
    def __repr__(self) -> str:
        return f"{self.color}P"

class Rook(Piece):
    def __init__(self, color:str , pos:tuple , board:list):
        super().__init__(color,value=5)
        self.pos=pos
        self.board=board
    
    def valid_moves(self) -> list:
        valid_moves=[]
        current=self.pos
        try:
            current=self.pos
            while True:
                if type(board[current[0]][current[1]+1])==Empty:
                    valid_moves.append((current[0],current[1]+1))
                    current=(current[0],current[1]+1)
                    continue
                else:
                    break
        except:
            pass

        try:
            current=self.pos
            while True:
                if type(board[current[0]][current[1]-1])==Empty and current[1]-1>=0:
                    valid_moves.append((current[0],current[1]-1))
                    current=(current[0],current[1]-1)
                    continue
                else:
                    break
        except:
            pass

        try:
            current=self.pos
            while True:
                if type(board[current[0]+1][current[1]])==Empty:
                    valid_moves.append((current[0]+1,current[1]))
                    current=(current[0]+1,current[1])
                    continue
                else:
                    break
        except:
            pass

        try:
            current=self.pos
            while True:
                if type(board[current[0]-1][current[1]])==Empty and current[0]-1>=0:
                    valid_moves.append((current[0]-1,current[1]))
                    current=(current[0]-1,current[1])
                    continue
                else:
                    break
        except:
            pass
        

        return valid_moves
    def __repr__(self) -> str:
        return f"{self.color}R"

    
board=[[Empty((j,i)) for i in range(8) ] for j in range(8)]
board[1]=[Pawn("b",(1,i),board) for i in range(8)]
board[6]=[Pawn("w",(6,i),board) for i in range(8)]

board[0][0]=Rook("w",(0,0),board)
board[4][4]=Rook("w",(4,4),board)
print(board[4][4].valid_moves())



for i in board:
    print(i)




