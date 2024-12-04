const exp = require('constants');
const fs = require('fs');

// Read the file synchronously
const fileContent = fs.readFileSync('./a-input.txt', 'utf-8');

// Split the content by new lines
const lines = fileContent.split(/\r?\n/);

var result = 0;

var pattern = /mul\([0-9][0-9]*,[0-9][0-9]*\)/ig

for (var line of lines) {
    while (match = pattern.exec(line)) {
        var expr = line.substring(match.index, pattern.lastIndex);
        var num1 = parseInt(expr.substring(4, expr.indexOf(',')))
        var num2 = parseInt(expr.substring(expr.indexOf(',') + 1, expr.length - 1))
        console.log(match.index, pattern.lastIndex, expr, num1, num2)
        result += num1 * num2;
    }
}

console.log(result);