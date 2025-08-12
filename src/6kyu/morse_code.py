# https://www.codewars.com/kata/54b724efac3d5402db00065e

from preloaded import MORSE_CODE

def decode_morse(morse_code):
    spaces = 0
    r = ''
    morse_split = morse_code.strip().split(' ')
    for letter in morse_split:
        if spaces == 2:
            r += ' ' 
            spaces = 0
        if letter ==  '':
            spaces += 1
        else:
            r += MORSE_CODE[letter]
    return r