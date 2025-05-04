from utils import filter_moves



def find_king(board,color):
    for i in board:
        for j in i:
            if type(j)==King and j.color==color:
                return j
    return None

class Empty:
    def __init__(self,pos:tuple,board):
        self.pos=pos
        self.color=None
        self.checking=False
        self.image=None
        self.board=board
        self.move_moved_2=None
    def valid_moves(self):
        return [self.pos]
    
    def check(self):
        color="w" if self.pos[0]==7 else "b"
        for row in self.board:
            for piece in row:
                if piece.color!=None:
                    if piece.color != color:
                        if self.pos in piece.valid_moves():
                            return True
        return False
    
    
        

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
        self.en_passanted=False
        self.just_moved_two=False
        self.en_passantobe=()
        self.move_moved_2=None
        self.move=None

    

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
            try: 
                if not isinstance(self.board[self.pos[0]][self.pos[1]+1],Empty): 
                    if self.board[self.pos[0]][self.pos[1]+1].just_moved_two:
                        valid_moves.append((self.pos[0]+1,self.pos[1]+1))
                if not isinstance(self.board[self.pos[0]][self.pos[1]-1],Empty):
                    if self.board[self.pos[0]][self.pos[1]-1].just_moved_two:
                        valid_moves.append((self.pos[0]+1,self.pos[1]-1))
            except Exception as e:
                print(e)
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
            try:
                if not isinstance(self.board[self.pos[0]][self.pos[1]+1],Empty):
                    if self.board[self.pos[0]][self.pos[1]+1].just_moved_two:
                        valid_moves.append((self.pos[0]-1,self.pos[1]+1))
                if not isinstance(self.board[self.pos[0]][self.pos[1]-1],Empty): 
                    if self.board[self.pos[0]][self.pos[1]-1].just_moved_two:
                        valid_moves.append((self.pos[0]-1,self.pos[1]-1))
                
            except Exception as e:
                print(e)
        if self.en_passanted:
            self.board[self.en_passantobe[0]][self.en_passantobe[1]]=Empty((self.pos[0]+1,self.pos[1]),self.board)

            


        new_moves=[]
        for i in filter_moves(valid_moves):

            og_pos=self.pos
            og_piece=self.board[i[0]][i[1]]
            self.board[i[0]][i[1]]=self
            self.pos=i
            self.board[og_pos[0]][og_pos[1]]=Empty(og_pos,self.board)
            try:
                if not find_king(self.board,self.color).check()[0]:
                    new_moves.append(i)
            except AttributeError:
                pass
            self.board[og_pos[0]][og_pos[1]]=self
            self.pos=og_pos
            self.board[i[0]][i[1]]=og_piece


        valid_moves.clear()

        return new_moves

        
    def __repr__(self) -> str:
        return f"{self.color}P"

class Rook(Piece):
    def __init__(self, color:str , pos:tuple , board:list):
        super().__init__(color,value=5)
        self.image=f"assets/{self.color}R.png"
        self.pos=pos
        self.board=board
        self.moved=False

    
    
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

        

        new_moves=[]
        for i in filter_moves(valid_moves):

            og_pos=self.pos
            og_piece=self.board[i[0]][i[1]]
            self.board[i[0]][i[1]]=self
            self.pos=i
            self.board[og_pos[0]][og_pos[1]]=Empty(og_pos,self.board)
            try:
                if not find_king(self.board,self.color).check()[0]:
                    new_moves.append(i)
            except AttributeError:
                pass
            self.board[og_pos[0]][og_pos[1]]=self
            self.pos=og_pos
            self.board[i[0]][i[1]]=og_piece


        valid_moves.clear()

        return new_moves


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
        

        new_moves=[]
        for i in filter_moves(valid_moves):

            og_pos=self.pos
            og_piece=self.board[i[0]][i[1]]
            self.board[i[0]][i[1]]=self
            self.pos=i
            self.board[og_pos[0]][og_pos[1]]=Empty(og_pos,self.board)
            try:
                if not find_king(self.board,self.color).check()[0]:
                    new_moves.append(i)
            except AttributeError:
                pass
            self.board[og_pos[0]][og_pos[1]]=self
            self.pos=og_pos
            self.board[i[0]][i[1]]=og_piece

        valid_moves.clear()

        return new_moves

        
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


        
        
        new_moves=[]
        for i in filter_moves(valid_moves):

            og_pos=self.pos
            og_piece=self.board[i[0]][i[1]]
            self.board[i[0]][i[1]]=self
            self.pos=i
            self.board[og_pos[0]][og_pos[1]]=Empty(og_pos,self.board)
            try:
                if not find_king(self.board,self.color).check()[0]:
                    new_moves.append(i)
            except AttributeError:
                pass
            self.board[og_pos[0]][og_pos[1]]=self
            self.pos=og_pos
            self.board[i[0]][i[1]]=og_piece
        valid_moves.clear()
        
        return new_moves


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

        
    
        
        new_moves=[]
        for i in filter_moves(valid_moves):

            og_pos=self.pos
            og_piece=self.board[i[0]][i[1]]
            self.board[i[0]][i[1]]=self
            self.pos=i
            self.board[og_pos[0]][og_pos[1]]=Empty(og_pos,self.board)
            try:
                if not find_king(self.board,self.color).check()[0]:
                    new_moves.append(i)
            except AttributeError:
                pass
            self.board[og_pos[0]][og_pos[1]]=self
            self.pos=og_pos
            self.board[i[0]][i[1]]=og_piece
        valid_moves.clear()

        return new_moves


    

    def __repr__(self) -> str:
        return f"{self.color}N"

