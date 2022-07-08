// https://www.codewars.com/kata/52685f7382004e774f0001f7

const humanReadable = seconds => {
    let hh = Math.floor((seconds % 31536000) / 3600).toString()
    let mm = Math.floor((((seconds % 31536000) % 86400) % 3600) / 60).toString()
    let ss = Math.floor((((seconds % 31536000) % 86400) % 3600) % 60).toString()
    return `${hh.length<2 ? '0'+hh : hh}:${mm.length<2 ? '0'+mm : mm}:${ss.length<2 ? '0'+ss : ss}`
  }