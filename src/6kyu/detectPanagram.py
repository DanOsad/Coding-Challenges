# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string

def is_pangram(s):
    a = list(string.ascii_lowercase)
    c = [l for l in s.lower()]
    for l in a:
        if l in c:
            continue
        else:
            return False
            break
    return True