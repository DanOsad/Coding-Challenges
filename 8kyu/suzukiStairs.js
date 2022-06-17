//https://www.codewars.com/kata/56fc55cd1f5a93d68a001d4e

const stairsIn20 = stairs => {
    let result = 0
    stairs.forEach(dayOfWeek => dayOfWeek.forEach(amount => result += amount))
    return result * 20
}