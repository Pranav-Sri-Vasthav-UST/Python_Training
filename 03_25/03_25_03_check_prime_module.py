# Program to take user input and filter all prime numbers
# Also print the missing prime numbers in the range

import primes
import copy

# input
print("Enter your data: ")
userData = []
while True:
    userInput = input(" -> ")
    if(userInput == "!"):
        break
    else:
        if(userInput.isdigit()):
            userData.append(int(userInput))


# processing

minInput = min(userData)
maxInput = max(userData)
allPrimes = primes.getAllPrimes(minInput, maxInput) # tuple (n, [])
userPrimes = []
for number in userData:
    if(primes.checkprime(number)):
        userPrimes.append(number)

userPrimes = list(set(userPrimes))
print("INFO: userPrimes -> ", userPrimes)

# Yeshwath
missingPrimes = list(copy.deepcopy(allPrimes))[1] # makes a proper copy
print("INFO: missingPrimes -> ", missingPrimes)
for item in userPrimes:
    missingPrimes.remove(item)

# Akshay
missingPrimes2 = [item for item in allPrimes[1] if item not in userPrimes]

# Purushotham
missingPrimes3 = set(userPrimes) ^ set(allPrimes[1])

missingPrimesCount = allPrimes[0] - len(userPrimes)

# output

print('-' * 80)
print(" Missing Primes Count : ", missingPrimesCount)
print(" Missing Primes       : ", missingPrimes)
print(" Missing Primes       : ", missingPrimes2)
print(" Missing Primes       : ", missingPrimes3)


'''
[19, 37, 47]

[11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

[11, 13, 17, 23, 29, 31,  41, 43]

'''