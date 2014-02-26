#!/usr/bin/env python

"""
Dogecider v0.1a
(c) 2014 Dhruv Nagpal / Chathika Weerasuriya
Released under the XXX License
Brought to you by the LazySundayCorporation: "Utility is secondary to validity."

"""

import math, readline

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

def autocompleter(text, state):
    options = [i for i in choices if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

#I have no idea what this does:
readline.parse_and_bind("tab: complete")

def new_choice(entry):
    if entry not in choice:
        choice.append(entry)


#set empty list of "choices" - this will just hold the master list of different options for the autocompleter
choices = []

# Set empty group dictionary
group = {}

# Set total group size and return to user
group_size = int(raw_input("Enter the number of people trying to make a decision: "))
print "\n" + str(group_size) + " jokers can't make a decision to save their lives"



# Other things needed:
# Figure out rest of autofill using tab autocompletion ("readline" module) / autocompleter function.
# "Re-choose" option
# "Edit/Remove specific choices/entries"
# "Save decision making session"
# "Re-open and edit decision making session"
# Ideally we should have a live display of each user, the options they enter and the relative preference score for each.

print "\n"

exit
