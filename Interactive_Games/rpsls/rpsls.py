# Rock-paper-scissors-lizard-Spock template

# NOTE: To see this in codeskulptor, visit http://www.codeskulptor.org/#user2-uNo4dk5H3k-18.py


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    if number == 0:
        return 'rock'
    if number == 1:
        return 'Spock'
    if number == 2:
        return 'paper'
    if number == 3:
        return 'lizard'
    if number == 4:
        return 'scissors'
    
    
def name_to_number(name):
    if name == 'rock':
        return 0
    if name == 'Spock':
        return 1
    if name == 'paper':
        return 2
    if name == 'lizard':
        return 3
    if name == 'scissors':
        return 4


import random
    
def rpsls(name): 
    player_number = name_to_number(name)
    comp_number = random.randrange(0,5)
    comp_name = number_to_name(comp_number)
    difference = (player_number - comp_number) % 5
    if difference <= 2:
        if difference != 0:
            winner = 'Player'
        else: 
            winner = 'tie'
    else:
        winner = 'Computer'
    print 'Player chooses ' + name 
    print 'Computer chooses ' + comp_name
    if winner == 'tie':
        print 'Player and Computer Tie!'
    else:
        print winner + ' wins!'
    print ''
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
