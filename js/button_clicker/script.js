// change textcontent of item id login to logout
function click_login() {
    document.getElementById("login").textContent = "Logout"
}

// remove item id def
function remove() {
    var e = document.getElementById("def");
    e.parentNode.removeChild(e);
}

// add onlick detection
document.getElementById("login").onclick = function() { click_login() };
document.getElementById("like0").onclick = function() { alert("Ninja was liked") };
document.getElementById("like1").onclick = function() { alert("Ninja was liked") };
document.getElementById("def").onclick = function() { remove() };