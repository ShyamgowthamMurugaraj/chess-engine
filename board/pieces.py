from utils import filter_moves

def find_king(board,color):
    for i in board:
        for j in i:
            if type(j)==King and j.color==color:
                return j

class Empty:
    def __init__(self,pos:tuple):
        self.pos=pos
        self.color=None
        self.image=None
    def valid_moves(self):
        return [self.pos]
    
    def __invert__(self):
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
    

    def threatening_moves(self) -> list:
        """Returns the moves this piece can threaten without considering checks."""
        return self.valid_moves()

    def valid_moves(self) -> list:
        valid_moves=[]
        if self.color=="b":
            if self.pos[0]+1<8 and type(self.board[self.pos[0]+1][self.pos[1]])==Empty:
                valid_moves.append((self.pos[0]+1,self.pos[1]))
            if self.pos[0]+2==3 and type(self.board[self.pos[0]+2][self.pos[1]])==Empty and type(self.board[self.pos[0]+1][self.pos[1]])==Empty:
                valid_moves.append((self.pos[0]+2,self.pos[1]))
            try:
                if self.board[self.pos[0]+1][self.pos[1]-1].color=="w":
                    valid_moves.append((self.pos[0]+1,self.pos[1]-1))
                if self.board[self.pos[0]+1][self.pos[1]+1].color=="w":
                    valid_moves.append((self.pos[0]+1,self.pos[1]+1))
                
            except:
                pass
        if self.color=="w":
            if self.pos[0]-1>0 and type(self.board[self.pos[0]-1][self.pos[1]])==Empty:
                valid_moves.append((self.pos[0]-1,self.pos[1]))
            if self.pos[0]-2==4 and type(self.board[self.pos[0]-2][self.pos[1]])==Empty and type(self.board[self.pos[0]-1][self.pos[1]])==Empty:
                valid_moves.append((self.pos[0]-2,self.pos[1]))
            try:
                if self.board[self.pos[0]-1][self.pos[1]-1].color=="b":
                    valid_moves.append((self.pos[0]-1,self.pos[1]-1))
                if self.board[self.pos[0]-1][self.pos[1]+1].color=="b":
                    valid_moves.append((self.pos[0]-1,self.pos[1]+1))

            except:
                pass
        king = find_king(self.board, self.color)
        if king and king.check()[0]:
            threatening_piece = king.check()[1]
            if threatening_piece:
                path_to_block = []
                if type(threatening_piece) in [Rook, Bishop, Queen]:
            
                    dx = threatening_piece.pos[0] - king.pos[0]
                    dy = threatening_piece.pos[1] - king.pos[1]
                    step_x = 0 if dx == 0 else dx // abs(dx)
                    step_y = 0 if dy == 0 else dy // abs(dy)
                    current_pos = (king.pos[0] + step_x, king.pos[1] + step_y)
                    while current_pos != threatening_piece.pos:
                        path_to_block.append(current_pos)
                        current_pos = (current_pos[0] + step_x, current_pos[1] + step_y)
                path_to_block.append(threatening_piece.pos)


                valid_moves = [move for move in valid_moves if move in path_to_block]
        
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
            for r in range(current[1]+1, 8):
                if type(self.board[current[0]][r])==Empty:
                    valid_moves.append((current[0],r))
                else:
                    if ~self.board[current[0]][r]==self.color:
                        valid_moves.append((current[0],r))
                    break 
                
        except:
            pass

        try:
            current=self.pos
            
            for r in range(current[1]-1, -1, -1):
                if type(self.board[current[0]][r])==Empty:
                    valid_moves.append((current[0],r))
                else:
                    if ~self.board[current[0]][r]==self.color:
                        valid_moves.append((current[0],r))
                    break 

            

        except:
            pass

        try:
            current=self.pos
            for r in range(current[0] + 1, 8, +1):
                if type(self.board[r][current[1]])==Empty:
                    valid_moves.append((r, current[1]))
                else:
                    if ~self.board[r][current[1]]==self.color:
                        valid_moves.append((r, current[1]))
                    break  

        except:
            pass

        try:
            current=self.pos

            for r in range(current[0] - 1, -1, -1):
                if type(self.board[r][current[1]])==Empty:
                    valid_moves.append((r, current[1]))
                else:
                    if ~self.board[r][current[1]]==self.color:
                        valid_moves.append((r, current[1]))
                    break  

                
        except:
            pass

        king = find_king(self.board, self.color)
        if king and king.check()[0]:
            threatening_piece = king.check()[1]
            if threatening_piece:
                path_to_block = []
                if type(threatening_piece) in [Rook, Bishop, Queen]:

                    dx = threatening_piece.pos[0] - king.pos[0]
                    dy = threatening_piece.pos[1] - king.pos[1]
                    step_x = 0 if dx == 0 else dx // abs(dx)
                    step_y = 0 if dy == 0 else dy // abs(dy)
                    current_pos = (king.pos[0] + step_x, king.pos[1] + step_y)
                    while current_pos != threatening_piece.pos:
                        path_to_block.append(current_pos)
                        current_pos = (current_pos[0] + step_x, current_pos[1] + step_y)
                path_to_block.append(threatening_piece.pos)


                valid_moves = [move for move in valid_moves if move in path_to_block]
        

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
        king = find_king(self.board, self.color)
        if king and king.check()[0]:
            threatening_piece = king.check()[1]
            if threatening_piece:
                path_to_block = []
                if type(threatening_piece) in [Rook, Bishop, Queen]:
            
                    dx = threatening_piece.pos[0] - king.pos[0]
                    dy = threatening_piece.pos[1] - king.pos[1]
                    step_x = 0 if dx == 0 else dx // abs(dx)
                    step_y = 0 if dy == 0 else dy // abs(dy)
                    current_pos = (king.pos[0] + step_x, king.pos[1] + step_y)
                    while current_pos != threatening_piece.pos:
                        path_to_block.append(current_pos)
                        current_pos = (current_pos[0] + step_x, current_pos[1] + step_y)
                path_to_block.append(threatening_piece.pos)


                valid_moves = [move for move in valid_moves if move in path_to_block]

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
            for r in range(current[1]+1, 8):
                if type(self.board[current[0]][r])==Empty:
                    valid_moves.append((current[0],r))
                else:
                    if ~self.board[current[0]][r]==self.color:
                        valid_moves.append((current[0],r))
                    break 

                
                
        except:
            pass

        try:
            current=self.pos
            
            for r in range(current[1]-1, -1, -1):
                if type(self.board[current[0]][r])==Empty:
                    valid_moves.append((current[0],r))
                else:
                    if ~self.board[current[0]][r]==self.color:
                        valid_moves.append((current[0],r))
                    break 

            

        except:
            pass

        try:
            current=self.pos
            for r in range(current[0] + 1, 8, +1):
                if type(self.board[r][current[1]])==Empty:
                    valid_moves.append((r, current[1]))
                else:
                    if ~self.board[r][current[1]]==self.color:
                        valid_moves.append((r, current[1]))
                    break  

        except:
            pass

        try:
            current=self.pos

            for r in range(current[0] - 1, -1, -1):
                if type(self.board[r][current[1]])==Empty:
                    valid_moves.append((r, current[1]))
                else:
                    if ~self.board[r][current[1]]==self.color:
                        valid_moves.append((r, current[1]))
                    break  

                
        except:
            pass
        king = find_king(self.board, self.color)
        if king and king.check()[0]:
            threatening_piece = king.check()[1]
            if threatening_piece:
                path_to_block = []
                if type(threatening_piece) in [Rook, Bishop, Queen]:
        
                    dx = threatening_piece.pos[0] - king.pos[0]
                    dy = threatening_piece.pos[1] - king.pos[1]
                    step_x = 0 if dx == 0 else dx // abs(dx)
                    step_y = 0 if dy == 0 else dy // abs(dy)
                    current_pos = (king.pos[0] + step_x, king.pos[1] + step_y)
                    while current_pos != threatening_piece.pos:
                        path_to_block.append(current_pos)
                        current_pos = (current_pos[0] + step_x, current_pos[1] + step_y)
                path_to_block.append(threatening_piece.pos)


                valid_moves = [move for move in valid_moves if move in path_to_block]
        
        
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

        
    
        king = find_king(self.board, self.color)
        if king and king.check()[0]:
            threatening_piece = king.check()[1]
            if threatening_piece:
                path_to_block = []
                if type(threatening_piece) in [Rook, Bishop, Queen]:
                    dx = threatening_piece.pos[0] - king.pos[0]
                    dy = threatening_piece.pos[1] - king.pos[1]
                    step_x = 0 if dx == 0 else dx // abs(dx)
                    step_y = 0 if dy == 0 else dy // abs(dy)
                    current_pos = (king.pos[0] + step_x, king.pos[1] + step_y)
                    while current_pos != threatening_piece.pos:
                        path_to_block.append(current_pos)
                        current_pos = (current_pos[0] + step_x, current_pos[1] + step_y)
                path_to_block.append(threatening_piece.pos)


                valid_moves = [move for move in valid_moves if move in path_to_block]
        return filter_moves(valid_moves)
    

    def __repr__(self) -> str:
        return f"{self.color}N"

class King(Piece):
    def __init__(self, color:str , pos:tuple , board:list):
        super().__init__(color,value=1)
        self.image=f"assets/{self.color}K.png"

        self.pos=pos
        self.board=board
        self.checking = False 
        
    
   


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
        

        legal_moves = []
        for move in valid_moves:
            original_piece = self.board[move[0]][move[1]]
            self.board[self.pos[0]][self.pos[1]] = Empty(self.pos)
            self.board[move[0]][move[1]] = self
            original_pos = self.pos
            self.pos = move

            if not self.check()[0]:
                legal_moves.append(move)

            self.pos = original_pos
            self.board[move[0]][move[1]] = original_piece
            self.board[self.pos[0]][self.pos[1]] = self

        valid_moves = legal_moves
       
            

        return filter_moves(valid_moves)
    
    def check(self):
        if self.checking:
            return (False, None)  
        self.checking = True
        try:
            for i in self.board:
                for j in i:
                    if type(j) != Empty and type(j) != King:
                        if j.color != self.color:
                            if self.pos in j.valid_moves():
                                return (True, j)
        finally:
            self.checking = False  
        return (False, None)
    
                            
                    
    
    def __repr__(self) -> str:
        return f"{self.color}K"
    



