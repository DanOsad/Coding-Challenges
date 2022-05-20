# https://www.codewars.com/kata/524f5125ad9c12894e00003f

def remainder(a,b):
    if a >= b:
        if b != 0:
            return a % b
        else:
            return None
    if a <= b:
        if a != 0:
            return b % a
        else:
            return None