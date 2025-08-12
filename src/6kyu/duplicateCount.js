// https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

const duplicateCount = str => {
    if ( str.length==0 ) { return 0 }
    let count = {}
    str = str.split('').map(l=>l.toLowerCase())
    for (val of str) {
      if (!count[val]) {
        count[val] = 1
      } else {
        count[val] += 1
      }
    }
    let result = 0
    for (key in count) {
      if (count[key] > 1) {
        result += 1
      }
    }
    return result
  }