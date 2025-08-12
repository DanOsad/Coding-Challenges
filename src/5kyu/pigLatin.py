# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    s = text.split(" ")
    n = []
    for word in s:
        if word.isalpha():
            if len(word) == 1:
                n.append(f"{word}ay")
            else:
                n.append(f"{word[1:]}{word[0]}ay")
        else:
            n.append(word)
    return ' '.join(n)