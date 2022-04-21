// In this exercise, you will create a function that takes an integer, i. With it you must do the following:
// Find all of its multiples up to and including 100,
// Then take the digit sum of each multiple (eg. 45 -> 4 + 5 = 9),
// And finally, get the total sum of each new digit sum.
// Note: If the digit sum of a number is more than 9 (eg. 99 -> 9 + 9 = 18) then you do NOT have to break it down further until it reaches one digit.

function procedure(n){
    let arr = []
    for (i=1; i<=100; i++){
        if (i%n==0){
            arr.push(i)
        }
    }
    let r = arr.map(n => n
        .toString()
        .split('')
        .reduce((a,c)=>Number(a)+Number(c))
        )
    return r.reduce((a,c)=>a+c)
  }

const testCases = [
    [procedure(30), 18],
    [procedure(12), 72],
    [procedure(49), 30],
    [procedure(17), 48],
    [procedure(10), 46],
]

function testProcedure(tests){
    for (let i=0; i<tests.length; i++){
        console.log(tests[i][0] === tests[i][1])
    }
}

testProcedure(testCases)