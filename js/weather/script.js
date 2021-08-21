// create object for each day weather card
var cards = [{
        day: 'Today',
        icon: 'assets/some_rain.png',
        weather_stat: 'some rain',
        high: 75,
        low: 65
    },
    {
        day: 'Tomorrow',
        icon: 'assets/some_sun.png',
        weather_stat: 'some sun',
        high: 80,
        low: 66
    },
    {
        day: 'Friday',
        icon: 'assets/some_clouds.png',
        weather_stat: 'some clouds',
        high: 69,
        low: 61
    },
    {
        day: 'Saturday',
        icon: 'assets/some_sun.png',
        weather_stat: 'some sun',
        high: 78,
        low: 70
    }
]

// generate a div element that display a weather card
function genCard(info, unit) {
    let card = document.createElement('div')
    card.className = 'card'
    let day = document.createElement('p')
    day.textContent = info.day
    let icon = document.createElement('img')
    icon.src = info.icon
    let stat = document.createElement('p')
    stat.textContent = info.weather_stat
    let temp = document.createElement('div')
    let hi = document.createElement('p')
    let low = document.createElement('p')
    if (unit == 'c') {
        hi.textContent = Math.floor((info.high - 32) * 5 / 9)
        low.textContent = Math.floor((info.low - 32) * 5 / 9)
    } else {
        hi.textContent = info.high
        low.textContent = info.low
    }
    temp.appendChild(hi)
    temp.appendChild(low)
    card.appendChild(day)
    card.appendChild(icon)
    card.appendChild(stat)
    card.appendChild(temp)
    return card
}

function spanCard() {
    var weather = document.getElementById('weather')
    weather.innerHTML = ''
    cards.forEach(e => weather.appendChild(genCard(e, document.getElementById('unit').value)))
}

// create and span the cookie accept element
function cookieAccept() {
    var parent = document.getElementById('weather').parentNode
    let box = document.createElement('div')
    box.className = 'cookie'
    let msg = document.createElement('div')
    msg.innerHTML = '<h1>Stop! Cookie time</h1><p>We use cookies (sadly not the edible ones) to personalize content and ads, to provide social media features and to analyse our traffic. <a href="">Read more...</a></p>'
    let icon = document.createElement('img')
    icon.src = 'assets/cookie.png'
    let btn = document.createElement('button')
    btn.textContent = 'I Accept'
    box.appendChild(icon)
    box.appendChild(msg)
    box.appendChild(btn)
    parent.appendChild(box)
}

spanCard()
cookieAccept()

// get button element from DOM, add onlick trigger, 
// remove parents element node when click
document.getElementsByTagName('button')[0].onclick = (e) => e.path[1].remove()

console.log('page loaded...')