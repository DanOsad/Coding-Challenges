// https://www.codewars.com/kata/5506b230a11c0aeab3000c1f

function evaporator(content, evap_per_day, threshold){ 
    let days = 0
    let newContent = content
    while (newContent > content * threshold / 100) { 
      days++
      newContent -= newContent*evap_per_day/100
    }
    return days
}