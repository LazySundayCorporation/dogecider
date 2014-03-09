#!/usr/bin/env python

"""
Dogecider v0.1a
(c) 2014 Dhruv Nagpal / Chathika Weerasuriya
Released under the XXX License
Brought to you by the LazySundayCorporation: "Utility is secondary to validity."

"""

import math, readline, re, random

# Welcome message

print """
Start ----------------------------------->
"""

#prompt tab autocompleter (like in BASH shell) - needed otherwise people need to keep typing in the same choice again
#http://stackoverflow.com/questions/187621/how-to-make-a-python-command-line-program-autocomplete-arbitrary-things-not-int
#http://tiswww.case.edu/php/chet/readline/readline.html#SEC44
#http://docs.python.org/2/library/readline.html

"""I think I understand this function - sort of. A different readline internal function (rl_completer_matches()) repeatedly calls autocompleter, setting the state+1 each time.
As long as the state < the size of list "options", it will return the next item in that list which begins with "text". I think.
"""

#integer check and repeat entry
def int_check(num):
    try:
        return int(num)
    except ValueError:
        num = raw_input("Try again. Enter a valid whole number: ")
        return int_check(num)

#console autocompleter
def autocompleter(text, state):
    options = [i for i in m_choices if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

#I have no idea what this does:
readline.parse_and_bind("tab: complete")
readline.set_completer(autocompleter)

#adds a new choice into master list of choices - used for autocompleter.
def new_choice(entry):
    if entry not in m_choices:
        m_choices.append(entry)

#set empty master list of "choices" - this will just hold the master list of different options for the autocompleter
m_choices = []

#master player dictionary - key is player name and value is player object
players = {}

#master list pre-random selection
randomiser_array = []

#define Player class and methods
class Player(object):
    
    
    def __init__(self, name, n_choices):
        self.name = name
        self.n_choices = n_choices
        self.i_choices = {}

    def remove_choice(self, sug):
        del self.i_choices[sug]

    def add_choice(self):
        entry = raw_input('Enter a new choice and score: ').lower()
        while not self.c_parse(entry):
            entry = raw_input('Incorrect format. Enter choice and score(1-9): ').lower()
        else:
            self.i_choices[self.c_parse(entry)[0]] = self.c_parse(entry)[1]
            new_choice(self.c_parse(entry)[0])
        
        #while self.c_parse(entry)[1] <1 or self.c_parse(entry)[1] > 9:
            #entry = raw_input('Incorrect format. Enter choice and score(1-9): ')
        
    #regex-parse any input string of format 'string, integer', return the two components. Individual components can be extracted as c_parse(entry)[0] and c_parse(entry)[1]. Tutorial: https://www.youtube.com/watch?v=kWyoYtvJpe4
    def c_parse(self, entry):
        parsed = re.search(r'(\S+)\s*,\s*(\d+)', entry)
        if parsed:
            return parsed.group(1), int(parsed.group(2))
        else:
            return False

def populate(players):
    for i in players:
        for j in players[i].i_choices:
            for k in range(players[i].i_choices[j]):
                randomiser_array.append(j)

def random_select(randomiser_array):
    print randomiser_array[random.randint(1, len(randomiser_array))]

# Set total group size and return to user
group_size = raw_input("Enter the number of people trying to make a decision: ")
print str(group_size) + " joker(s) can't make a decision to save their lives"

#check if group_size is an int
group_size = int_check(group_size)

#check if group_size >0 and set mode.
while group_size < 1:
    print "Gotta have at least one person being indecisive"
    group_size = int(raw_input("Re-enter the number of people trying to make a decision: "))

else:
    if group_size == 1:
        mode = 's'
        print 'single indecisive person'
    elif group_size > 1:
        mode = 'm'
        print 'a group of indecisive people'

#main add-player add-choices block

count = 1
while count <= group_size:
    p_name = raw_input('Enter player name: ')
    p_nchoices = int_check(raw_input('Enter the number of choices: '))
    players[p_name] = Player(p_name, p_nchoices)
    print "OK " + p_name + " , it's time to enter some choices."
    print "Enter a choice followed by a score - in this format: 'Apple, 9'. Scores must be 1-10."
    for i in range(p_nchoices):
        players[p_name].add_choice()
    count += 1
print "\n"
for i in players:
    print i, players[i].i_choices
print "\n"
print "Master choice list: ", m_choices
print "\n"
populate(players)
print "Master randomiser_array", randomiser_array
print "\n"
print "Randomiser x 6"
random_select(randomiser_array)
random_select(randomiser_array)
random_select(randomiser_array)
random_select(randomiser_array)
random_select(randomiser_array)
random_select(randomiser_array)

# player.add_choice(); player.remove_choice(); player.choice_lookup()

print "\n"

exit
