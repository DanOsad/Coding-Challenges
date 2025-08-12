# https://www.codewars.com/kata/5202ef17a402dd033c000009

def title_case(title, minor_words=''):
    words = [c.lower() for c in title.split(' ')]
    minors = [c.lower() for c in minor_words.split(' ')]
    print(minors)
    sent = []
    for word in words:
        if word in minors:
            sent.append(word.lower())
        else:
            sent.append((word.lower().capitalize()))
    if sent[0] in minors:
        sent[0] = sent[0].capitalize()
    return ' '.join(sent)