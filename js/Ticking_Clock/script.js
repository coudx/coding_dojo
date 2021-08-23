function getSecondsSinceStartOfDay() {
    return [new Date().getSeconds(), new Date().getMinutes(), new Date().getHours()]
}


// i got it super complicated
setInterval(function() {
    var time = getSecondsSinceStartOfDay();
    console.log(time)
    if (time[0] < 30) {
        document.getElementById('seconds').style.transform = 'rotate(' + (time[0] + 30) * 6 + 'deg)'
    } else {
        document.getElementById('seconds').style.transform = 'rotate(' + (time[0] - 30) * 6 + 'deg)'
    }
    if (time[1] < 30) {
        document.getElementById('minutes').style.transform = 'rotate(' + (time[1] + 30) * 6 + 'deg)'
    } else {
        document.getElementById('minutes').style.transform = 'rotate(' + (time[1] - 30) * 6 + 'deg)'
    }
    if (time[2] < 12) {
        var hr = time[2]
    } else {
        hr = time[2] - 12
    }
    if (hr < 6) {
        document.getElementById('hour').style.transform = 'rotate(' + (hr + 6) * 30 + 'deg)'
    } else {
        document.getElementById('hour').style.transform = 'rotate(' + (hr - 6) * 30 + 'deg)'
    }
}, 1000);