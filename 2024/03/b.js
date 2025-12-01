const exp = require('constants');
const fs = require('fs');

// Read the file synchronously
const fileContent = fs.readFileSync('./b-input.txt', 'utf-8');

// Split the content by new lines
const lines = fileContent.split(/\r?\n/);

var result = 0;

var pattern = /(do(n't)?\(\))|(mul\([0-9][0-9]*,[0-9][0-9]*\))/ig

var active = true;
for (var line of lines) {
    var resolve = [];

    while (match = pattern.exec(line)) {
        
        resolve.push(line.substring(match.index, pattern.lastIndex));
    }

    console.log(resolve)

    for (var r of resolve) {
        if (r == 'do()') {active = true}
        else if (r == "don't()") {active = false}
        else if (active) {
            var num1 = parseInt(r.substring(4, r.indexOf(',')))
            var num2 = parseInt(r.substring(r.indexOf(',') + 1, r.length - 1))
            result += num1 * num2;
        }
    }
}

console.log(result);