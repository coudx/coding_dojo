/** @format */

class card {
    constructor(name, cost) {
        this.name = name
        this.cost = cost
    }
}

class unitcard {
    constructor(name, cost, power, resilience) {
        super(name, cost)
        this.power = power
        this.resilience = resilience
    }

    attack(unit) {
        console.log(this.name + " attacked " + unit.name)
        console.log(
            this.name + " made " + this.power - unit.resilience + "damage."
        )
    }
}

class effectcard {
    constructor(name, cost, text, stat, magnitud) {
        super(name, cost)
        this.text = text
        this.stat = stat
        this.magnitud = magnitud
    }

    play(unit) {
        if (stat == "resilience") {
            unit.resilience += this.magnitud
        } else if (stat == "power") {
            unit.power += this.power
        }
        console.log(this.name + " is played on " + unit.name)
        console.log(this.text)
    }
}

const red = unitcard("Red Belt Ninja", 3, 3, 4)
const ha = effectcard(
    "Hard Algorithm",
    2,
    "increase target's resilience by 3",
    "resilience",
    3
)
ha.play(red)
const black = unitcard("Black Belt Ninja", 4, 5, 4)
const upr = effectcard(
    "Unhandled Promise Rejection",
    1,
    "reduce target's resilience by 2",
    "resilience", -2
)
upr.play(red)
const pp = effectcard(
    "Pair Programming",
    3,
    "increase target's power by 2",
    "power",
    2
)
pp.play(red)
red.attack(black)