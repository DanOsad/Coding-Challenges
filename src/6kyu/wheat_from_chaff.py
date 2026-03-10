# https://www.codewars.com/kata/5bdcd20478d24e664d00002c/train/python

def wheat_from_chaff(values):
    i = 0
    j = len(values) - 1
    
    while i < j:
        if values[j] > 0:
            j -= 1
            continue
        if values[i] > 0:
            values[i], values[j] = values[j], values[i]
        else:
            i += 1
            
    return values