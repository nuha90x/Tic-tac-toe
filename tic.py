# grid = [['-','-','-'],['-','-','-'],['-','-','-']]
# x = "x"
# o = "0"

# player = 0
# counter = 0

# def check_win():
#     if (grid[0][0]==[0][1] and grid[0][2] and grid[0][0]!='-') or


# def show_grid():

# def x_round():

# def o_round():

# #once player 1 once player 2
# def alternate():    



# #if player 1 = player 2 no winner
# def check_tie():

x_player="x"
o_player="o"
activeplayer = x_player
activegame = True

board = {
    1:None,
    2:None,
    3:None,
    4:None,
    5:None,
    6:None,
    7:None,
    8:None,
    9:None,
}


def checkValue(num):
    if (board[num] is None):
        return str(num)
    else:
        return board[num]

def check_win():

    if ((checkValue(1)==checkValue(2) and checkValue(1)==checkValue(3)) or
        (checkValue(4)==checkValue(5) and checkValue(4)==checkValue(6)) or
        (checkValue(7)==checkValue(8) and checkValue(7)==checkValue(9)) or
        (checkValue(1)==checkValue(5) and checkValue(1)==checkValue(9)) or
        (checkValue(3)==checkValue(5) and checkValue(3)==checkValue(7)) or
        (checkValue(1)==checkValue(4) and checkValue(1)==checkValue(7)) or
        (checkValue(2)==checkValue(5) and checkValue(2)==checkValue(8)) or
        (checkValue(3)==checkValue(6) and checkValue(3)==checkValue(9))
        
        
        ):
        print(str(activeplayer) + " player - you are a winner")
        activegame=False
    elif(all(board.values())):     
        print("You are both tie")
        activegame=False

def draw_board():
    print(checkValue(1), checkValue(2), checkValue(3) )
    print(checkValue(4), checkValue(5), checkValue(6) )
    print(checkValue(7), checkValue(8), checkValue(9) )



def changeplayer():
    global activeplayer
    if (activeplayer==x_player):
        activeplayer = o_player
    else:
        activeplayer = x_player 

    


def play():
    ans = int(input(str(activeplayer) + " player - choose a number: "))
    if (ans > 0 and ans < 10):
        if (board[ans] is None):
            board[ans] = activeplayer
            check_win()
            changeplayer()
            draw_board()
            
        else:
          print("Please choose other number")  
    else:
      print("Please choose a number between 1 and 9")
      play()


draw_board()

while activegame:
    play()
    