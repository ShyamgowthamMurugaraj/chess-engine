from utils import filter_moves



class Empty:
    def __init__(self,pos:tuple):
        self.pos=pos
        self.color=None
        self.image=None
    def valid_moves(self):
        return [self.pos]
    
    def __invert__():
        return None
    def __repr__(self):
        return f"--"
    
class Piece:
    def __init__(self,color:str,value:int):
        self.color=color
        self.value=value
    def __invert__(self):
        if self.color == "w":
            return "b"
        else:
            return "w"

    
class Pawn(Piece):
    def __init__(self, color:str , pos:tuple , board:list):
        super().__init__(color,value=1)
        self.image=f"assets/{self.color}P.png"

        self.pos=pos
        self.board=board
    
    def valid_moves(self) -> list:
        valid_moves=[]
        if self.color=="b":
            if self.pos[0]+1<8 and type(self.board[self.pos[0]+1][self.pos[1]])==Empty:
                valid_moves.append((self.pos[0]+1,self.pos[1]))
            if self.pos[0]+2==3 and type(self.board[self.pos[0]+2][self.pos[1]])==Empty and type(self.board[self.pos[0]+1][self.pos[1]])==Empty:
                valid_moves.append((self.pos[0]+2,self.pos[1]))
            try:
                if self.board[self.pos[0]+1][self.pos[1]+1].color=="w":
                    valid_moves.append((self.pos[0]+1,self.pos[1]+1))
                if self.board[self.pos[0]+1][self.pos[1]-1].color=="w":
                    valid_moves.append((self.pos[0]+1,self.pos[1]-1))
            except:
                pass
        if self.color=="w":
            if self.pos[0]-1>0 and type(self.board[self.pos[0]-1][self.pos[1]])==Empty:
                valid_moves.append((self.pos[0]-1,self.pos[1]))
            if self.pos[0]-2==4 and type(self.board[self.pos[0]-2][self.pos[1]])==Empty and type(self.board[self.pos[0]-1][self.pos[1]])==Empty:
                valid_moves.append((self.pos[0]-2,self.pos[1]))
            try:
                if self.board[self.pos[0]-1][self.pos[1]+1].color=="b":
                    valid_moves.append((self.pos[0]-1,self.pos[1]+1))
                if self.board[self.pos[0]-1][self.pos[1]-1].color=="b":
                    valid_moves.append((self.pos[0]-1,self.pos[1]-1))
            except:
                pass

        
        return filter_moves(valid_moves)
    def __repr__(self) -> str:
        return f"{self.color}P"

class Rook(Piece):
    def __init__(self, color:str , pos:tuple , board:list):
        super().__init__(color,value=5)
        self.image=f"assets/{self.color}R.png"
        self.pos=pos
        self.board=board
    
    def valid_moves(self) -> list:
        valid_moves=[]
        current=self.pos
        try:
            current=self.pos
            for i in range(current[1],8):
                if type(self.board[current[0]][i])==Empty:
                    valid_moves.append((current[0],i))
                elif ~self.board[current[0]][i]==self.color:
                    valid_moves.append((current[0],i))
                    break
                
        except:
            pass

        try:
            current=self.pos
            
            for i in range(current[1],-1,-1):
                if type(self.board[current[0]][i])==Empty:
                    valid_moves.append((current[0],i))
                elif ~self.board[current[0]][i]==self.color:
                    valid_moves.append((current[0],i))
                    break

            

        except:
            pass

        try:
            current=self.pos

            for i in range(current[0],8):
                if type(self.board[i][current[1]])==Empty:
                    valid_moves.append((i,current[1]))
                elif ~self.board[i][current[1]]==self.color:
                    valid_moves.append((i,current[1]))
                    break
        except:
            pass

        try:
            current=self.pos

            for i in range(current[0],-1,-1):
                if type(self.board[i][current[1]])==Empty:
                    valid_moves.append((i,current[1]))
                elif ~self.board[i][current[1]]==self.color:
                    valid_moves.append((i,current[1]))
                    break
        except:
            pass
        

        return filter_moves(valid_moves)
    def __repr__(self) -> str:
        return f"{self.color}R"

