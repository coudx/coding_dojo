document.getElementById("myvid").addEventListener("mouseover", function() {
    this.play();
});

document.getElementById("myvid").addEventListener("mouseleave", function() {
    this.pause();
});

console.log("page loaded...");