// Write a function that will check if two given characters are the same case.
// If either of the characters is not a letter, return -1
// If both characters are the same case, return 1
// If both characters are letters, but not the same case, return 0

const sameCase = (a,b) => {
    return a.toLowerCase() === a.toUpperCase() || b.toLowerCase() === b.toUpperCase() ? -1
    : (a === a.toUpperCase() && b === b.toUpperCase()) || (a === a.toLowerCase() && b === b.toLowerCase()) ? 1
    : 0
  }
  
  const testCases = [
      [sameCase('C', 'B'), 1],
      [sameCase('b', 'a'), 1],
      [sameCase('d', 'd'), 1],
      [sameCase('A', 's'), 0],
      [sameCase('c', 'B'), 0],
      [sameCase('b', 'Z'), 0],
      [sameCase('\t', 'Z'), -1],
      [sameCase('H', ':'), -1],
  ]	
  
  function testSameCase(tests){
      for (let i=0; i<testCases.length; i++){
          console.log(
              tests[i][0] === tests[i][1]
          )
      }
  }
  
  testSameCase(testCases)