'''Palindrome Exercise'''

strings = ["racecar", "brother", "peacan"]

def filter_palindromes(strings):
    palindromes = []
    for string in strings:
        if string == string[::-1]:
            palindromes.append(string)
    print(palindromes)

filter_palindromes(strings)