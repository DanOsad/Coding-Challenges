# https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(s):
    y = []

    for num in [x for x in range(1, 10)]:
        for word in s.split(' '):
            if str(num) in word:
                y.append(word)
    return ' '.join(x for x in y)