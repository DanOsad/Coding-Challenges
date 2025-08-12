// https://www.codewars.com/kata/541c8630095125aba6000c00

function digital_root(n) {
    let result = n.toString().split('').map(n=>+n).reduce((a,c)=>a+c)
    return result.toString().length > 1 ? digital_root(result) : result
  }