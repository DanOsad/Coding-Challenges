// https://www.codewars.com/kata/55b42574ff091733d900002f
// Make a program that filters a list of strings and returns a list with only your friends name in it.
// If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

function friend(friends){
    let r = []
    for (i=0; i<friends.length;i++){
        if (friends[i].split('').length == 4) {
        r.push(friends[i])
        }
    }
    return r
}

const testCases = [
    [friend(["Ryan", "Kieran", "Mark"]), ["Ryan", "Mark"]],
    [friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"]],
    [friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"]],
    [friend(["Love", "Your", "Face", "1"]), ["Love", "Your", "Face"]],
    ]	

function testFriends(tests){
    for (let i=0; i<testCases.length; i++){
        console.log(
            tests[i][0] === tests[i][1]
        )
    }
}

testFriends(testCases)