import random
win  = 0

def gen_code():
    code = []
    for x in range(4):
        code.append(random.randrange(0,9))
    return code

def count_code(code):
    count = {}
    for num in code:
        ticker = 0
        count[num] = 0
        for i in range(len(code)):
            if num == code[i]:
                ticker += 1
            count[num] = ticker
    return count


def check(code, guess, win):
    guess_out   = ['-','-','-','-']
    win_con     = 0
    x_it        = 0
    y_it        = 0
    count       = 0
    code_count  = count_code(code)
    guess_count = count_code(guess)

    for number in guess:
        for num in code:
        #print(num)
            #print("Guess,Count:\t",guess[count], code[count], count)
            #print("Guess,Num  :\t",guess[count], num)
            if  number == num and guess[count] != code[count]:
                #print (count)
                if code_count[number] > guess_count[number]:
                    for i in range(guess_count[number]):
                        guess_out[x_it] = 'X'
                        x_it  += 1
                        print('a:\t',guess_out, x_it)
                elif guess_count[number] > code_count[number]:
                    for i in range(code_count[number]):
                        guess_out[x_it] = 'X'
                        x_it  += 1
                        print('b:\t',guess_out, x_it)
                elif guess_count[number] == code_count[number]:
                    for i in range(code_count[number]):
                        guess_out[x_it] = 'X'
                        x_it  += 1
                        print('c:\t',guess_out, x_it)
        count += 1
        print(num,'\t', count)

    for x in range(len(guess)):
        if guess[x] == code[x]:
            guess_out[y_it] = 'O'
            y_it += 1
            win_con += 1
        if win_con == 4:
            print ("!!! CODE CRACKED !!!")
            return 'cracked'
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
    print(count_code(crack))
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

