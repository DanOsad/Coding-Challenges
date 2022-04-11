// Create a function that takes an array of letters, and combines them into words in a sentence.

function arrAdder(arr) {
    let r = []
    for (i=0; i<arr[0].length; i++){
      for (j=0; j<arr.length; j++){
          r.push(arr[j][i])
      }  
      r.push(' ')
    }
    return r.join('').trim()
}

const testCases = [
    [
        arrAdder(
        [['J','L','L','M'],
        ['u','i','i','a'],
        ['s','v','f','n'],
        ['t','e','e','']]
        ), 
        "Just Live Life Man"
    ]
    [
        arrAdder(
        [[ 'T', 'M', 'i', 't', 'p', 'o', 't', 'c' ],
        [ 'h', 'i', 's', 'h', 'o', 'f', 'h', 'e' ],
        [ 'e', 't', '', 'e', 'w', '', 'e', 'l' ],
        [ '', 'o', '', '', 'e', '', '', 'l' ],
        [ '', 'c', '', '', 'r', '', '', '' ],
        [ '', 'h', '', '', 'h', '', '', '' ],
        [ '', 'o', '', '', 'o', '', '', '' ],
        [ '', 'n', '', '', 'u', '', '', '' ],
        [ '', 'd', '', '', 's', '', '', '' ],
        [ '', 'r', '', '', 'e', '', '', '' ],
        [ '', 'i', '', '', '', '', '', '' ],
        [ '', 'a', '', '', '', '', '', '' ]]
        ), 
        "The Mitochondria is the powerhouse of the cell"
    ]
]

function testArrAdder(tests){
    for (i=0; i<tests.length; i++){
        console.log(
            tests[i][0] === tests[i][1]
        )
    }
}

testArrAdder(testCases)