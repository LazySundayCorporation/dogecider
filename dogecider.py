#!/usr/bin/env python

"""
Dogecider v0.1a
(c) 2014 Dhruv Nagpal / Chathika Weerasuriya
Released under the XXX License
Brought to you by the LazySundayCorporation: "Utility is secondary to validity."

"""

import math, readline, re

# Welcome message

print """

***********************************************

Welcome to the dogecider v0.1 - the decision making script for indecisive people.
This simple script will enable you and your lackadaisical friends to choose one of any given list of options in a weighted pseudo-random manner.

***********************************************

The princple is simple:
1. Enter the number of people in the group.
2. Each person enters the options they offer, along with a preference score for each option.
3. The program makes a weighted pseudo-random decision as to what option you're all going to follow through.

Note: it is pretty easy to weight a choice towards what you want by giving it a high preference score - but if you already have a strong preference for a give option, then why the hell are you using the dogecider?

Such indecision. Much solution. Wow.

Ctrl+D to exit at any given point.
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
    options = [i for i in choices if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

#I have no idea what this does:
readline.parse_and_bind("tab: complete")

#adds a new choice into master list of choices - used for autocompleter.
def new_choice(entry):
    if entry not in m_choices:
        m_choices.append(entry)

#set empty master list of "choices" - this will just hold the master list of different options for the autocompleter
m_choices = []

#master player dictionary - key is player name and value is player object
players = {}

#define Player class and methods
class Player(object):
    
    #individual choices and preferences
    i_choices = {}
    
    def __init__(self, name, n_choices):
        self.name = name
        self.n_choices = n_choices

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

for i in players:
    print i, players[i].i_choices

print "\n"
print "Master choice list: ", m_choices

# Other things needed:
# Figure out rest of autofill using tab autocompletion ("readline" module) / autocompleter function.
# "Re-choose" option
# "Edit/Remove specific choices/entries"
# "Save decision making session"
# "Re-open and edit decision making session"
# Ideally we should have a live display of each user, the options they enter and the relative preference score for each.

# player.add_choice(); player.remove_choice(); player.choice_lookup()

print "\n"

exit
