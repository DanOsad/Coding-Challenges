// https://www.codewars.com/kata/5a523566b3bfa84c2e00010b

function minSum(arr) {
    arr.sort((a,b)=>b-a)
    frontArr = arr.slice(0,arr.length/2)
    backArr = arr.slice(arr.length/2).sort((a,b)=>a-b)
    let sum = 0
    for (let i=0; i<frontArr.length; i++) {
      sum += frontArr[i] * backArr[i]
    }
    return sum
}