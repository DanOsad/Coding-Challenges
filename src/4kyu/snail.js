// https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

const snail = (arr) => {
    let finalArray = []
    while (arr.length) {
      finalArray.push(...arr.shift())
      for (let i=0; i<arr.length; i++){
        finalArray.push(arr[i].pop())
      }
      finalArray.push(...(arr.pop() || []).reverse())
      for (let i=arr.length-1; i>=0; i--){
        finalArray.push(arr[i].shift())
      }
    }
    return finalArray
}