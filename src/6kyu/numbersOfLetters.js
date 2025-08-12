// https://www.codewars.com/kata/599febdc3f64cd21d8000117

const numbersOfLetters = n => {
    const nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
    let r = [n.toString().split('').map(letter=>parseInt(letter)).map(num=>nums[num]).join('')]
    let lastNum = r[0]
    while (lastNum.length != nums.indexOf(lastNum)) {
      r.push(lastNum.length > nums.length-1 ? lastNum.length.toString().split('').map(letter=>parseInt(letter)).map(num=>nums[num]).join('') : nums[lastNum.length])
      lastNum = r[r.length-1]
    }
    return r
  }