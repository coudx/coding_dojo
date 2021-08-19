var likect = [0, 0, 0];
var like = document.getElementsByClassName("like")

// Reset all likes count to 0 since we dont have a database to read
for (var i = 0; i < like.length; ++i) {
    like[i].getElementsByTagName('p')[0].innerHTML = likect[i] + " Like(s)"
}

// add 1 to corresponding like count and then update the inner html of p tag
function liked(n) {
    likect[n]++;
    document.getElementById("p" + n).innerHTML = likect[n] + " Like(s)"
}