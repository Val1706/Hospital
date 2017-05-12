import random
from random import randint
from time import sleep
import os
import time



life_inv = {"Lifes": 3}
inv = {"Keys":0}
med_inv = {"Ambulance": 100}


class bcolors:
    HEADER = '\033[95m'
    OKGRAY = '\033[43m' #43m
    OKBLUE = '\033[19m'
    WARNING = '\033[93m'  #
    FAIL = '\033[30m' #91
    END = '\033[0m'  #41
    BOLD = '\033[41m'
    UNDERLINE = '\033[4m'


key_col = bcolors.FAIL + "🔑" + bcolors.BOLD
block_col = bcolors.OKGRAY + "█" + bcolors.BOLD
def read_map():
    with open("mapa.txt", "r") as f:
        board1 =[]
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in open('mapa.txt')]
        for line in lines:
            row=[]
            
            #row.append(line)
            for letter in line:
                if letter == "🔑":
                     letter = key_col
                if letter == "█":
                     letter = block_col             
                row.append(letter)
            board1.append(row)
    return board1

def read_map2():
    with open("mapa2.txt", "r") as f:
        board =[]
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in open('mapa2.txt')]
        for line in lines:
            row=[]         
            for letter in line:
                if letter == "█":
                     letter = block_col     
                row.append(letter)
            board.append(row)
    return board
def read_map3():
    with open("mapa3.txt", "r") as f:
        board =[]
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in open('mapa3.txt')]
        for line in lines:
            row=[]         
            for letter in line:
                if letter == "█":
                     letter = block_col     
                row.append(letter)
            board.append(row)
    return board

def read_map4():
    with open("mapa3.txt", "r") as f:
        board =[]
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in open('mapa4.txt')]
        for line in lines:
            row=[]         
            for letter in line:
                if letter == "█":
                     letter = block_col     
                row.append(letter)
            board.append(row)
    return board



def print_board(board):
    for row in board:
        for character in row:
            print(character, end='')

        print()


def insert_player(board, width, height):
    board[width][height] = bcolors.OKBLUE + "👳‍" + bcolors.OKBLUE
    
    return board





def getch():
    import sys, tty, termios
    from select import select
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        [i, o, e] = select([sys.stdin.fileno()], [], [], 0.35)
        if i: ch=sys.stdin.read(1)
        else: ch=''
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def doors(movable_items):
    if inv["Keys"] == 4:
        movable_items.append("🚪")
        

def user_move(x_pos, y_pos, character, board):
    
    board[x_pos][y_pos] = " "
    movable_items = [" ", key_col, "💉","💊","🌡"]
    doors(movable_items)
    if character == 'd' and board[x_pos][y_pos +1] in movable_items:
        med_inv["Ambulance"] -= 2
        y_pos += 1
 
    elif character == 'a' and board[x_pos][y_pos - 1] in movable_items:
        med_inv["Ambulance"] -= 2
        y_pos -= 1
    elif character == 'w' and board[x_pos - 1][y_pos] in movable_items:
        med_inv["Ambulance"] -= 2
        x_pos -= 1
    elif character == 's' and board[x_pos + 1][y_pos] in movable_items:
        med_inv["Ambulance"] -= 2
        x_pos += 1
    
    elif character == "q":
        exit()

    return board, x_pos, y_pos

def doctor_move(x_pos_doc, y_pos_doc, board):
    free_space = []
    board[x_pos_doc][y_pos_doc] = " "
    
    if board[x_pos_doc][y_pos_doc +1] == " ":
        free_space.append((x_pos_doc, y_pos_doc +1))
    if board[x_pos_doc][y_pos_doc -1] == " ":
        free_space.append((x_pos_doc, y_pos_doc -1))
    if board[x_pos_doc -1][y_pos_doc] == " ":
        free_space.append((x_pos_doc -1, y_pos_doc))
    if board[x_pos_doc +1][y_pos_doc] == " ":
        free_space.append((x_pos_doc +1, y_pos_doc))
    doctor_new_position = random.choice(free_space)
    
    new_x_doc = doctor_new_position[0]
    new_y_doc = doctor_new_position[1]
    return new_x_doc, new_y_doc

def insert_doctor(x_pos_doc, y_pos_doc, board, symbol):
    board[x_pos_doc][y_pos_doc] = bcolors.OKBLUE + symbol + bcolors.BOLD
    return board


def not_enter(x_pos, y_pos, character, board,inv):
            if character == 'd' and board[x_pos][y_pos + 1] == "🚪":
                for keys in inv:
                    if inv[keys] != 4:
                        print("Plese find all keys")
                        return False
                    else: 
                        print("You won!")
                        med_inv["Ambulance"] = 100
                        return True
def not_enter_2(x_pos, y_pos, character, board, med_inv):
    
    if character == 'd' and board[x_pos][y_pos + 1] == "🚪":
        print("You won!")
        return True
    else:
        return False

def not_enter_3(x_pos, y_pos, character, board, med_inv):
    
    if character == 'd' and board[x_pos][y_pos + 1] == "🚪":
        print("You won!")
        return True
    else:
        return False

def touch_boss(x_pos, y_pos, character, board):
    
    if character == 'd' and board[x_pos][y_pos + 1] == block_col:
        print("You won!")
        return True
    else:
        return False
    

