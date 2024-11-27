const fs = require('fs');
const { parse } = require('path');
const { cursorTo } = require('readline');
const fileContent = fs.readFileSync('./a-input-test.txt', 'utf-8');
const lines = fileContent.split(/\r?\n/);

function printMap(map) {
    map.forEach((line, i) => {
        console.log(line.join(""));
    });
    console.log("")
}

var space = [];
var _space = [];
var c = 0;
lines.forEach((line, y) => {
    _line = [...line.split("")];
    space.push([..._line]);
    _space.push([..._line]);

    _line.forEach((e, x) => {
        if (e == '#') {
            c++;
            _space[y][x] = c.toString();
        }
    });
});






printMap(space)
printMap(_space)