function get_neighbourhood(type, arr, coordinates){
    let r = []
    if ((coordinates[0] && coordinates[1] > arr.length) || (coordinates[0] && coordinates[1] < 0)){
        if (type == 'von_neumann'){
        r.push(
            arr[coordinates[0]-1][coordinates[1]],
            arr[coordinates[0]+1][coordinates[1]],
            arr[coordinates[0]][coordinates[1]-1],
            arr[coordinates[0]][coordinates[1]+1],
        )
        }else if (type == 'moore'){
        r.push(
            arr[coordinates[0]-1][coordinates[1]],
            arr[coordinates[0]-1][coordinates[1]-1],
            arr[coordinates[0]-1][coordinates[1]+1],
            arr[coordinates[0]+1][coordinates[1]],
            arr[coordinates[0]+1][coordinates[1]+1],
            arr[coordinates[0]+1][coordinates[1]-1],
            arr[coordinates[0]][coordinates[1]-1],
            arr[coordinates[0]][coordinates[1]+1],
        )
        }else if (arr === []){
        return r
        }
    }else{
      return r
    }
    return r.sort((a,b)=>a-b)
  }