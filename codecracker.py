import random
win  = 0

def gen_code():
    code = []
    for x in range(4):
        code.append(random.randrange(0,9))
    return code

def check(code, guess, win):
    guess_out = ['-','-','-','-']
    win_con   = 0
    x_it = 0
    for i in range(len(code)):
        print (i)
        if guess[i] == code:
            guess_out[x_it] = 'X'
            x_it += 1
    for x in range(len(guess)):
        if guess[x] == code[x]:
            guess_out[x] = 'O'
            win_con += 1
        if win_con == 4:
            print ("!!! CODE CRACKED !!!")
            return 'cracked'

def take_guess():
    guess_in = []
    y = input('Enter 4 Digit Code: ')
    print(y)
    for char in y:
        guess_in.append(int(char))
    print (guess_in)
    return guess_in

def main (win):
    crack = gen_code()
    print(crack)
    while win < 11:
        guess = take_guess()
        print(guess)
        check_guess = check(crack,guess, win)
        if check_guess == 'cracked':
            return
        if win == 10:
            return print('GAME OVER')
        win += 1



main(win)

