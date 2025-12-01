const fs = require('fs');

// Read the file synchronously
const fileContent = fs.readFileSync('./a-input.txt', 'utf-8');

// Split the content by new lines
const lines = fileContent.split(/\r?\n/);

var left = []
var right = []

var i = 0;
for (var line of lines) {
    var numleft = line.substring(0, line.indexOf(" "));
    left.push(parseInt(numleft))
    
    var numRight = line.substring(line.indexOf(" ") + 3);
    right.push(parseInt(numRight))

    i++
}

//console.log(left)
//console.log(right)

left.sort()
right.sort()

//console.log(left)
//console.log(right)

var result = [];
for (var i = 0; i < left.length; i++) {
    result.push(Math.abs(left[i] - right[i]));
}

console.log(result.reduce((total, current) => total + current, 0))