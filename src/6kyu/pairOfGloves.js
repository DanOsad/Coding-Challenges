// https://www.codewars.com/kata/58235a167a8cb37e1a0000db

const numberOfPairs = gloves => {
    let arr = gloves.map(i=>i).sort()
    let pairs = 0
    for (let i=0; i<arr.length; i++) {
      if (arr[i] == arr[i+1]) {
        pairs ++
        i+=1
      }
    }
    return pairs
}