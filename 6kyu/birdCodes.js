// https://www.codewars.com/kata/5a580064e6be38fd34000147

const birdCode = arr => {
    let birds = arr.map(element => element.split(/-| /))
    let r = []
    for (bird of birds) {
      let newName = ''
      if (bird.length < 2) {
        r.push(bird[0].slice(0,4))
      } else if (bird.length < 3) {
        bird.forEach(el => {
          newName += el.slice(0,2)
        })
        r.push(newName)
      } else if (bird.length < 4) {
        for (let i=0; i<bird.length; i++) {
          if (i == 0 || i == 1) {
            newName += bird[i].slice(0,1)
            
          } else {
            newName += bird[i].slice(0,2)
          }
        }
        r.push(newName)
      } else {
        bird.forEach(el => {
          newName += el.slice(0,1)
        })
        r.push(newName)
      }
    }
    return r.map(bird=>bird.toUpperCase())
  }