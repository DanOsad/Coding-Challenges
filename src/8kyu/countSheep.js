// https://www.codewars.com/kata/5b077ebdaf15be5c7f000077

var countSheep = function (num){
    let r = ''
    if (num > 0) {
      for (i=1; i<=num; i++) {
        r += `${i} sheep...`
      }
    } else if (num == 0) {
      return ""
    }
    return r
  }