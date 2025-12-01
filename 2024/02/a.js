const fs = require('fs');

// Read the file synchronously
const fileContent = fs.readFileSync('./a-input.txt', 'utf-8');

// Split the content by new lines
const lines = fileContent.split(/\r?\n/);

var result = 0;

var i = 0;
for (var line of lines) {
    var data = line.split(" ");
    data = data.map((e) => {return parseInt(e)})

    //console.log(data)

    var valid = true;
    for (var j = 0; j < data.length - 1; j++) {
        if (!valid) {break;}
        var diff = data[j] - data[j + 1];
        if (j == 0) {
            var inc = false;
            if (diff > 0) {
                inc = true;
            }
        }

        if ((diff > 0 && inc == false) || (diff < 0 && inc == true)) {
            valid = false
        }

        diff = Math.abs(diff)

        if (diff == 0 || diff > 3) {
            valid = false
        }
    }

    if (valid) {result++}

    i++
}

console.log(result)