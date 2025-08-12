// https://www.codewars.com/kata/59c053f070a3b7d19100007e

const distanceFromLine = ([ax,ay],[bx,by],[cx,cy]) => {
    const dist = (x1,y1,x2,y2) => Math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if (ax == bx && ay == by) {
      return dist(ax,ay,cx,cy)
    }
    const ab = dist(ax,ay,bx,by)
    const ac = dist(ax,ay,cx,cy)
    const bc = dist(bx,by,cx,cy)
    const p = (ab+bc+ac) / 2
    return Math.sqrt(p * (p - ab) * (p - bc) * (p - ac)) * 2 / ab
  }