def colision(x_pos, y_pos, x_pos_doc, y_pos_doc,x_pos_doc_2, y_pos_doc_2,x_pos_doc_3, y_pos_doc_3, x_pos_doc_4, y_pos_doc_4,x_pos_doc_5, y_pos_doc_5, x_pos_doc_6, y_pos_doc_6):  
    if x_pos == x_pos_doc and y_pos == y_pos_doc: 
        return True
    elif x_pos == x_pos_doc_2 and y_pos == y_pos_doc_2:
        return True
    elif x_pos == x_pos_doc_3 and y_pos == y_pos_doc_3:
        return True
    elif x_pos == x_pos_doc_4 and y_pos == y_pos_doc_4:
        return True
    elif x_pos == x_pos_doc_5 and y_pos == y_pos_doc_5:
        return True
 
def print_table(dict1,dict2,dict3):
    print("   ╔========================╗")
    print("   Inventory:      Amount: \n")
    for k,v in dict1.items():
        print("   ║",k, "       :  ", v)
    print("    ----------------------------")
    for k,v in dict2.items():
        print("   ║",k, "   :  ", v)
    for k,v in dict3.items():
        print("   ║",k, "        :  ", v)
     
    print("   ╚=========================╝")
    print("  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
def stopwatch():
    start = time.time()
    time.clock()    
    elapsed = 1
    elapsed = time.time() - start
    a = 2 - time.clock()
    print("  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print ("      Your time:" , a)
    if a <= 0:
        a = 0
        print("   Time out")
        quit()
        
def main():
    level = 1
    x_pos = 1
    y_pos = 1
    board = read_map()

    character = ''
    x_pos = 1
    y_pos = 1
    x_pos_doc = 1
    y_pos_doc = 20
    x_pos_doc_2 = 12
    y_pos_doc_2 = 21
    x_pos_doc_3 = 21
    y_pos_doc_3 = 12
    x_pos_doc_4 = 7
    y_pos_doc_4 = 42
    x_pos_doc_5 = 22
    y_pos_doc_5 = 65
    x_pos_doc_6 = 15
    y_pos_doc_6 = 30
    next_level = False
    next_level2 = False
    next_level3 = False
    while character != block_col:
        character = getch()
        board, x_pos, y_pos = user_move(x_pos, y_pos, character, board)
        if board[x_pos][y_pos] == key_col:
            inv["Keys"] += 1
        os.system('clear')    
        board = insert_player(board, x_pos, y_pos)
        print_board(board)
        if level == 1:
            if next_level != True:
                next_level = not_enter(x_pos, y_pos, character, board,inv)   
                

        
            if next_level == True:
                
                level = 2
            
                x_pos = 15
                y_pos = 15
                
                next_level = False
           

            
            

        if level == 2:
            board = read_map2()
            stopwatch()
            print_table(life_inv,med_inv,inv)
            x_pos_doc, y_pos_doc = doctor_move(x_pos_doc, y_pos_doc, board)
            x_pos_doc_2, y_pos_doc_2 = doctor_move(x_pos_doc_2, y_pos_doc_2, board)
            x_pos_doc_3, y_pos_doc_3 = doctor_move(x_pos_doc_3, y_pos_doc_3, board)
            x_pos_doc_4, y_pos_doc_4 = doctor_move(x_pos_doc_4, y_pos_doc_4, board)
            x_pos_doc_5, y_pos_doc_5 = doctor_move(x_pos_doc_5, y_pos_doc_5, board)
            x_pos_doc_6, y_pos_doc_6 = doctor_move(x_pos_doc_6, y_pos_doc_6, board)

            board = insert_doctor(x_pos_doc, y_pos_doc, board, "👨‍")
            board = insert_doctor(x_pos_doc_2, y_pos_doc_2, board, "👩‍")
            board = insert_doctor(x_pos_doc_3, y_pos_doc_3, board, "🤕")
            board = insert_doctor(x_pos_doc_4, y_pos_doc_4, board, "👩")
            board = insert_doctor(x_pos_doc_5, y_pos_doc_5, board, "👮‍")
            board = insert_doctor(x_pos_doc_6, y_pos_doc_6, board, "👮‍")


            if colision(x_pos, y_pos, x_pos_doc, y_pos_doc,x_pos_doc_2, y_pos_doc_2,x_pos_doc_3, y_pos_doc_3,x_pos_doc_4, y_pos_doc_4,x_pos_doc_5, y_pos_doc_5,x_pos_doc_6, y_pos_doc_6) == True:
                
                life_inv["Lifes"] -= 1
                x_pos = 26
                y_pos = 14
            health = ["💉","💊","🌡"]
            if board[x_pos][y_pos] in health:
                med_inv["Ambulance"] += 2
            if med_inv["Ambulance"] <= 0 or  life_inv["Lifes"] <= 0:
                print("You lost, try again")
                quit()
            
            if next_level2 != True:
                next_level2 = not_enter_2(x_pos, y_pos, character, board, med_inv)   
                board = insert_player(board, x_pos, y_pos)
                

            if next_level2 == True:
                level = 3
                x_pos = 10
                y_pos = 5
                next_level2 == False

        if level == 3:
            board = read_map3()

            if next_level3 != True:
                next_level3 = not_enter_3(x_pos, y_pos, character, board, med_inv)   
                print(next_level3)
                board = insert_player(board, x_pos, y_pos)

            if next_level3 == True:
                level = 4
                x_pos = 15
                y_pos = 5
                next_level3 = False

        if level == 4:
            board = read_map4()

            touch_bos = touch_boss(x_pos, y_pos, character, board)
            print(touch_bos)
            if touch_bos == True:
                import hot.py
        

            
                

                
                            
                    

                        
                    
                    
                            

                
                    


                    

                    
                    
            
                    

            
main()