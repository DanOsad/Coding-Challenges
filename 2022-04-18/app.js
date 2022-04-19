// There was a test in your class and you passed it. Congratulations!
// But you're an ambitious person. You want to know if you're better than the average student in your class.
// You receive an array with your peers' test scores. Now calculate the average and compare your score!
// Return True if you're better, else False!

function betterThanAverage(classPoints, yourPoints) {
    classPoints.push(yourPoints)
    return (classPoints.reduce((acc, curr)=> acc + curr, 0) / (classPoints.length)) <= yourPoints ? true : false
  }
  
  const testCases = [
    [betterThanAverage([2, 3], 5), true],
    [betterThanAverage([100, 40, 34, 57, 29, 72, 57, 88], 75), true],
    [betterThanAverage([12, 23, 34, 45, 56, 67, 78, 89, 90], 9), false],
    [betterThanAverage([41, 75, 72, 56, 80, 82, 81, 33], 50), false],
    [betterThanAverage([29, 55, 74, 60, 11, 90, 67, 28], 21), false],
  ]
  
  function testAverage(tests){
      for (let i=0; i<testCases.length; i++){
          console.log(
              tests[i][0] === tests[i][1]
          )
      }
  }