class King(Piece):
    def __init__(self, color:str , pos:tuple , board:list):
        super().__init__(color,value=1)
        self.image=f"assets/{self.color}K.png"

        self.pos=pos
        self.board=board
        self.checking = False 
        self.moved=False
        self.king_castled=False
        self.queen_castled=False

        
    
   


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

        if not self.check()[0]:
        #castling
        #kingside 
            try:
                if type(self.board[self.pos[0]][self.pos[1]+1])==Empty and type(self.board[self.pos[0]][self.pos[1]+2])==Empty and type(self.board[self.pos[0]][self.pos[1]+3])==Rook and not self.board[self.pos[0]][self.pos[1]+3].moved and not self.checking:
                    if not self.board[self.pos[0]][self.pos[1]+1].check() and not self.board[self.pos[0]][self.pos[1]+2].check():
                        if (not self.moved) and (not self.board[self.pos[0]][self.pos[1]+3].moved):
                            valid_moves.append((self.pos[0],self.pos[1]+2))
                            if self.king_castled==True:
                                print(self.pos)
                                self.board[self.pos[0]][self.pos[1]+1]=Rook(self.color,(self.pos[0],self.pos[1]+1),self.board)
                                self.board[self.pos[0]][self.pos[1]+2]=self
                                self.board[self.pos[0]][self.pos[1]+3]=Empty((self.pos[0],self.pos[1]+3),self.board)
                                self.board[self.pos[0]][self.pos[1]]=Empty((self.pos[0],self.pos[1]),self.board)

                        
            except:
                pass

            #Queenside

            
            try:
                if type(self.board[self.pos[0]][self.pos[1]-1])==Empty and type(self.board[self.pos[0]][self.pos[1]-2])==Empty and type(self.board[self.pos[0]][self.pos[1]-3])==Empty and type(self.board[self.pos[0]][self.pos[1]-4])==Rook and not self.board[self.pos[0]][self.pos[1]-4].moved and not self.checking:
                    if not self.board[self.pos[0]][self.pos[1]-1].check() and not self.board[self.pos[0]][self.pos[1]-2].check() and not self.board[self.pos[0]][self.pos[1]-3].check() :
                        if (not self.moved) and (not self.board[self.pos[0]][self.pos[1]-4].moved):
                            valid_moves.append((self.pos[0],self.pos[1]-2))
                            if self.queen_castled==True:
                                print("yes")
                                self.board[self.pos[0]][self.pos[1]-1]=Rook(self.color,(self.pos[0],self.pos[1]-1),self.board)
                                self.board[self.pos[0]][self.pos[1]-2]=self
                                self.board[self.pos[0]][self.pos[1]-4]=Empty((self.pos[0],self.pos[1]-4),self.board)
                                self.board[self.pos[0]][self.pos[1]]=Empty((self.pos[0],self.pos[1]),self.board)

                        
            except:
                pass

        
        
       

        legal_moves = []
        for move in valid_moves:
            original_piece = self.board[move[0]][move[1]]
            self.board[self.pos[0]][self.pos[1]] = Empty(self.pos,self.board)
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
    
    def squares_in_all_dir(self):
        valid_moves=[]
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

    
    def check(self):
        if self.checking:
            return (False, None)  
        self.checking = True

        try:
            for square in self.squares_in_all_dir():
                j=self.board[square[0]][square[1]]
                if type(j) != Empty:
                    if j.color != self.color:
                        if self.pos in j.valid_moves():
                            return (True, j)
        except Exception as e:
            print(e)
        finally:
            self.checking = False  


        
        return (False, None)

        
        
    
                            
                    
    
    def __repr__(self) -> str:
        return f"{self.color}K"
    



