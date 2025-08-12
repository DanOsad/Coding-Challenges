// https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

const solution = str => {
    splitString = str.split('')
    pairs = []
    while (splitString.length > 1) {
        let pair = `${splitString.shift()}${splitString.shift()}`
        pairs.push(pair)
    }
    if (splitString.length == 1) {
        let pair = `${splitString.shift()}_`
        pairs.push(pair)
    }
    return pairs
}