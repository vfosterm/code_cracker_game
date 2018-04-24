import random
from terminaltables import SingleTable

def guess_out_trans(guess_out):
    guess_out_transd = []
    for x in range(len(guess_out)):
        guess_str = ''
        for guess in guess_out[x]:
            guess_str += guess
        guess_out_transd.append(guess_str)
    return guess_out_transd

def draw_game(guess_list, guess_out):
    game_length = 10
    game = [[" CODE \n"," CRACK \n STATUS "],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['','']]
    crack_status = guess_out_trans(guess_out)
    game_add = []
    for x in range(len(guess_list)):
        game_add.append([guess_list[x], crack_status[x]])
    
    for addition in game_add:
        game[game_length] = addition
        game_length -= 1



    draw = SingleTable(game)
    draw.justify_columns[0] = 'center'
    draw.justify_columns[1] = 'center'
    print(draw.table)


def gen_code():
    code = []
    for x in range(4):
        code.append(random.randrange(0,9))
    return code

def check(code, guess, turn):
    guess_out   = ['-','-','-','-']
    x_it        = 0
    temp_code   = []
    guess_in = []
    for char in guess:
        guess_in.append(int(char))
    for num in code:
        temp_code.append(num)
    for x in range(len(guess_in)):
        if guess_in[x] == temp_code[x]:
            guess_out[x_it] = 'O'
            x_it += 1
            temp_code[x] = 99
            guess_in[x]     = 99

    for x in range(len(guess_in)):    
        for y in range(len(code)):
            if guess_in[x] == temp_code[y] and x != y and guess_in[x] < 10:
                guess_out[x_it] = 'X'
                x_it += 1
                guess_in[x] = 99
                temp_code[y] = 99
    return guess_out

def take_guess():
    guess = input('Enter 4 Digit Code: ')

    return guess

def main ():
    turn  = 1
    code = gen_code()
    guess_list   = []
    guess_out = []
    while turn < 11:
        
        draw_game(guess_list, guess_out)        
        guess     = take_guess()
        guess_list.append(guess)
        crack     = check(code,guess, turn)
        guess_out.append(crack)

        if crack == ['O','O','O','O']:
            draw_game(guess_list, guess_out)
            print ("!!! CODE CRACKED !!!")
            return
        if turn == 10:
            draw_game(guess_list, guess_out)
            print ("  !!! GAME OVER !!! ")
            return
        
        turn += 1



main()

