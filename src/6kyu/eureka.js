// https://www.codewars.com/kata/5626b561280a42ecc50000d1

const sumDigPow = (a, b) => {
    let r = []
    let pointer = 1
    for (let i=a; i<=b; i++) {
      if (i.toString().length == 1) {
        if (i**pointer == i) {
          r.push(i)
        }
      } else {
        let num = i.toString()
                             .split('')
                             .map((num,ind) => (+num)**(ind+1))
                             .reduce((a,b)=>a+b)
        if (num == i) {
          r.push(num)
        }
      }
    }
    return r
  }