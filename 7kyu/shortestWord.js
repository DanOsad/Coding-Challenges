// https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

function findShort(s){
    let r = s.split(' ')
    let lengthList = []
    for (i=0; i<r.length; i++) {
      lengthList.push(r[i].length)
    }
    return lengthList.sort((a,b)=>a-b)[0]
  }