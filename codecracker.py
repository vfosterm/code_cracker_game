import random
win  = 0

def gen_code():
    code = []
    for x in range(4):
        code.append(random.randrange(0,9))
    return code

def check(code, guess, win):
    guess_out   = ['-','-','-','-']
    win_con     = 0
    x_it        = 0
    temp_code   = []
    
    for num in code:
        temp_code.append(num)
    for x in range(len(guess)):
        if guess[x] == temp_code[x]:
            guess_out[x_it] = 'O'
            x_it += 1
            win_con += 1
            temp_code[x] = 99
            guess[x]     = 99

        if win_con == 4:
            print ("!!! CODE CRACKED !!!")
            return True
    for x in range(len(guess)):    
        for y in range(len(code)):
            if guess[x] == temp_code[y] and x != y and guess[x] < 10:
                guess_out[x_it] = 'X'
                x_it += 1
                guess[x] = 99
                temp_code[y] = 99
    return print(guess_out)

def take_guess():
    guess_in = []
    y = input('Enter 4 Digit Code: ')
    for char in y:
        guess_in.append(int(char))
    return guess_in

def main (win):
    crack = gen_code()
    print(crack)
    while win < 10:
        guess = take_guess()
        if check(crack,guess, win) == True:
            return
        if win == 10:
            return print('GAME OVER')
        win += 1



main(win)

