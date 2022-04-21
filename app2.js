// Given a list of the times you need to brew each coffee, return the minimum total waiting time.
// If you get it right, you will get that raise your boss promised you!

function barista(arr){
    arr.sort((a,b)=>a-b)
    let r = [arr[0]]
    for (i=1;i<arr.length;i++){
      r.push((r[i-1]+arr[i])+2)
    }
      return arr.length > 0 ? r.reduce((a,b)=>a+b) : 0
  }

  const testCases = [
    [barista([2,10,5,3,9]), 85],
    [barista([4,3,2]),22],
    [barista([20,5]),32],
    [barista([20,5,4,3,1,5,7,8]),211],
    [barista([5,4,3,2,1]),55],
]	

function testBarista(tests){
    for (let i=0; i<testCases.length; i++){
        console.log(
            tests[i][0] === tests[i][1]
        )
    }
}

testBarista(testCases)