// Write a function toWeirdCase that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased.

function toWeirdCase(str){
    let r = str.split(' ').map(word=>word.split(''))
    s = ''
    for (i=0; i<r.length; i++){
      r[i].map((l,i)=>{
        return i%2==0 ? s+=l.toUpperCase() : s+= l
      })
      s += ' '
    }
    return s.trim()
  }