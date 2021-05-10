def main():
    player1Score =0
    player2Score = 0

    player1 = input("1. oyuncuyu temsil etmek için bir karakter giriniz:")
    player2 = input("2. oyuncuyu temsil etmek için bir karakter giriniz:")
    satir=int(input("Oyun alanının satır sayısını giriniz (3-7):"))
    sutun=int(input("Oyun alanının sütun sayısını giriniz (3-19):"))
    board= liste_yap(satir,sutun)

    for i in range(sutun):
        board[0][i][0] = 1
        board[satir-1][i][1] =1
    for k in range(satir):
        board[k][0][3] = 1
        board[k][sutun-1][2] = 1

    while(player1Score*player2Score < satir*sutun):
        turn = sira(player1,board,player1Score,satir,sutun)
        if turn == False :
            turn = sira(player2,board,player2Score,satir,sutun)

def sira(player,board,playerScore,satir,sutun):
    turn = oyna(player, board,satir,sutun)
    if turn== "score" :
        playerScore+=1
        sira(player,board,playerScore,satir,sutun)
    else:
        return False

def oyna(player,board,satir,sutun):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"]
    yon=["K","G","D","B"]
    s = input("Player " + player + "  seçmek istediğiniz kordinatı seçin !")
    if s[4] == "K" and board[int(s[0])][alphabet.index(s[2])][yon.index(s[4])] == 0 :
        board[int(s[0])-1][alphabet.index(s[2])][yon.index(s[4])]=1
        board[int(s[0])-2][alphabet.index(s[2])][1]=1

    if s[4] == "G" and board[int(s[0])][alphabet.index(s[2])][yon.index(s[4])] == 0 :
        board[int(s[0])-1][alphabet.index(s[2])][yon.index(s[4])]=1
        board[int(s[0])][alphabet.index(s[2])][0]=1

    if s[4] == "D" and board[int(s[0])][alphabet.index(s[2])][yon.index(s[4])] == 0 :
        board[int(s[0])-1][alphabet.index(s[2])][yon.index(s[4])] = 1
        board[int(s[0])-1][alphabet.index(s[2])+1][3] = 1

    if s[4] == "B" and board[int(s[0])][alphabet.index(s[2])][yon.index(s[4])] == 0 :
        board[int(s[0])-1][alphabet.index(s[2])][yon.index(s[4])] = 1
        board[int(s[0])-1][alphabet.index(s[2])-1][2] = 1


    if (board[int(s[0])-1][alphabet.index(s[2])][0] ==1 and board[int(s[0])-1][alphabet.index(s[2])][1]==1
        and board[int(s[0])-1][alphabet.index(s[2])][2]==1 and board[int(s[0])-1][alphabet.index(s[2])][3] ==1 ):
        yazdirma(board, satir, sutun, player)
        print("")
        return "score"
    else   :
        yazdirma(board, satir, sutun, "")
        print("")
        return "turn"

def liste_yap(satir,sutun):
    board = []
    for i in range(satir):
        board.append([])
        for b in range(sutun):
            board[i].append([0,0,0,0])
    return board

def yazdirma(board,satir,sutun,player):
    for i in range(satir):
        print("")
        for l in range(sutun):
            if board[i][l][0] == 1 :
                print(" _ " , end="")
        print("")
        for p in range(sutun):

            if board[i][p][3] == 1:
                print("|" , end="")
            else:
                print("   ",end="")
            if board[i][p][2] == 1 :
                print(" |",end="" )
            #else:
             #   print("   ",end="")
        print("")
        for o in range(sutun):
            if board[i][o][1] == 1:
                print(" _ " ,end="")

main()
