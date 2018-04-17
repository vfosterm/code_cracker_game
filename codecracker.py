import random
win  = 0

def gen_code():
    code = []
    for x in range(4):
        code.append(random.randrange(0,9))
    return code
#print(gen_code())

def check(code, guess, win):
    guess_out = []
    win_con   = 0
    for guess in code:
        if guess == code:
            guess_out.append('X')
            print(guess_out)
    for x in guess:
        if guess[x] == code[x]:
            guess_out.append('O')
            win_con += 1
            print(guess_out)
        if win_con == 4:
            print ("!!! CODE CRACKED !!!")
            win += 10
    return print(guess_out)

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
    while win < 10:
        guess = take_guess()
        print(guess)
        print (check(crack,guess, win))
        win += 1



main(win)

