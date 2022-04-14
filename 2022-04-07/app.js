// Complete the function that takes two numbers as input, num and nth and return the nth digit of num (counting from right to left).

// Note
// If num is negative, ignore its sign and treat it as a positive value
// If nth is not positive, return -1
// Keep in mind that 42 = 00042. This means that findDigit(42, 5) would return 0

let findDigit = (num, nth) => {
    let r = num.toString().split('').reverse().filter(l => l != '-')
    while (r.length < nth) {
      r.push('0')
    }
    let n = Number(r.join(''))
    return (nth > 0) ? Number(r.join('')[nth-1]) : -1
  }
  
  const testCases = [
        [[5673, 4], 5],
      [[129, 2], 2],
      [[-2825, 3], 8],
      [[-456, 4], 0],
      [[0, 20], 0],
      [[65, 0], -1],
      [[24, -8], -1]
  ]
  
  function testAssertions(tests) {
      for (i=0; i<testCases.length; i++){
        console.log(
            findDigit(testCases[i][0][0], testCases[i][0][1]) == testCases[i][1]
          )
      }
    }
    
  testAssertions(testCases)