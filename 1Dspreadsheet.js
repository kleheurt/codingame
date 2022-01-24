/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const N = parseInt(readline());
let inputs = [];
for (let i = 0; i < N; i++) {
    inputs.push(readline().split(' '));
}

/** Solution */
// main processing loop
for (let i = 0; i < N; i++) {
    let x = parserMemo(inputs,i);
    if(x == 0) console.log(0);
    else console.log(x);
}

// memory of already computed values
function parserMemo(arr,pos){
    console.error(arr[pos]);
    if(arr[pos][0] == 'DONE') return arr[pos][1];
    else{
        let tmp = parser(arr,pos);
        arr[pos] = ['DONE', tmp];
        return tmp;
    }
}

// line parsing and computing
function parser(arr, pos){
    switch(arr[pos][0]){
        case 'VALUE' :
            return extr(arr,pos,1);
        case 'ADD':
            return extr(arr,pos,1) + extr(arr,pos,2);
        case 'SUB':
            return extr(arr,pos,1) - extr(arr,pos,2);    
        case 'MULT':
            return extr(arr,pos,1) * extr(arr,pos,2);
        }
}

// links extraction
function extr(arr,pos,pos2){
    if(arr[pos][pos2].charAt(0) == '$') return parserMemo(arr,parseInt(arr[pos][pos2].substring(1)));
    else return safeParseInt(arr[pos][pos2]);
}

// deal with ndash and hyphens
function safeParseInt(str){
    if(str.charAt(0) == '-') return -1 * parseInt(str.substring(1));
    return parseInt(str);
}
