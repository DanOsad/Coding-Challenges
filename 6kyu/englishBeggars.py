# https://www.codewars.com/kata/59590976838112bfea0000fa

def beggars(values, n):
    b = []
    if n > 0:
        for num in range(n):
            t = sum(values[num::n])
            b.append(t)
    else:
        b = []
    return b