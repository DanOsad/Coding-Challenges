# https://www.codewars.com/kata/56606694ec01347ce800001b

def is_triangle(a, b, c):
    if b + c <= a:
        return False
    elif a + c <= b:
        return False
    elif a + b <= c:
        return False
    else:
        return True