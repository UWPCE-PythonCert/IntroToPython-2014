// Object.prototype.values = function() { return values(this) }
// Object.prototype.keys = function() { return keys(this) }

function python(file_path) {
    var spawn = require('child_process').spawn,
        py = spawn('python', [file_path]),
        store = ''
    py.stdout.on('data', function (data) { store += data })
    py.stderr.on('data', function (data) { console.log('stderr: ' + data) })
    py.on('close', function (code) { 
        // buck = store 
        console.log(store)
        python = store
    })
}


function isInt(n){
    return typeof n== "number" && isFinite(n) && n%1===0;
}

if (!keys) {
    function keys(arr) {
        var k = []
        for (a in arr) k.push(a)
        return k
    }
}


if (!values) {
    function values(arr) {
        var v = []
        for (a in arr) v.push(arr[a])
        return v
    }
}




function isArray(obj) {
    return Array.isArray(obj)
}

Array.prototype.unique = function () {
    var o = {}

    for (var i = this.length - 1; i >= 0; i--) {
        if (o[this[i]]) {
            o[this[i]].count += 1            
        } else {
            o[this[i]] = {
                count: 1,
                type: typeof(this[i])
            }

        }
    }

    function setkeys(arr) {
        var k = []
        for (a in arr) {
            if (arr[a].type == 'number') {
                if (a.match(/\./gmi)) {
                    k.push(parseFloat(a))
                } else {
                    k.push(parseInt(a))    
                }  
            } else {
                k.push(a)    
            } 
        }
        return k
    }
    return setkeys(o)
}


String.prototype.loop = function () {
    for (i in this) {
        console.log(this[i])
    }
}

String.prototype.trigram = function(str) {
    
    Array.prototype.frequency = function () {
        var o = {}

        for (var i = this.length - 1; i >= 0; i--) {
            if (o[this[i]]) {
                o[this[i]] += 1            
            } else {
                o[this[i]] = 1            
            }
        }
        return o
    }


    function set(str) {  
        var s = str.split(' ')
        var o = {}

        for (var i = 0, g = s.length; i<g; i++) {
            // if (s[i+1] != undefined) {
            if (s[i+1]) {
                var k = s[i] + ' ' + s[i+1]
                if (o[k]) { 
                    o[k].push(s[i+2])
                } else {
                    o[k] = [s[i+2]]
                }
            }
        }
        return o
    }


    function predict(str) {
        var s = set(str)


    }

    return set(this)
}












// function Triagram() {
//     return {
//         set:set,
//         // predict: predict
//     }
// }


// function predict(str) {
 
//     var set = this.set
 
//     // if (set[str]) {
//     //     var x = set[str].frequency()
//     //     var k = keys(x)
//     //     var y = ''

//     //     for (var i = k.length - 1; i >= 0; i--) {
//     //         var a = x[k[i]]
//     //         var b = x[k[i-1]] || 0
//     //         y = (a > b)? k[i]: k[i-1] 
//     //     }


//     //     return y


//     // } else {
//     //     return ''
//     // }

//     return set[str]

// }



// // this version for when setting self object
// function set(str) {  
//     var s = str.split(' ')
//     var o = {}

//     for (var i = 0, g = s.length; i<g; i++) {
//         // if (s[i+1] != undefined) {
//         if (s[i+1]) {
//             var k = s[i] + ' ' + s[i+1]
//             if (o[k]) { 
//                 o[k].push(s[i+2])
//             } else {
//                 o[k] = [s[i+2]]
//             }
//         }
//     }

//     return this.set = o
// }