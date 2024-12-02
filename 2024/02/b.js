const fs = require('fs');

// Read the file synchronously
const fileContent = fs.readFileSync('./b-input.txt', 'utf-8');

// Split the content by new lines
const lines = fileContent.split(/\r?\n/);

var result = 0;
var unsafes = [];

var i = 0;
for (var line of lines) {
    var data = line.split(" ");
    data = data.map((e) => {return parseInt(e)})

    //console.log(data)

    var valid = true;
    for (var j = 0; j < data.length - 1; j++) {
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
        
        if (!valid) {unsafes.push(data); break;}
    }

    if (valid) {result++}

    i++
}

console.log(unsafes);

for (var u of unsafes) { // each of unsafe reports
    var totalValid = 0;
    for (var i in u) {
        var copyU = [...u];
        copyU = copyU.filter((e, x) => {if (i == x) {return null} else {return e}});
        console.log(copyU)

        var valid = true;
        for (var j = 0; j < copyU.length - 1; j++) {
            var diff = copyU[j] - copyU[j + 1];
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
            
            if (!valid) {break;}
        }

        if (valid) {totalValid++}
    }

    if (totalValid > 0) {result++}
}

console.log(result)