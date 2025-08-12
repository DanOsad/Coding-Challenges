# https://www.codewars.com/kata/57cc981a58da9e302a000214

def small_enough(array, limit):
    for n in array:
        if n <= limit:
            continue
        else:
            return False
    return True