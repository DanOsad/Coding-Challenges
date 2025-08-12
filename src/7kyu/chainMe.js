// https://www.codewars.com/kata/54fb853b2c8785dd5e000957

function chain(input, fs) {
    let r
    for (let i=0; i<fs.length; i++) {
      if (i == 0) {
        r = fs[i](input)
      } else {
      r = fs[i](r)
      }
    }
    return r
}