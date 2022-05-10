// Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

function moveZeros(arr) {
    let result = []
    arr.forEach((n,i)=> n===0 ? result.push(i) : null)
    let newArr = arr.filter(n=>n!==0)
    result.forEach(n=>newArr.push(0))
    return newArr
}