// https://www.codewars.com/kata/5266876b8f4bf2da9b000362
/* WHO LIKES IT? */
// Implement the function which takes an array containing the names of people that like an item.

function likes(names) {
    return names.length == 0 ? 'no one likes this'
    : names.length == 1 ? `${names[0]} likes this`
    : names.length == 2 ? `${names[0]} and ${names[1]} like this`
    : names.length == 3 ? `${names[0]}, ${names[1]} and ${names[2]} like this`
    : `${names[0]}, ${names[1]} and ${names.length-2} others like this`
  }

const testCases = [
    [likes([]), 'no one likes this'],
    [likes(['Peter']), 'Peter likes this'],
    [likes(['Jacob', 'Alex']), 'Jacob and Alex like this'],
    [likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this'],
    [likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this'],
]

function testNames(tests){
    for (let i=0; i<tests.length; i++){
        console.log(tests[i][0] === tests[i][1])
    }
}

testNames(testCases)