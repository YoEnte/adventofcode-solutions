const fs = require('fs');

// Read the file synchronously
const fileContent = fs.readFileSync('./b-input.txt', 'utf-8');

// Split the content by new lines
const lines = fileContent.split(/\r?\n/);

var left = []
var right = {}

var i = 0;
for (var line of lines) {
    var numleft = line.substring(0, line.indexOf(" "));
    left.push(numleft)
    
    var numRight = line.substring(line.indexOf(" ") + 3);
    if (right[numRight] == undefined) {
        right[numRight] = 1;
    } else {
        right[numRight]++;
    }

    i++
}

var result = 0

for (l of left) {
    if (right[l] != undefined) {
        result += right[l] * parseInt(l);
    }
}
console.log(result)