// detect keypress usage on calculator instead of pressing on button
document.onkeypress = (e) => {
    console.log(e)
    switch (e.keyCode) {
        case 48:
            press(0)
            break
        case 49:
            press(1)
            break
        case 50:
            press(2)
            break
        case 51:
            press(3)
            break
        case 52:
            press(4)
            break
        case 53:
            press(5)
            break
        case 54:
            press(6)
            break
        case 55:
            press(7)
            break
        case 56:
            press(8)
            break
        case 57:
            press(9)
            break
        case 191:
            setOP('/')
            break
        case 56:
            setOP('*')
            break
        case 187:
            setOP('+')
            break
        case 189:
            setOP('-')
            break
        case 190:
            press('.')
            break
    }
}

// enter the number into display when button or key pressed
function press(e) {
    $('#display')[0].textContent == 0 ? $('#display')[0].textContent = e : $('#display')[0].textContent = $('#display')[0].textContent + e
}

// clr the display to 0
function clr() {
    $('#display')[0].textContent = 0
}

// add the operator to display
function setOP(e) {
    $('#display')[0].textContent == 0 ? $('#display')[0].textContent = 0 : $('#display')[0].textContent = $('#display')[0].textContent + e
}

// calculate the input function
function calculate() {
    $('#display')[0].textContent = eval($('#display')[0].textContent.toString())
}