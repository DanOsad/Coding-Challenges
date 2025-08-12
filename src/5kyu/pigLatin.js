// https://www.codewars.com/kata/520b9d2ad5c005041100000f

const pigIt = str => {
    let words = str.split(' ').map(word=>word.split(''))
    for (word of words) {
      if (/[a-zA-Z]/.test(word)) {
        let firstLetter = word.shift()
        word.push(firstLetter,'a','y')
      }
    }
    return words.map(word=>word.join('')).join(' ')
  }