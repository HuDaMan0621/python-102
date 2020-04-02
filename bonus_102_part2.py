'''Create a simple number guessing game that gives the user 5 chances.
Read the python 3 documentation for the "random.randint()" function.
Use that function to generate a random integer between 0 and 10.
Then, prompt them 5 times (at most) to guess the number.
If they guess correctly, congratulate them, and do not prompt them any more.
If they guess incorrectly, let them know they didn't guess correctly
If they run out of guesses, tell them they need to run the program again.
'''

from random import randint
def generator():
    return randint(0, 10)

def rand_guess():
    random_number = generator()
    guess_left = 5
    flag = 0
    
    while guess_left > 0:
        guess = int(input('Pick your lucky number \n'))
        if guess == random_number:
           flag = 1
           break
    else:
        print('wrong guess')
    
    guess_left -= 1

    if flag is 1:
        return True
    else: return False

if __name__ == '__main__': 
    if rand_guess() is True: 
        print("Congrats!! You Win.") 
    else : 
        print("Sorry, You Lost!") 