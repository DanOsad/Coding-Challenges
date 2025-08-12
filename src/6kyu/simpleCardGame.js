// https://www.codewars.com/kata/53417de006654f4171000587

const winner = (deckSteve, deckJosh) => {
    const values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    let x = 0 //steve points
    let y = 0 //josh points
    while (deckSteve.length > 0){
      if (values.indexOf(deckSteve[0]) > values.indexOf(deckJosh[0])) {
        x++
        deckSteve.shift()
        deckJosh.shift()
      }else if (values.indexOf(deckSteve[0]) < values.indexOf(deckJosh[0])) {
        y++
        deckSteve.shift()
        deckJosh.shift()
      }else {
        deckSteve.shift()
        deckJosh.shift()
      }
    }
    return x > y ? `Steve wins ${x} to ${y}`
                :y > x ? `Josh wins ${y} to ${x}`
                : "Tie"
}