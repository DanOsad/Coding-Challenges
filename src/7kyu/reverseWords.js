// https://www.codewars.com/kata/5259b20d6021e9e14c0010d4

function reverseWords(str) {
    let i = str.split(' ') // split sentence into words
    let j = i.map(n => n.split('')) // split words into letters
    let k = j.map(n => n.reverse()) // reverse letters
    let q = k.map(n => n.join('')).join(' ')
    return q
  }