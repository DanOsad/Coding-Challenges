# https://www.codewars.com/kata/53368a47e38700bd8300030d

def namelist(list):
    names = []
    if len(list) > 1:
        for item in list:
            for k, v in item.items():
                names.append(v)
        foreNames = ', '.join(names[0:len(names) - 1])
        finalName = f'& {names[-1]}'
        return f'{foreNames} {finalName}'
    elif len(list) == 1:
        for item in list:
            for k, v in item.items():
                names.append(v)
        return f'{names[0]}'
    else:
        return ''