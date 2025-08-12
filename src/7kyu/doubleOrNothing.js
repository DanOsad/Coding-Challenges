// https://www.codewars.com/kata/5d378318e04cd7001ad72a27

function doubleOrNothing(cash, wager, rounds){
    for (i=1; i<rounds; i++) {
      wager *= 2
    }
    return wager<=cash ? cash-wager : "I'll pay you back later"
  }