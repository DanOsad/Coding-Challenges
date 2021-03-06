// https://www.codewars.com/kata/55805ab490c73741b7000064
// Complete the function to create backronyms. Transform the given string (without spaces) to a backronym, using the preloaded dictionary and return a string of words, separated with a single space (but no trailing spaces).
// The keys of the preloaded dictionary are uppercase letters A-Z and the values are predetermined words, for example:

const dict = { 
    'A': "awesome", 
    'B': 'beautiful', 
    'C': 'confident', 
    'D': 'disturbing', 
    'E': 'eager', 
    'F': 'fantastic', 
    'G': 'gregarious', 
    'H': 'hippy', 
    'I': 'ingestable', 
    'J': 'joke', 
    'K': 'klingon', 
    'L': 'literal', 
    'M': 'mustache', 
    'N': 'newtonian', 
    'O': 'oscillating', 
    'P': 'perfect', 
    'Q': 'queen', 
    'R': 'rant', 
    'S': 'stylish', 
    'T': 'turn', 
    'U': 'underlying', 
    'V': 'volcano', 
    'W': 'weird', 
    'X': 'xylophone', 
    'Y': 'yogic', 
    'Z': 'zero' 
}

let makeBackronym = string => {
    return string.toUpperCase().split('').map(letter => dict[letter]).join(' ')
}

const testCases = [
    ['dgm', 'disturbing gregarious mustache'],
    ['lkj', 'literal klingon joke'],
    ['interesting', 'ingestable newtonian turn eager rant eager stylish turn ingestable newtonian gregarious'],
    ['codewars', 'confident oscillating disturbing eager weird awesome rant stylish'],
]

function testBackronyms(tests) {
    for (i=0; i<tests.length; i++){
      console.log(
          makeBackronym(tests[i][0]) == tests[i][1]
      )
    }
  }
  
testBackronyms(testCases)