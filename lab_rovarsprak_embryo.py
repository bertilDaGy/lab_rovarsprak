'''lab_rovarsprak_embryo.py

    Here's the framework for lab rövarspråk

    BLu 230919
'''

# decide if a character is a vowel or not
# e.g. is_vowel('a') -> True
#      is_vowel('k') -> False

def is_vowel(ch):
    # enter code here
    return False

def rovarsprak(text):
    # Doesn't work that good yet, fix it!

    result = ''
    for c in text:
         result += c

    return result

# Run the program
if __name__ == '__main__':

    answer = input('Mata in en text:')
    while answer :
        print(rovarsprak(answer))
        answer = input('Mata in en text:')
 