
def int_to_roman(num):
    r_map = [
        [1000, "M"],
        [900, "CM"],
        [500, "D"],
        [400, "CD"],
        [100, "C"],
        [90, "XC"],
        [50, "L"],
        [40, "XL"],
        [10, "X"],
        [9, "IX"],
        [5, "V"],
        [4, "IV"],
        [1, "I"],
    ]

    roman = ""

    while num > 0:
        for val, rom in r_map:
            if num >= val:
                roman += rom
                num -= val
                break
    
    return roman


print(int_to_roman(3999))