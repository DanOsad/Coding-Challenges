# https://www.codewars.com/kata/57e92e91b63b6cbac20001e5

import math

def duty_free(price, discount, holiday_cost):
    discounted_price = price * discount * .01
    cover_holiday_cost = holiday_cost // discounted_price
    return cover_holiday_cost