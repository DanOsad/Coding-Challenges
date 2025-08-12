# https://www.codewars.com/kata/555eded1ad94b00403000071

def series_sum(n):
    s = []
    for num in range(1, n + 1):
        if n > 0:
            s.append(1 / ((num * 2) + (num - 2)))
        else:
            return 0
    return '{:.2f}'.format(sum(s))