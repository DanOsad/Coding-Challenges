# https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk):
    origin = [0, 0]
    destination = [0, 0]
    for direction in walk:
        if direction == 'n':
            destination[0] += 1
        elif direction == 's':
            destination[0] -= 1
        elif direction == 'e':
            destination[1] += 1
        elif direction == 'w':
            destination[1] -= 1
    if destination == origin and len(walk) == 10:
        return True
    else:
        return False