# https://www.codewars.com/kata/58649884a1659ed6cb000072

def update_light(c):
    col = ['green','yellow','red']
    i = 0
    if c == col[0]:
        return col[1]
    elif c == col[1]:
        return col[2]
    elif c == col[2]:
        return col[0]