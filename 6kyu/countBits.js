// https://www.codewars.com/kata/526571aae218b8ee490006f4

const countBits = num => {
    return Array.from(num.toString(2)).filter(n=>n=='1').length
  }