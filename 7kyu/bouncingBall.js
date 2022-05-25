// https://www.codewars.com/kata/5a40c250c5e284a76400008c

function bouncingBall(initial, proportion) {
    let current = initial
    let count = 0
    while (current > 1) {
      current *= proportion
      count++
    }
    return count
  }