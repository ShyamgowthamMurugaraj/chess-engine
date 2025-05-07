from pieces import Empty,Pawn,Rook,Bishop,Queen,Knight,King

def make_board(player:str)->list:
    if player=="w":
        board=[]
        board=[[Empty((j,i),board) for i in range(8) ] for j in range(8)]
        board[1]=[Pawn("b",(1,i),board) for i in range(8)]
        board[6]=[Pawn("w",(6,i),board) for i in range(8)]

        board[0][0]=Rook("b",(0,0),board)
        board[0][7]=Rook("b",(0,7),board)
        board[7][7]=Rook("w",(7,7),board)
        board[7][0]=Rook("w",(7,0),board)





        board[0][2]=Bishop("b",(0,2),board)
        board[0][5]=Bishop("b",(0,5),board)
        board[7][2]=Bishop("w",(7,2),board)
        board[7][5]=Bishop("w",(7,5),board)

        board[0][3]=Queen("b",(0,3),board)
        board[0][4]=King("b",(0,4),board)
        board[7][3]=Queen("w",(7,3),board)
        board[7][4]=King("w",(7,4),board)


        board[0][1]=Knight("b",(0,1),board)
        board[0][6]=Knight("b",(0,6),board)
        board[7][1]=Knight("w",(7,1),board)
        board[7][6]=Knight("w",(7,6),board)
    
    if player=="b":
        board=[]
        board=[[Empty((j,i),board) for i in range(8) ] for j in range(8)]
        board[1]=[Pawn("w",(1,i),board) for i in range(8)]
        board[6]=[Pawn("b",(6,i),board) for i in range(8)]

        board[0][0]=Rook("w",(0,0),board)
        board[0][7]=Rook("w",(0,7),board)
        board[7][7]=Rook("b",(7,7),board)
        board[7][0]=Rook("b",(7,0),board)





        board[0][2]=Bishop("w",(0,2),board)
        board[0][5]=Bishop("w",(0,5),board)
        board[7][2]=Bishop("b",(7,2),board)
        board[7][5]=Bishop("b",(7,5),board)

        board[0][3]=Queen("w",(0,3),board)
        board[0][4]=King("w",(0,4),board)
        board[7][3]=Queen("b",(7,3),board)
        board[7][4]=King("b",(7,4),board)


        board[0][1]=Knight("w",(0,1),board)
        board[0][6]=Knight("w",(0,6),board)
        board[7][1]=Knight("b",(7,1),board)
        board[7][6]=Knight("b",(7,6),board)
    
    return board


# board[0][0]=Rook("b",(0,0),board)
# board[0][7]=King("w",(0,7),board)

# board[0][2]=Bishop("b",(0,2),board)





