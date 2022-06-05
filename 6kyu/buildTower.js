// https://www.codewars.com/kata/576757b1df89ecf5bd00073b

function towerBuilder(nFloors) {
    let tow = []
    spaces = 0
    for (let i=nFloors; i>0; i--) {
      let floor = ' '.repeat(spaces) + '*'.repeat((i*2)-1) + ' '.repeat(spaces)
      tow.unshift(floor)
      spaces += 1
    }
    
    return tow
  }