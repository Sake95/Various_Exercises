''' Vowel Remover'''

string = "Here is the solution!"

def remove_vowels(string):
    new_string = ""
    for char in string:
        if char.lower() not in 'aeiou':
            new_string += char
    print(new_string)

remove_vowels(string)