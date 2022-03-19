# https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
    nums = [int(n) for n in numbers.split(' ')]
    even = []
    odd = []
    for n in nums:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    if len(even) > len(odd):
        return nums.index(odd[0])+1
    elif len(even) < len(odd):
        return nums.index(even[0])+1