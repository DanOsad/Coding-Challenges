// https://www.codewars.com/kata/577a98a6ae28071780000989

var min = function(list){
    list.sort((a,b)=>a-b)
    return list[0];
}

var max = function(list){
    list.sort((a,b)=>b-a)
    return list[0];
}