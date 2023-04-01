'''Even Numbers Filter'''

numbers = [12, 15, 28, 33, 44, 54]

def filter_even_numbers(numbers):
    new_list = []
    for x in numbers:
        if x % 2 == 0:
            new_list.append(x)
        else:
            continue
    print(new_list)

filter_even_numbers(numbers)

''' Same code but using list comprehension '''

# def filter_even_numbers(numbers):
#     return [x for x in numbers if x % 2 == 0]