// https://www.codewars.com/kata/558fc85d8fd1938afb000014

function sumTwoSmallestNumbers(numbers) {  
    let nums = numbers.sort((a,b)=>a-b)
    return nums[0] + nums [1]
  }