board = ['','','','','','','','','']
def draw_board():
    print("__"+board[8]+"|__"+board[7]+"___|"+board[6]+"__")
    print("__"+board[5]+"|__"+board[4]+"___|"+board[3]+"__")
    print("__"+board[2]+"|__"+board[1]+"___|"+board[0]+"__")
    
def select_marker():
    marker = ''

    while marker != 'x' and marker != 'o':
        marker = raw_input("Do you want to be X or O")
    if marker == 'x':
        return ('x','o')
    else:
        return ('o','x')

def win_condition(board,mark):
        if board[0]==board[1]==board[2]==mark or \
           board[3]==board[4]==board[5]==mark or \
           board[6]==board[7]==board[8]==mark or \
           board[0]==board[4]==board[8]==mark or \
           board[2]==board[4]==board[6]==mark or \
           board[0]==board[3]==board[6]==mark or \
           board[2]==board[5]==board[8]==mark or \
           board[1]==board[4]==board[7]==mark:
            return True
        else:
            return False
    

def check_place(i):
        if board[i]=='x' or board[i]=='o':
            #print("position filled")
            return False
        else:
            #print("position vacant")
            return True
        
def player_input1():
    
    print("select the box you want to play x or o")
    ans = int(raw_input())
    if check_place(ans):
        print("position vacant")
        board[ans]=mark[0]
        draw_board()
        if win_condition(board,mark[0]):
            print("player 1 wins")
        else:
            print("player 2 turn")
            player_input2()
        
        
    else:
        while not check_place(ans):
            print("box already filled, select another box")
            ans = int(raw_input())
        board[ans]=mark[0]
        draw_board()
        if win_condition(board,mark[0]):
            print("player 1 wins")
        else:
            print("player 2 turn")
            player_input2()
    
        
    
    

def player_input2():
    print("select the box you want to play x or o")
    ans = int(raw_input())
    if check_place(ans):
        board[ans]=mark[1]
        draw_board()
        if win_condition(board,mark[1]):    
            print("player 2 wins")
        else:
            print("player 1 turn")
            player_input1()
    
        
    else:
        while not check_place(ans):
            print("box already filled, select another box")
            ans = int(raw_input())
        board[ans]=mark[1]
        draw_board()
        if win_condition(board,mark[1]):
            print("player 2 wins")
        else:
            print("player 1 turn")
            player_input1()
        
        
   
    

    


        
draw_board()

print("take the player 1 input")
mark = select_marker()
player_input1()
