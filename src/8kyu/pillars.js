// https://www.codewars.com/kata/5bb0c58f484fcd170700063d

function pillars(num_pill, dist, width) {
    if (num_pill < 2) {
      return 0;
    } else {
    return (((num_pill-2)*width)+((num_pill-1)*(dist*100)))
    }
  }