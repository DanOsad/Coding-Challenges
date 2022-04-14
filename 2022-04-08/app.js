// The BOPE is the squad of special forces of police that usually handles the operations in the Favelas in Rio de Janeiro.

// In this Kata you have to write a function that determine the number of magazines that every soldier has to have in his bag.

// You will receive the weapon and the number of streets that they have to cross. Considering that every street the officer shoots 3 times. Bellow there is the relation of weapons:

// PT92 - 17 bullets
// M4A1 - 30 bullets
// M16A2 - 30 bullets
// PSG1 - 5 bullets

function magNumber(info){
    const ammo = {
      "PT92": 17,
      "M4A1": 30,
      "M16A2": 30,
      "PSG1": 5,
    }
    return Math.ceil(info[1]*3/ammo[info[0]])
  }
  
const testCases = [
        [["PT92", 6], 2],
        [["M4A1", 8], 1],
        [["M16A2", 19], 2],
        [["PSG1", 31], 19],
        [["PT92", 19], 4]
]

function testMagNumber(tests) {
  for (i=0; i<testCases.length; i++){
    console.log(
        magNumber(testCases[i][0]) == testCases[i][1]
    )
  }
}

testMagNumber(testCases)