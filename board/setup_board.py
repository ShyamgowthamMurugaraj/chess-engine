from pieces import Empty,Pawn,Rook,Bishop,Queen,Knight,King

board=[[Empty((j,i)) for i in range(8) ] for j in range(8)]
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

# board[4][4]=Queen("w",(4,4),board)


if __name__=="__main__":

    # print(board[4][4].valid_moves())



    for i in board:
        print(" ".join(map(str,i)))

    print("\n"*5)
    for i in board:
        for j in i:
            print(f'{str(j)} - {j.valid_moves()}')