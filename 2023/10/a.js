const fs = require('fs');
const { parse } = require('path');
const { cursorTo } = require('readline');
const fileContent = fs.readFileSync('./a-input.txt', 'utf-8');
const lines = fileContent.split(/\r?\n/);

var pipes = [];
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

lines.forEach((line, y) => {
    _line = [...line.split("")];
    pipes.push(_line);

    _line.forEach((e, x) => {
        if (e == 'S') {
            spos = [x, y];
        }
    });
});

var cpos = [...spos];
var cvec = ''

var skip = false;
Object.keys(vectors).forEach((v, i) => {
    if (skip) {return}
    var newX = cpos[0] + vectors[v][0];
    var newY = cpos[1] + vectors[v][1];
    var newField = pipes[newY][newX];
    //console.log(newX, newY, newField, pieces[newField], v, inverse[v])

    if (newField == '.' || newField == undefined) {return}
    if (pieces[newField].includes(inverse[v])) {
        //console.log("connect", v)
        cvec = v;
        skip = true;
    }
});

var count = 1;
while (true) {
    var newX = cpos[0] + vectors[cvec][0];
    var newY = cpos[1] + vectors[cvec][1];
    var newField = pipes[newY][newX];

    if (newField == 'S') {break}

    //console.log(newField)

    if (inverse[cvec] == pieces[newField][0]) {
        cvec = pieces[newField][1];
    } else {
        cvec = pieces[newField][0];
    }

    cpos = [newX, newY];

    count++;
}

console.log(count, count / 2)