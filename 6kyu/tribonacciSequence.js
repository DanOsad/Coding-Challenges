// https://www.codewars.com/kata/556deca17c58da83c00002db
// As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next.

function tribonacci(signature,n){
    let [a,b,c] = [signature[0], signature[1], signature[2]]
    let r = []
    let d = 0
    r.push(a,b,c)
    let i = 2
    while (i < n-1) {
      r.push[signature[i]]
        d = r[i-2]+r[i]+r[i-1]
      r.push(d)  
      i++
    }
    return r.length<1 ? [] 
    : n == 1 ? [r[0]]
    : n == 0 ? []
    : r
  }

  const testCases = [
    [tribonacci([1,1,1],10),[1,1,1,3,5,9,17,31,57,105]],
    [tribonacci([0,0,1],10),[0,0,1,1,2,4,7,13,24,44]],
    [tribonacci([0,1,1],10),[0,1,1,2,4,7,13,24,44,81]],
    [tribonacci([1,0,0],10),[1,0,0,1,1,2,4,7,13,24]],
    [tribonacci([0,0,0],10),[0,0,0,0,0,0,0,0,0,0]],
    [tribonacci([1,2,3],10),[1,2,3,6,11,20,37,68,125,230]],
    [tribonacci([3,2,1],10),[3,2,1,6,9,16,31,56,103,190]],
]	

function testTribonacci(tests){
    for (let i=0; i<testCases.length; i++){
        console.log(
            tests[i][0] === tests[i][1]
        )
    }
}

testTribonacci(testCases)