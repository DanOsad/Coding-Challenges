// https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

const sortArray = arr => {
    let oddsArray = arr.filter(num=>num%2!==0).sort((a,b)=>a-b)
    arr.forEach((num,i) => {
      if (arr[i]%2==0) {
        oddsArray.splice(i,0,arr[i])
      }
    })
    return oddsArray
  }