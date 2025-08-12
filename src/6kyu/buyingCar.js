// https://www.codewars.com/kata/554a44516729e4d80b000012

function nbMonths(carValue, purchase, saving, percent){
    let depreciation = percent / 100
    let month = 0
    let totalSaved = carValue
    while (totalSaved < purchase) {
      month++
      if (month % 2 == 0) {
        depreciation += .005
      }
      carValue *= 1 - depreciation
      purchase *= 1 - depreciation
      totalSaved = carValue + (saving*month)
    }
    return [month, Math.round(totalSaved-purchase)]
  }