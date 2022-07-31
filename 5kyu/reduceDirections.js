// https://www.codewars.com/kata/550f22f4d758534c1100025a

const dirReduc = arr => {
    let dir = arr.join(" ")
    let dir2 = dir.replace("NORTH SOUTH", "").replace("SOUTH NORTH", "").replace("EAST WEST", "").replace("WEST EAST", "")
    let dir3 = dir2.split(" ").filter(item => item.length > 1)
    return dir3.length < arr.length ? dirReduc(dir3) : dir3
  }