class Bishop(Piece):
    def __init__(self, color:str , pos:tuple , board:list):
        super().__init__(color,value=3)
        self.image=f"assets/{self.color}B.png"
        self.pos=pos
        self.board=board
    
    def valid_moves(self) -> list:
        valid_moves=[]
        current=self.pos
        try:
            current=self.pos
            while True:
                if type(self.board[current[0]+1][current[1]+1])==Empty:
                    valid_moves.append((current[0]+1,current[1]+1))
                    current=(current[0]+1,current[1]+1)
                    continue
                elif ~self.board[current[0]+1][current[1]+1]==self.color:
                    valid_moves.append((current[0]+1,current[1]+1))
                    break

                else:
                    break
            
        except:
            pass

        try:
            current=self.pos
            while True:
                if (type(self.board[current[0]-1][current[1]-1])==Empty and (current[1]-1>=0 and current[0]-1>=0)):
                    valid_moves.append((current[0]-1,current[1]-1))
                    current=(current[0]-1,current[1]-1)
                    continue
                elif ~self.board[current[0]-1][current[1]-1]==self.color:
                    valid_moves.append((current[0]-1,current[1]-1))
                    break

                else:
                    break

           
        except:
            pass

        try:
            current=self.pos
            while True:
                if (type(self.board[current[0]-1][current[1]+1])==Empty and (current[1]-1>=0)):
                    valid_moves.append((current[0]-1,current[1]+1))
                    current=(current[0]-1,current[1]+1)
                    continue
                elif ~self.board[current[0]-1][current[1]+1]==self.color:
                    valid_moves.append((current[0]-1,current[1]+1))
                    break

                else:
                    break
        except:
            pass
        try:
            current=self.pos
            while True:
                if (type(self.board[current[0]+1][current[1]-1])==Empty and current[1]-1>=0):
                    valid_moves.append((current[0]+1,current[1]-1))
                    current=(current[0]+1,current[1]-1)
                    continue
                elif ~self.board[current[0]+1][current[1]-1]==self.color:
                    valid_moves.append((current[0]+1,current[1]-1))
                    break

                else:
                    break
        except:
            pass
        return filter_moves(valid_moves)
    def __repr__(self) -> str:
        return f"{self.color}B"
        
class Queen(Piece):
    def __init__(self, color:str , pos:tuple , board:list):
        super().__init__(color,value=9)
        self.image=f"assets/{self.color}Q.png"
        self.pos=pos
        self.board=board
    
    def valid_moves(self) -> list:
        valid_moves=[]
        current=self.pos
        try:
            current=self.pos
            while True:
                if type(self.board[current[0]+1][current[1]+1])==Empty:
                    valid_moves.append((current[0]+1,current[1]+1))
                    current=(current[0]+1,current[1]+1)
                    continue
                elif ~self.board[current[0]+1][current[1]+1]==self.color:
                    valid_moves.append((current[0]+1,current[1]+1))
                    break

                else:
                    break
            
        except:
            pass

        try:
            current=self.pos
            while True:
                if (type(self.board[current[0]-1][current[1]-1])==Empty and (current[1]-1>=0 and current[0]-1>=0)):
                    valid_moves.append((current[0]-1,current[1]-1))
                    current=(current[0]-1,current[1]-1)
                    continue
                elif ~self.board[current[0]-1][current[1]-1]==self.color:
                    valid_moves.append((current[0]-1,current[1]-1))
                    break

                else:
                    break

           
        except:
            pass

        try:
            current=self.pos
            while True:
                if (type(self.board[current[0]-1][current[1]+1])==Empty and (current[1]-1>=0)):
                    valid_moves.append((current[0]-1,current[1]+1))
                    current=(current[0]-1,current[1]+1)
                    continue
                elif ~self.board[current[0]-1][current[1]+1]==self.color:
                    valid_moves.append((current[0]-1,current[1]+1))
                    break

                else:
                    break
        except:
            pass
        try:
            current=self.pos
            while True:
                if (type(self.board[current[0]+1][current[1]-1])==Empty and current[1]-1>=0):
                    valid_moves.append((current[0]+1,current[1]-1))
                    current=(current[0]+1,current[1]-1)
                    continue
                elif ~self.board[current[0]+1][current[1]-1]==self.color:
                    valid_moves.append((current[0]+1,current[1]-1))
                    break

                else:
                    break
        except:
            pass
        try:
            current=self.pos
            for i in range(current[1],8):
                if type(self.board[current[0]][i])==Empty:
                    valid_moves.append((current[0],i))
                elif ~self.board[current[0]][i]==self.color:
                    valid_moves.append((current[0],i))
                    break
                
        except:
            pass

        try:
            current=self.pos
            
            for i in range(current[1],-1,-1):
                if type(self.board[current[0]][i])==Empty:
                    valid_moves.append((current[0],i))
                elif ~self.board[current[0]][i]==self.color:
                    valid_moves.append((current[0],i))
                    break

            

        except:
            pass

        try:
            current=self.pos

            for i in range(current[0],8):
                if type(self.board[i][current[1]])==Empty:
                    valid_moves.append((i,current[1]))
                elif ~self.board[i][current[1]]==self.color:
                    valid_moves.append((i,current[1]))
                    break
        except:
            pass

        try:
            current=self.pos

            for i in range(current[0],-1,-1):
                if type(self.board[i][current[1]])==Empty:
                    valid_moves.append((i,current[1]))
                elif ~self.board[i][current[1]]==self.color:
                    valid_moves.append((i,current[1]))
                    break
        except:
            pass
        
        
        return filter_moves(valid_moves)
    
    def __repr__(self) -> str:
        return f"{self.color}Q"
    
