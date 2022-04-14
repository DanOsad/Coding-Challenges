// We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

// So given a string "super", we should return a list of [2, 4].

function vowelIndices(word){
	let vowels = ['a','e','i','o','u','y']
  let r = []
  for (i=0; i<vowels.length; i++){
  	let idx = word.toLowerCase().indexOf(vowels[i])
    while (idx != -1) {
    	r.push(idx+1)
        idx = word.toLowerCase().indexOf(vowels[i], idx+1)
    }
  }
  return r.sort((a,b)=>a-b)
}

const testCases = [
    [vowelIndices("apple"), [1,5]],
    [vowelIndices("super"), [2,4]],
    [vowelIndices("orange"), [1,3,6]],
    [vowelIndices("supercalifragilisticexpialidocious"), [2,4,7,9,12,14,16,19,21,24,25,27,29,31,32,33]],
]

function testVowelIndices(tests){
    for (i=0; i<tests.length; i++){
        console.log(
            tests[i][0] === tests[i][1]
        )
    }
}

testVowelIndices(testCases)