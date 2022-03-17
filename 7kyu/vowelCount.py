# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(input_str):
    num_vowels = 0
    vowels = ['a','e','i','o','u']
    for x in vowels:
        num = input_str.count(x)
        num_vowels += num
    
    return num_vowels