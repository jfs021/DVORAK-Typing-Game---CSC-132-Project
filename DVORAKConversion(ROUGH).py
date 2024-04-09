#####################################################################
# author: Taylor DeMent  
# date: 4/8/2024    
# description: A ROUGH program that converts QWERTY keystrokes
# to DVORAK and combines the changed DVORAK letters into a 5 letter
# word and prints it 
#####################################################################


# function takes in each character typed  on the QWERTY keyboard
# and converts it to DVORAK
def ChangeKeyInput(letter):
    if ((letter == "q")):
        letter = "'"

    if ((letter == "w")):
        letter = ","

    if ((letter == "e")):
        letter = "."

    if ((letter == "r")):
        letter = "p"

    if ((letter == "t")):
        letter = "y"
        
    if ((letter == "y")):
        letter = "f"

    if ((letter == "u")):
        letter = "g"

    if ((letter == "i")):
        letter = "c"

    if ((letter == "o")):
        letter = "r"

    if ((letter == "p")):
        letter = "l"

    if ((letter == "a")):
        letter = "a"

    if ((letter == "s")):
        letter = "o"

    if ((letter == "d")):
        letter = "e"

    if ((letter == "f")):
        letter = "u"

    if ((letter == "g")):
        letter = "i"

    if ((letter == "h")):
        letter = "d"

    if ((letter == "j")):
        letter = "h"

    if ((letter == "k")):
        letter = "t"

    if ((letter == "l")):
        letter = "n"

    if ((letter == ";")):
        letter = "s"

    if ((letter == "z")):
        letter = ";"

    if ((letter == "x")):
        letter = "q"

    if ((letter == "c")):
        letter = "j"

    if ((letter == "v")):
        letter = "k"

    if ((letter == "b")):
        letter = "x"

    if ((letter == "n")):
        letter = "b"

    if ((letter == "m")):
        letter = "m"

    if ((letter == ",")):
        letter = "w"

    if ((letter == ".")):
        letter = "v"

    if ((letter == "/")):
        letter = "z"
    return letter

# Typing loop is started and will end once the test is over
# For this part of the code there is no end condition, so
# loop runs indfinetly
run_test = True

# Loop takes in user input of one character one at a time, changes
# the keystroke into its DVORAK counterpart, and adds it to a string to make a word 
# for a total of five times.
# the word is then 
while (run_test == True):
    i = 0 
    typed_words = ""
    while (i < 5): 

        letter = str(input())
        dvorakletter = ChangeKeyInput(letter)
        typed_words += dvorakletter
        i += 1
    
    print (typed_words)
    







