// https://leetcode.com/problems/climbing-stairs

const climbStairs = n => {
    let pre = 1
    let curr = 1
    let temp = 0
    for (let i=1; i<n; i++) {
      temp = curr
      curr = curr + pre
      pre = temp
    }
    return curr
  }