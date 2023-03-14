#!/usr/bin/node
const fs = require('fs');
/*
 * In this script, we first import the fs module to read and write files. We
 * then get the file paths of the two source files (file1 and file2) and the
 * destination file (dest) from the command line arguments using process.argv.
 */
const fir = fs.readFileSync(process.argv[2], 'utf8');
const las = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFileSync(process.argv[4], fir + las);
