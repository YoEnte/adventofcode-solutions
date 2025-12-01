const fs = require('fs');
const { parse } = require('path');
const { cursorTo } = require('readline');
const fileContent = fs.readFileSync('./b-input.txt', 'utf-8');
const lines = fileContent.split(/\r?\n/);

var histories = [];
var result = 0;

for (var line of lines) {
    histories.push([...line.split(" ")].map(str => parseInt(str)));
}

for (var h of histories) {
    layers = [[...h]];

    var len = h.length;
    for (var l = 0; l < len; l++) {
        layer = layers[l];
        var allZero = true;
        
        var preSave = [];
        for (var e = 1; e < layers[l].length; e++) {
            if (layers[l][e] != 0) {allZero = false}
            preSave.push(layers[l][e] - layers[l][e - 1]);
            //console.log(layers[l][e], layers[l][e] - layers[l][e - 1], e, allZero);
        }

        if (allZero) {
            break;
        }

        layers.push([...preSave])
    }

    //console.log(layers);
    var extendLayers = [...layers];

    for (var i = layers.length - 1; i >= 0; i--) {
        //console.log(i);

        if (i == layers.length - 1) {
            extendLayers[i].push(0);
        } else {
            var add = extendLayers[i][0] - extendLayers[i + 1][0];
            extendLayers[i].unshift(add);

            if (i == 0) {result += add}
        }
    }

    //console.log(extendLayers);
}

console.log(result);