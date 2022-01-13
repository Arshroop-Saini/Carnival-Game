initial_list=['','O','']



def shuffling(initial_list):
    from random import shuffle
    shuffle(initial_list)
    return initial_list

final_list=shuffling(initial_list)


def player_guess():
    guess=''

    while guess not in ['0','1','2']:
        guess= input("Choose a number from 0,1 and 2:  ")

    return int(guess)

guess=player_guess() 

def check_guess(mylist,guess):
        if mylist[guess] == 'O':
            print('Correct Guess!')
        else:
            print("Better luck next time :(")
            print(initial_list)

check_guess(final_list, guess)







