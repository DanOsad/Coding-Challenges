// Given a two dimensional array, return the co-ordinates of 'x'.
// If 'x' is not inside the array, or if 'x' appears multiple times, return []
// The co-ordinates should be zero indexed.
// You should assume you will always get an array as input. The array will only contain 'x's and 'o's.

const xMarksTheSpot = (input) => {
    let r = []
    for (let i=0; i<input.length; i++){
        if (input[i].includes('x')) {
            r.push([i, input[i].indexOf('x')])
        }  
    }
  	return r.length === 1 ? r[0] : r = []
  }

const testCases = [
    [xMarksTheSpot([]), []],
    [xMarksTheSpot([
                    ['o', 'o'],
                    ['o', 'o']
                ]), []],
    [xMarksTheSpot([
                    ['x', 'o'],
                    ['o', 'x']
                ]), []],
    [xMarksTheSpot([
                    ['x', 'o'],
                    ['o', 'o']
                ]), []],
    [xMarksTheSpot([
        ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o', 'o', 'x', 'o'],
        ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
      ]), [4,6]],
]

function testX(tests){
    for (i=0; i<tests.length; i++){
        console.log(
            tests[i][0] === tests[i][1]
        )
    }
}

testX(testCases)