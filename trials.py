"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_list = []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)
    
    return even_list

def get_odd_indices(items):
    result = []
    for idx, item in enumerate(items):
        if idx % 2 == 1:
            result.append(item)
    return result        


def print_as_numbered_list(items):
    counter = 1

    for item in items:
        print(f"{counter}. {item}")
        counter += 1


def get_range(start, stop):
    nums = []
    
    for num in range(start, stop):
        nums.append(num)

    return nums

def censor_vowels(word):
    chars = []

    for char in word:
        if char in 'aeiou':
            chars.append("*")
        else:
            chars.append(char)
    return ''.join(chars)

def snake_to_camel(string):
    camel_case = []

    for s in string.split('_'):
        camel_case.append(s.title())

    return ''.join(camel_case)

def longest_word_length(words):
    longest = len(words[0])

    for word in words[1:]:
        if longest < len(word):
            longest = len(word)
    return longest

def truncate(string):
    result = []

    for s in string:
        if not result:
            result.append(s)
        if s != result[-1]:
            result.append(s)
    return ''.join(result)


def has_balanced_parens(string):
    parens = 0

    for s in string:
        if s == '(':
            parens += 1
        elif s == ')':
            parens -= 1
            if parens < 0:
                return False
    return parens < 0

def compress(string): # ['aabcc']
    compressed = []

    curr_char = ''
    char_count = 0

    for s in string:
        if s != curr_char:
            compressed.append(s) #['a2b']
            if char_count > 1:
                compressed.append(str(char_count)) #['a2']
            
            curr_char = s
            char_count = 0
        
        char_count += 1

    compressed.append(curr_char)

    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)

print(compress('aabcc'))
            