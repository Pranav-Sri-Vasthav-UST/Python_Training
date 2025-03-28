# import the file
import strops

print('-'*80)
print("Welcome to the String Operations")

def test():
    while(True):
        print(f'''
            {'-'*80}
            1. GetSpan
            2. ReverseWords
            3. RemovePunctuation
            4. CountWords
            5. CharecterMaps
            6. MakeTitle
            7. NormalizeSpaces
            8. Transform
            9. GetPermutation
            10. Exit
            {'-'*80}
        ''')
        option = int(input("Please select the one option: "))
        if option == 1:
            text = input("Enter the main string: ")
            substring = input("Enter the substring to find: ")
            print(strops.spansub(text, substring))
        elif option == 2:
            text = input("Enter the string to reverse words: ")
            print(strops.reverseWords(text))
        elif option == 3:
            text = input("Enter the string to remove punctuation: ")
            print(strops.removePunctuation(text))
        elif option == 4:
            text = input("Enter the string to count words: ")
            print(strops.countWords(text))
        elif option == 5:
            text = input("Enter the string for character map: ")
            print(strops.charecterMap(text))
        elif option == 6:
            text = input("Enter the string to make title: ")
            print(strops.makeTitle(text))
        elif option == 7:
            text = input("Enter the string to normalize spaces: ")
            print(strops.normalize_spaces(text))
        elif option == 8:
            text = input("Enter the string to transform (reverse and swap case): ")
            print(strops.transform(text))
        elif option == 9:
            text = input("Enter the string to get permutations: ")
            permutations = strops.getPermutations(text)
            print(f"Type1 - {[list(item) for item in permutations]}")
            print(f'Type2 - {permutations}')
        elif option == 10:
            print("Exiting the program...")
            break
        else:
            print("Invalid option, please try again.")

