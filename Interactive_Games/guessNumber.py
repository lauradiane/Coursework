# NOTE: In order to actually run the code, you will need to go to http://www.codeskulptor.org/#user3-enf5xq9RVb-63.py
# becauase CodeSkulptor has "simplegui"

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# initialize global variables used in your code
secretNumber = 0
high = 100
guessesLeft = 1

# helper functions
def init():
    global high, secretNumber, guessesLeft
    while 2 **(guessesLeft) < high + 1:
        guessesLeft += 1
    print "New Game. Range is from 0 to " + str(high)
    print "Number of remaining guesses is " + str(guessesLeft)
    secretNumber = random.randrange(high)
    return secretNumber

# define event handlers for control panel
def range100():
    ''' button that changes range to range [0,100) and restarts '''
    global high
    high = 100
    print ''
    return init()    

def range1000():
    ''' button that changes range to range [0,1000) and restarts '''
    global high
    high = 1000
    print ''
    return init()
    
def get_input(guess):
    ''' main logic of the game, creates input that take and processes guess '''
    global guessesLeft
    print ' '
    print "Guess was " + str(guess)
    guess = int(guess)
    guessesLeft -= 1
    print "Number of remaining guesses is " + str(guessesLeft)
    if guess == secretNumber:
        print "Correct!"
        print ''
        init()
    elif guessesLeft == 0:
        print "No Guesses Left. Answer was " + str(secretNumber)
        print ''
        init()
    elif guess < secretNumber:
        print "Higher!"
    else:
        print "Lower!"
    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)

frame.add_button("Range is [0, 1000)", range1000, 200)

frame.add_input("Guess a number: ", get_input, 100)

init()

# start frame
frame.start()