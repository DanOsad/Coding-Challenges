// https://www.codewars.com/kata/513e08acc600c94f01000001

const rgb = (r,g,b) => {
    const convertToHex = n => {
      n < 0 ? hex = '00' : 
      n > 255 ? hex = 'ff' : 
      hex = n.toString(16)
      return hex.length == 1 ? '0'+hex.toUpperCase() : hex.toUpperCase()
    }
    return `${convertToHex(r)}${convertToHex(g)}${convertToHex(b)}`
}

console.log(rgb(0, 0, 0))// '000000'
console.log(rgb(0, 0, -20))// '000000'
console.log(rgb(300,255,255))// 'FFFFFF'
console.log(rgb(173,255,47))// 'ADFF2F'