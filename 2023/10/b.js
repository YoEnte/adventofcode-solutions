const fs = require('fs');
const { parse } = require('path');
const { unescape } = require('querystring');
const { cursorTo } = require('readline');
const fileContent = fs.readFileSync('./b-input.txt', 'utf-8');
const lines = fileContent.split(/\r?\n/);

var pipes = [];
var loop = []
var result = 0;
var spos;
var vectors = {
    'l': [-1, 0],
    'r': [1, 0],
    'u': [0, -1],
    'd': [0, 1]
}
var inverse = {
    'l': 'r',
    'r': 'l',
    'u': 'd',
    'd': 'u'
}
var pieces = {
    '|': ['u', 'd'],
    '-': ['l', 'r'],
    'F': ['r', 'd'],
    '7': ['l', 'd'],
    'L': ['r', 'u'],
    'J': ['l', 'u']
}

function printMap(map) {
    map.forEach((line, i) => {
        console.log(line.join(""));
    });
    console.log("")
}

var width = lines[0].length;

var ground = ('.'.repeat(width)).split("");
// console.log(ground)

lines.forEach((line, y) => {
    _line = [...line.split("")];
    pipes.push(_line);
    loop.push([...ground]);

    _line.forEach((e, x) => {
        if (e == 'S') {
            spos = [x, y];
        }
    });
});

var cpos = [...spos];
var cvec = ''

var skip = false;
var connects = [];
Object.keys(vectors).forEach((v, i) => {
    var newX = cpos[0] + vectors[v][0];
    var newY = cpos[1] + vectors[v][1];
    //console.log(newX, newY, newField, pieces[newField], v, inverse[v])

    if (pipes[newY] == undefined || pipes[newY][newX] == undefined || pipes[newY][newX] == '.') {return}
    var newField = pipes[newY][newX];
    if (pieces[newField].includes(inverse[v])) {
        //console.log("connect", v)
        if (skip) {
            cvec = v;
        }
        connects.push(v);

        skip = true;
    }
});

Object.keys(pieces).forEach((p, i) => {
    if (pieces[p].includes(connects[0]) && pieces[p].includes(connects[1])) {
        loop[cpos[1]][cpos[0]] = p;
    }
});

var count = 1;
while (true) {
    var newX = cpos[0] + vectors[cvec][0];
    var newY = cpos[1] + vectors[cvec][1];
    var newField = pipes[newY][newX];

    if (newField == 'S') {break}

    //console.log(newField)
    loop[newY][newX] = newField;

    if (inverse[cvec] == pieces[newField][0]) {
        cvec = pieces[newField][1];
    } else {
        cvec = pieces[newField][0];
    }

    cpos = [newX, newY];

    count++;
}

var _loop = [];
for (var k of loop) {
    _loop.push([...k]);
}
var inCount = 0;
var y = 0;
for (var line of loop) {
    var x = 0;
    var wallCount = 0;
    var lastCornerVec = undefined;

    for (var l of line) {
        //console.log(l, lastCornerVec)
        if (l == '.') {
            if (wallCount % 2 == 1) {
                inCount++;
                _loop[y][x] = 'I';
            } else {
                _loop[y][x] = 'O';
            }
        } else if (l == '|') {
            wallCount++;
        } else if (l == '-') {
            // pass
        } else {
            if (lastCornerVec === undefined) {
                lastCornerVec = pieces[l][1];
            } else {
                if (lastCornerVec != pieces[l][1]) {
                    wallCount++;
                }
                lastCornerVec = undefined
            }
        }
        x++;
    }
    y++;
}

printMap(pipes);
printMap(loop);
printMap(_loop);

console.log(count, count / 2, inCount)