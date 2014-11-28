#!/usr/bin/env node 

String.prototype.startswith = function(text) {
    return this.substr(0,text.length) == text
}


Array.prototype.append = Array.prototype.push


// def read_in_data(infilename):

//     infile = open(infilename, 'r') # text mode is default
//     # strip out the header, table of contents, etc.
//     for i in range(61):
//         infile.readline()

//     full_text = []
//     # read the rest of the file line by line
//     for line in infile:
//         if line.startswith("End of the Project Gutenberg EBook"):
//             break
//         full_text.append(line)

//     # put all the lines together into one big string:
//     return " ".join(full_text)

var fs = require('fs')

function read_in_data (infilename) {
	var infile = fs.readFileSync(infilename,'utf8')
	infile = infile.split('\n')
	return infile.join(' ')

}