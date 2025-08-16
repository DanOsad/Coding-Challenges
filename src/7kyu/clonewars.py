# https://www.codewars.com/kata/58ddffda929dfc2cae0000a5

def clonewars(kata_per_day):
    # r = []
    clones = 0
    kata_solved = 1
    able_to_solve = kata_per_day
    for i in range(kata_per_day):
        clones += 1
        able_to_solve -= 1
        kata_solved = ((kata_solved + able_to_solve) * clones) - kata_solved
        print(f"clones: {clones}, kata_solved: {kata_solved}, able_to_solve: {able_to_solve}")

    return [clones, kata_solved]

print(clonewars(0) == [1, 0])
print(clonewars(1) == [1, 1])
print(clonewars(5) == [16, 57])
print(clonewars(10) == [512, 2036])