class Knight(Piece):
    def __init__(self, color:str , pos:tuple , board:list):
        super().__init__(color,value=1)
        self.image=f"assets/{self.color}N.png"

        self.pos=pos
        self.board=board
    
    def valid_moves(self) -> list:
        valid_moves=[]
        try:
            if type(self.board[self.pos[0]+1][self.pos[1]+2])==Empty or ~self.board[self.pos[0]+1][self.pos[1]+2]==self.color:
                valid_moves.append((self.pos[0]+1,self.pos[1]+2))
        except:
            pass
        try:
            if type(self.board[self.pos[0]-1][self.pos[1]+2])==Empty or ~self.board[self.pos[0]-1][self.pos[1]+2]==self.color:
                valid_moves.append((self.pos[0]-1,self.pos[1]+2))
        except:
            pass

        try:
            if type(self.board[self.pos[0]+2][self.pos[1]+1])==Empty or ~self.board[self.pos[0]+2][self.pos[1]+1]==self.color:
                valid_moves.append((self.pos[0]+2,self.pos[1]+1))
        except:
            pass
        try:
            if type(self.board[self.pos[0]-2][self.pos[1]+1])==Empty or ~self.board[self.pos[0]-2][self.pos[1]+1]==self.color:
                valid_moves.append((self.pos[0]-2,self.pos[1]+1))
        except:
            pass

        

        try:
            if type(self.board[self.pos[0]-2][self.pos[1]-1])==Empty or ~self.board[self.pos[0]-2][self.pos[1]-1]==self.color:
                valid_moves.append((self.pos[0]-2,self.pos[1]-1))
        except:
            pass
        try:
            if type(self.board[self.pos[0]+2][self.pos[1]-1])==Empty or ~self.board[self.pos[0]+2][self.pos[1]-1]==self.color:
                valid_moves.append((self.pos[0]+2,self.pos[1]-1))
        except:
            pass

        try:
            if type(self.board[self.pos[0]-1][self.pos[1]-2])==Empty or ~self.board[self.pos[0]-1][self.pos[1]-2]==self.color:
                valid_moves.append((self.pos[0]-1,self.pos[1]-2))
        except:
            pass
        try:
            if type(self.board[self.pos[0]+1][self.pos[1]-2])==Empty or ~self.board[self.pos[0]+1][self.pos[1]-2]==self.color:
                valid_moves.append((self.pos[0]+1,self.pos[1]-2))
        except:
            pass
        
        return filter_moves(valid_moves)
    

    def __repr__(self) -> str:
        return f"{self.color}N"

class King(Piece):
    def __init__(self, color:str , pos:tuple , board:list):
        super().__init__(color,value=1)
        self.image=f"assets/{self.color}K.png"

        self.pos=pos
        self.board=board
    
    def valid_moves(self) -> list:
        valid_moves=[]
        try:
            if type(self.board[self.pos[0]][self.pos[1]+1])==Empty or ~self.board[self.pos[0]][self.pos[1]+1]==self.color:
                valid_moves.append((self.pos[0],self.pos[1]+1))
        except:
            pass
        try:
            if type(self.board[self.pos[0]][self.pos[1]-1])==Empty or ~self.board[self.pos[0]][self.pos[1]-1]==self.color:
                valid_moves.append((self.pos[0],self.pos[1]-1))
        except:
            pass
        try:
            if type(self.board[self.pos[0]+1][self.pos[1]])==Empty or ~self.board[self.pos[0]+1][self.pos[1]]==self.color:
                valid_moves.append((self.pos[0]+1,self.pos[1]))
        except:
            pass
        try:
            if type(self.board[self.pos[0]+1][self.pos[1]+1])==Empty or ~self.board[self.pos[0]+1][self.pos[1]+1]==self.color:
                valid_moves.append((self.pos[0]+1,self.pos[1]+1))
        except:
            pass
        try:
            if type(self.board[self.pos[0]+1][self.pos[1]-1])==Empty or ~self.board[self.pos[0]+1][self.pos[1]-1]==self.color:
                valid_moves.append((self.pos[0]+1,self.pos[1]-1))
        except:
            pass
        try:
            if type(self.board[self.pos[0]-1][self.pos[1]-1])==Empty or ~self.board[self.pos[0]-1][self.pos[1]-1]==self.color:
                valid_moves.append((self.pos[0]-1,self.pos[1]-1))
        except:
            pass
        try:
            if type(self.board[self.pos[0]-1][self.pos[1]])==Empty or ~self.board[self.pos[0]-1][self.pos[1]]==self.color:
                valid_moves.append((self.pos[0]-1,self.pos[1]))
        except:
            pass
        try:
            if type(self.board[self.pos[0]-1][self.pos[1]+1])==Empty or ~self.board[self.pos[0]-1][self.pos[1]+1]==self.color:
                valid_moves.append((self.pos[0]-1,self.pos[1]+1))
        except:
            pass

        return filter_moves(valid_moves)

    def __repr__(self) -> str:
        return f"{self.color}K"
    



