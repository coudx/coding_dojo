// function to change name to "new name"
function changeName() {
    document.getElementById("name").textContent = "New Name";
}

function bonus(e) {

    switch (e) {
        case 'a1':
            var element = document.getElementById('a');
            console.log(element);
            element.remove();
            var n = parseInt(document.getElementById("cr").textContent);
            document.getElementById("cr").textContent = n - 1;
            break;
        case 'a0':
            var element = document.getElementById('a');
            console.log(element);
            element.remove();
            var n = parseInt(document.getElementById("cs").textContent);
            document.getElementById("cs").textContent = n + 1;
            break;
        case 'b1':
            var element = document.getElementById('b');
            console.log(element);
            element.remove();
            var n = parseInt(document.getElementById("cr").textContent);
            document.getElementById("cr").textContent = n - 1;
            break;
        case 'b0':
            var element = document.getElementById('b');
            console.log(element);
            element.remove();
            var n = parseInt(document.getElementById("cs").textContent);
            document.getElementById("cs").textContent = n + 1;
            break;
    }
}