// https://www.codewars.com/kata/57a083a57cb1f31db7000028

function powersOfTwo(n){
    p = []
    for (i=0; i<n+1; i++) {
      p.push(2**i)
    }
    return p
  }