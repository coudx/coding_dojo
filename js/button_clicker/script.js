function click_login() {
    document.getElementById("login").textContent = "Logout"
}

function remove() {
    var e = document.getElementById("def");
    e.parentNode.removeChild(e);
}

document.getElementById("login").onclick = function() { click_login() };
document.getElementById("like0").onclick = function() { alert("Ninja was liked") };
document.getElementById("like1").onclick = function() { alert("Ninja was liked") };
document.getElementById("def").onclick = function() { remove() };