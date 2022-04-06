# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0

def solve(arr):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = [x for x in range(0, 26)]
    alpha = dict(zip(letters, numbers))
    solve_list = []
    for word in arr:
        l = [c.lower() for c in word]
        i = 0
        letter_counter = 0
        for letter in l:
            if i == alpha[l[i]]:
                letter_counter += 1
                i += 1
            else:
                i += 1
        solve_list.append(letter_counter)
    return solve_list