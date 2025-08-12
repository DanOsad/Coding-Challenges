# https://www.codewars.com/kata/5865cff66b5699883f0001aa

def to_time(s):
    h = s // 3600
    m = s - h * 3600
    return f'{h} hour(s) and {m//60} minute(s)'