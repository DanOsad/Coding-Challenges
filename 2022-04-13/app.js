// Complete the square sum function so that it squares each number passed into it and then sums the results together.

function squareSum(numbers){
    let sum = 0
    for (let i=0; i<numbers.length; i++){
      sum += numbers[i]**2
    }
    return sum
  }

const testCases = [
    [squareSum([1,2]), 5],
    [squareSum([0, 3, 4, 5]), 50],
    [squareSum([]), 0],
]

function testSquareSum(tests){
    for (let i=0; i<testCases.length; i++){
        console.log(
            tests[i][0] === tests[i][1]
        )
    }
}

testSquareSum(testCases)