// https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9

var number=function(array){
    r = []
    for (i=0; i<array.length; i++) {
      r.push(`${i+1}: ${array[i]}`)
    }
    return r
  }