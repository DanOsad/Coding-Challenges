# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    sum = 0
    for num in str(n):
        sum += int(num)
    if sum > 9:
        sum = digital_root(sum)
    return sum