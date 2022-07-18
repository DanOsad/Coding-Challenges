// https://www.codewars.com/kata/523f5d21c841566fde000009

const arrayDiff = (a,b) => {
    let i = 0
    if (a.length > 0 && b.length > 0) {
    while (i < b.length) {
      a = a.filter(num=>num!==b[i])
      i++
      }
    }
    return a
  }