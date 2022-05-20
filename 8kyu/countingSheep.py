# https://www.codewars.com/kata/54edbc7200b811e956000556

def count_sheeps(sheep):
    counter = 0
    for i in sheep:
        if i == True:
            counter += 1
        else:
            continue
    return counter