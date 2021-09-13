/** @format */

var cards

// create object for each day weather card
const parseData = async(e) => {
        console.log(e)
        var parsed = [{
                day: "Today",
                icon: e[0].day.condition.icon,
                weather_stat: e[0].day.condition.text,
                high: e[0].day.maxtemp_f,
                low: e[0].day.mintemp_f,
            },
            {
                day: "Tomorrow",
                icon: e[1].day.condition.icon,
                weather_stat: e[1].day.condition.text,
                high: e[1].day.maxtemp_f,
                low: e[1].day.mintemp_f,
            },
            {
                day: "Day after Tomorrow",
                icon: e[2].day.condition.icon,
                weather_stat: e[2].day.condition.text,
                high: e[2].day.maxtemp_f,
                low: e[2].day.mintemp_f,
            },
        ]
        return parsed
    }
    // generate a div element that display a weather card
const genCard = async(info, unit) => {
    console.log("*****Generating Cards*****")
    let card = document.createElement("div")
    card.className = "card"
    let day = document.createElement("p")
    day.textContent = await info.day
    let icon = document.createElement("img")
    icon.src = info.icon
    let stat = document.createElement("p")
    stat.textContent = await info.weather_stat
    let temp = document.createElement("div")
    let hi = document.createElement("p")
    let low = document.createElement("p")
    hi.textContent = await (unit == "c" ?
        Math.floor(((info.high - 32) * 5) / 9) :
        info.high)
    low.textContent = await (unit == "c" ?
        Math.floor(((info.low - 32) * 5) / 9) :
        info.low)
    temp.appendChild(hi)
    temp.appendChild(low)
    card.appendChild(day)
    card.appendChild(icon)
    card.appendChild(stat)
    card.appendChild(temp)
    console.log(card)
    document.getElementById("weather").appendChild(card)
}

const spanCard = async() => {
    console.log("about to span the card")
    var weather = document.getElementById("weather")
    weather.innerHTML = ""
    for (var i = 0; i < cards.length; i++) {
        genCard(cards[i], document.getElementById("unit").value)
    }
}

const search = async() => {
    console.log("function search called")
    var loc = document.getElementById("loc").value
    var data = await fetch(
            "https://forward-reverse-geocoding.p.rapidapi.com/v1/search?q=" +
            loc +
            "&accept-language=en&polygon_threshold=0.0", {
                method: "GET",
                headers: {
                    "x-rapidapi-host": "forward-reverse-geocoding.p.rapidapi.com",
                    "x-rapidapi-key": "3160f91b0dmsh7300af528512412p16e1bajsn48961a9d5dd3",
                },
            }
        )
        .then((response) => response.json())
        .catch((err) => {
            console.error(err)
        })
    cards = await fetch(
            "https://weatherapi-com.p.rapidapi.com/forecast.json?q=" +
            data[0].lat +
            "," +
            data[0].lon +
            "&days=5", {
                method: "GET",
                headers: {
                    "x-rapidapi-host": "weatherapi-com.p.rapidapi.com",
                    "x-rapidapi-key": "3160f91b0dmsh7300af528512412p16e1bajsn48961a9d5dd3",
                },
            }
        )
        .then((res) => res.json())
        .then((e) => {
            document.getElementById("title").textContent = `${e.location.name}`
            console.log("title changed")
            return parseData(e.forecast.forecastday)
        })
        .catch((err) => {
            console.error(err)
        })
    spanCard()
}

// create and span the cookie accept element
function cookieAccept() {
    var parent = document.getElementById("weather").parentNode
    let box = document.createElement("div")
    box.className = "cookie"
    let msg = document.createElement("div")
    msg.innerHTML =
        '<h1>Stop! Cookie time</h1><p>We use cookies (sadly not the edible ones) to personalize content and ads, to provide social media features and to analyse our traffic. <a href="">Read more...</a></p>'
    let icon = document.createElement("img")
    icon.src = "assets/cookie.png"
    let btn = document.createElement("button")
    btn.textContent = "I Accept"
    btn.id = "accept"
    box.appendChild(icon)
    box.appendChild(msg)
    box.appendChild(btn)
    parent.appendChild(box)
}

const run = async() => {
    cards = await fetch(
            "https://weatherapi-com.p.rapidapi.com/forecast.json?q=los%20angeles&days=5", {
                method: "GET",
                headers: {
                    "x-rapidapi-host": "weatherapi-com.p.rapidapi.com",
                    "x-rapidapi-key": "3160f91b0dmsh7300af528512412p16e1bajsn48961a9d5dd3",
                },
            }
        )
        .then((res) => res.json())
        .then((e) => {
            console.log(e.location.name)
            document.getElementById("title").textContent = `${e.location.name}`
            console.log("title changed")
            return parseData(e.forecast.forecastday)
        })
        .catch((err) => console.error(err))
    console.log("******************************")
    console.log(cards)
    spanCard()
    console.log("page loaded...")
}

// get button element from DOM, add onlick trigger,
// remove parents element node when click
cookieAccept()
document.getElementById("accept").onclick = (e) => e.path[1].remove()
run()