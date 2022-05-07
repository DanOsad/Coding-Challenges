// Find the area of a rectangle when provided with one diagonal and one side of the rectangle. If the input diagonal is less than or equal to the length of the side, return "Not a rectangle". If the resultant area has decimals round it to two places.

const area = (d,l) => d>l ? +(Math.sqrt(d**2-l**2)*l).toFixed(2) : "Not a rectangle"

const testCases = [
    [area(10,6),48],
    [area(5,4),12],
    [area(13,5),60],
    [area(12,5),54.54],
]

function testArea(tests){
    tests.forEach(test=>console.log(test[0]===test[1]))
}

testArea(testCases)