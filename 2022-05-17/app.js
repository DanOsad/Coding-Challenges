// Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

const persistence = num => {
    let r = num.toString().split('').map(n=>+n).reduce((a,b)=>a*b)
    let count = 1
    if (num.toString().split('').length < 2) {
      return 0
    } else {
        while (r.toString().length > 1) {
            r = r.toString().split('').map(n=>+n).reduce((a,b)=>a*b)
            count++
        }
    }
    return count
}

const testCases = [
    [persistence(39),3],
    [persistence(4),0],
    [persistence(25),2],
    [persistence(999),4],
]

const testPersistence = tests => {
    tests.forEach(test=>console.log(test[0]===test[1]))
}

testPersistence(testCases)