// https://www.codewars.com/kata/546e2562b03326a88e000020
// In this kata, you are asked to square every digit of a number and concatenate them.
// For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
// Note: The function accepts an integer and returns an integer

const squareDigits = num => Number(Array.from(String(num)).map(e=>Number(e)**2).join(''))

const testCases = [
    [squareDigits(9350639), 81925036981],
    [squareDigits(5659654), 25362581362516],
    [squareDigits(9966496), 81813636168136],
    [squareDigits(4894156), 1664811612536],
    [squareDigits(6111279), 3611144981],
    [squareDigits(8578829), 6425496464481],
    [squareDigits(6391644), 369811361616],
    [squareDigits(9576753), 8125493649259],
    [squareDigits(9478676), 81164964364936],
    [squareDigits(3808456), 964064162536],
    [squareDigits(5557606), 2525254936036],
    [squareDigits(7421261), 4916414361],
    [squareDigits(9336518), 81993625164],
]

function testFilterList(tests){
    for (let i=0; i<tests.length; i++){
        return tests[i][0] == tests[i][1]
    }
}

testFilterList(testCases)