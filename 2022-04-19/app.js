// Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
// we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.

function digPow(n, p){
    let numArr = n.toString().split('').map(Number)
    let newNumArr = []
    for (let i=0; i<numArr.length; i++){
      newNumArr.push(numArr[i]**p)
      p+=1
    }
    let r = newNumArr.reduce((a,c)=>a+c) / n
    return Number.isInteger(r) === true ? r : -1 
  }
  
  const testCases = [
    [digPow(89, 1), 1],
    [digPow(92, 1), -1],
    [digPow(46288, 3), 51],
  ]
  
  function testDigPow(tests){
    for (let i=0; i<tests.length; i++){
      console.log(tests[i][0] === tests[i][1])
    }
  }
  
  testDigPow(testCases)