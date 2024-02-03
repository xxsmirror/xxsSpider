function reverse(unicodeData){
    return String.fromCharCode(unicodeData);
}
let a = reverse('\ua123')
console.log(a);