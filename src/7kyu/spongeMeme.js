// https://www.codewars.com/kata/5982619d2671576e90000017

const spongeMeme = s => {
    return s.toLowerCase().split('').map((l,i) => i%2==0 ? l.toUpperCase() : l).join('')
  }