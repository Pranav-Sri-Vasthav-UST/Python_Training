# imports
import string
from collections import Counter
import itertools

#Global_variables
getspan_list = []

#process

# Function - getspan(s, ss) – Returns the start and end index (span) of substring ss in string s.

def spansub(string_in, substring_in):
    substring_length = len(substring_in)
    for i in range(len(string_in)):
        sub_string = substring_length+i
        if substring_in == string_in[i:sub_string]:
            getspan_list.append((i,sub_string))

    return len(getspan_list), getspan_list

# Function - reverseWords(s) – Reverses the order of words in s. 

def reverseWords(s):
    words = s.split()
    '''
    to reverse the each word
        for i in words:
        reversed_words.append(i[::-1]) 
        reversed_words.reverse()
    '''
    return ' '.join(words[::-1])


# Function - removePunctuation(s) – Removes all Punctuation from s. 

def removePunctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

removePunctuation("Hello, Pranav! Let's remove Punctuations.")


# Function - countWords(s) – Counts the number of words in s.

def countWords(s):
    list_of_words = s.split()
    return len(list_of_words)

countWords("hi hi hi hello")

'''
Function - charecterMap(s) – Returns a dictonary with characters of s as keys and their frequencies as 
values. 
'''

def charecterMap(s):
    return Counter(s)

charecterMap("hi hi hi")

# Function - makeTitle(s) – Converts s to title case.

def makeTitle(s):
    return s.title()

makeTitle("hi hi hi")

# Function - normalizeSpaces(s) – Removes extra spaces, leaving only single spaces between words. 

def normalize_spaces(text):
    return ' '.join(text.split())


# Function -  transform(s) – Reverses the string and swaps case (e.g., "Hello" → "OLLEh").

def transform(s):
    reversed_string = s[::-1]
    transformed_string = reversed_string.swapcase()
    return transformed_string

transform('Hello')


# Function -  getPermutations(s) – Returns all Permutations of the string s.

def getPermutations(s):
    if len(s) <= 1:
        return [s]
    
    result = []
    for i, char in enumerate(s):
        for perm in getPermutations(s[:i] + s[i+1:]):
            result.append(char + perm)

    list_of_permutations = list(result)
    
    return list_of_permutations


'''
Another way to do it:
    print(list(itertools.permutations('hiii')))
'''
