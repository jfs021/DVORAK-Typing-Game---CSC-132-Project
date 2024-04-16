import random
from random import randint

#function to take user input for letters
def letterInput():
  numLetter = int(input("How many letters do you want in each word? Please enter 5:"))
  if (numLetter == 5):
    return wordBank(numLetter)
  else:
    letterInput()

#function to create wordbank, takes user input from first function
def wordBank(numLetter):
  if numLetter == 5:
    with open('5letter.txt', 'r') as file:
      lines = file.readlines()
    lines = [line.strip() for line in lines]
  words = []
  for i in range(0,200,1):
    randomNum = randint(0,200)
    words.append(lines[randomNum])
  return words

word = (letterInput())
print(word)

