# https://www.codewars.com/kata/54e6533c92449cc251001667/python

def unique_in_order(iter):
    i = 0
    j = 0
    r = []
    for item in iter:
        if len(r) and (iter[i] == r[j]):
            continue
        else:
            # r[j] = iter[i]
            r.append(iter[i])
            print(f'Appending {iter[i]} to r: r = {r}')
            j += 1
        i += 1
    return r

tests = [
    ('AAAABBBCCDAABBB', ['A', 'B', 'C', 'D', 'A', 'B']),
    ('ABBCcAD', ['A', 'B', 'C', 'c', 'A', 'D']),
    ([1, 2, 2, 3, 3], [1, 2, 3]),
    ((1, 2, 2, 3, 3), [1, 2, 3])
]

for i, test in enumerate(tests):
    if unique_in_order(test[0]) == test[1]:
        print(f'Test {i} Passed')
    else:
        print(f'Test {i} Failed')