// Given a string of words, you need to find the highest scoring word.
// Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
// You need to return the highest scoring word as a string.
// If two words score the same, return the word that appears earliest in the original string.
// All letters will be lowercase and all inputs will be valid.

function high(x){
    let a = "abcdefghijklmnopqrstuvwxyz".split('')
    let r = x.split(' ').map(word=>word.split(''))
    let v = []
    for (let i=0; i<r.length; i++){
      let l=0
      for (let j=0; j<r[i].length; j++){
        l+=a.indexOf(r[i][j])+1
      }
      v.push(l)
    }
    return x.split(' ')[v.indexOf(Math.max(...v))]
}

testCases = [
    [high('man i need a taxi up to ubud'), 'taxi'],
    [high('what time are we climbing up the volcano'), 'volcano'],
    [high('take me to semynak'), 'semynak'],   
    [high('aa b'), 'aa'],
    [high('b aa'), 'b'],
    [high('bb d'), 'bb'],
    [high('d bb'), 'd'],
    [high('aaa b'), 'aaa'],
]

function testHigh(tests){
    tests.forEach(test=>console.log(test[0]===test[1]))
}

testHigh(testCases)