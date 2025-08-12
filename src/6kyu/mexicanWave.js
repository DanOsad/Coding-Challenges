// https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

const wave = str => {
    let r = []
    for (let i=0; i<str.length; i++) {
      if (str[i] == ' ') continue
      r.push(Array.from(str,(letter,j) => i===j ? letter.toUpperCase() : letter).join(''))
    }
    return r
  }