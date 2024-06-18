#!/usr/bin/node
const cp = process.argv.length;
console.log(cp === 2 ? 'No argument' : cp === 3 ? 'Argument found' : 'Argument found');
