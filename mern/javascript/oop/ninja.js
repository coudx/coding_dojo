/** @format */

class ninja {
    constructor(name, health) {
        this.name = name
        this.health = health
        this.speed = 3
        this.strength = 3
    }

    sayName() {
        console.log(this.name)
    }

    showStats() {
        console.log("Name: " + this.name)
        console.log("Health: " + this.health)
        console.log("Speed: " + this.speed)
        console.log("Strength: " + this.strength)
    }

    drinkSake() {
        this.health += 10
    }
}