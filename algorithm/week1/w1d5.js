function reverse(arr) {
    var rev = [];
    while (arr.length > 0) {
        rev.push(arr.pop())
    }
    return rev;
}

function reverseOringalArr(arr) {
    var tmp = "";
    for (var i = 0; i < arr.length / 2; i++) {
        tmp = arr[i];
        arr[i] = arr[arr.length - (i + 1)];
        arr[arr.length - (i + 1)] = tmp
    }
    return arr;
}

var ourarry = ["a", "b", "c", "d", "e"];
console.log(reverse(ourarry))
var ourarry = ["a", "b", "c", "d", "e"];
console.log(reverseOringalArr(ourarry))