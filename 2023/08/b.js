const fs = require('fs');
const fileContent = fs.readFileSync('./b-input.txt', 'utf-8');
const lines = fileContent.split(/\r?\n/);

var scheme = ""
var desertMap = {}
var pos = []
var depth = 0

var i = 0;
for (var line of lines) {
    if (i == 0) {
        scheme = line
    } else if (i >= 2) {
        var key = line.substring(0, line.indexOf(" ="))
        var value1 = line.substring(line.indexOf("(") + 1, line.indexOf(","))
        var value2 = line.substring(line.indexOf(",") + 2, line.indexOf(")"))
        desertMap[key] = [value1, value2]

        if (key.endsWith('A')) {
            pos.push(key)
        }
    }

    i++
}

var importOld = true
if (importOld) {
    var depth = 1777115964223
    pos = [ 'SCZ', 'NJC', 'KPK', 'NQQ', 'NQZ', 'GVZ' ] 
}

while (true) {

    var zCounter = 0;
    var move = depth % scheme.length;
    var side = 0
    if (scheme[move] == "R") {
        side = 1
    }

    var nextSteps = []
    for (p of pos) {
        var nextP = desertMap[p][side]
        nextSteps.push(nextP)
        if (nextP.endsWith('Z')) {
            zCounter++
        }
    }

    pos = [...nextSteps]
    depth++

    if (zCounter >= 3) {
        console.log(depth, pos, scheme[move], "###   ".repeat(zCounter))
    }

    if (zCounter == pos.length) {
        break
    }
}

console.log(scheme)
console.log(desertMap)
console.log(depth)