# https://www.codewars.com/kata/57a429e253ba3381850000fb

def bmi(weight, height):
    bmiCalc = float(weight/height**2)
    if bmiCalc <= 18.5:
        return "Underweight"
    elif bmiCalc <= 25.0:
        return "Normal"
    elif bmiCalc <= 30.0:
        return "Overweight"
    elif bmiCalc > 30.0:
        return "Obese"