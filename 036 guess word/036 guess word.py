from graphics import *;
from random import *

#window = GraphWin("Window", 500, 500)
#window.setBackground("white")

f = open("text.txt", "r")
words = []
for i in f:
    words.append(i.strip())

randword = words[randint(0,len(words))]
og = randword
scrambled = ""

while len(randword) > 0:
    letter = randint(0, len(randword)-1)
    scrambled += randword[letter]
    randword = randword[0:letter] + randword[letter+1::]

correct = False

while not correct:
    correct = True
    correct_letters = []
    print("\n\nScrambled Word:", scrambled)
    while True:
        guess = input("Enter a guess: ")
        if len(guess) != 5:
            print("Guess must be five letters long")
        else:
            break
        
    for i in range(len(guess)):
        if guess[i] == og[i]:
            correct_letters.append(i)
        else:
            correct = False

    if not correct:
        print("Incorrect")
        print("Letters in correct position: ", end="")
        for i in correct_letters:
            print(guess[i] + " ", end="")

print("Correct!")
