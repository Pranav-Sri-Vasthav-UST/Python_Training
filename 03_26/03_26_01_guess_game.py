'''
    Jumbled Word: "otpcomure"
    Your Guess: "computer"
    ✅ Correct! 

'''

import random

# function to jumble the word

def jumble(w):
    temp = list(w)
    random.shuffle(temp)
    return ''.join(temp)


# Welcome message

print("\n")
print("Welcome to the WORD JUMBLE GAME")
print("-" * 80)

print("The computer presents a jumbled word")
print("You need to guess it. For every correct guess")
print("you will be offered a point")
print("-" * 80)

# Get the words and process it 
f = open(r"D:\Python Training\Python_Training\03_26\words.txt")
content = f.read()
f.close()

f = open(r"D:\Python Training\Python_Training\03_26\hints.txt")
hints = f.read()
f.close()

content = content.split(',')
hints = hints.split('\n')

fruits = content[:6]
vegis = content[6:]

guess_count_1 = 0
guess_count_2 = 0
points_count = 0
guess_count_1_items = []
guess_count_2_items = []
wrong_guess_items = []



# print("INFO content -> ", content)

points = 0

# for every word in list of words
random.shuffle(content)

for word in content:

    print("\n")

    # jumble the word
    jumbled_word = jumble(word)

    for i in range(2):
        print(jumbled_word)
        user_word = input("Can you guess -> ")
        if ((user_word == word) and (i==0)):
            points+=2
            guess_count_1 +=1
            guess_count_1_items.append(word)
            break
        elif((user_word != word) and (i==0)):
            if word in fruits:
                print(f"hints: {hints[0]}, The first letter is {word[0]}")
                print('')
            else:
                print(f"hints: {hints[1]}, The first letter is {word[0]}")
                print('')
        if(user_word == word and i==1):
            points+=1
            guess_count_2 +=1
            guess_count_2_items.append(word)
        else:
            points +=0

wrong_guess_items = [item for item in content if item not in (guess_count_1_items+guess_count_2_items)]
print("")
print("-" * 80)
print("")
print(f"The total points scored --- {points}, The Guesses are {guess_count_1_items+guess_count_2_items}")
print("")
print(f"no.of items guessed in first attepmt --- {guess_count_1}, The Guesses are {guess_count_1_items}")
print("")
print(f"no.of items guessed in second attepmt --- {guess_count_2}, The Guesses are {guess_count_2_items}")
print("")
print(f"The Guesses that went wrong are  --- {wrong_guess_items}")
print("")

print("-" * 80)

if (points>15 and (guess_count_1 ==9 and guess_count_2==0)):
    print("O-outstanding")
elif(points>=15 and (guess_count_1 >=6 and guess_count_2<=3)):
    print("A-Very good")
elif(points>=12 and (guess_count_1 >=4 and guess_count_2<=5)):
    print("B-good")
elif(points>=8 and (guess_count_1 >=2 and guess_count_2<=7)):
    print("c-Average")
else:
    print("please improve your vocabulaby")

print("-" * 80)