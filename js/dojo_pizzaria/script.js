function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crust = crustType;
    pizza.sauce = sauceType;
    pizza.cheese = cheeses;
    pizza.topping = toppings;
    return pizza;
}

function randomTopping() {
    var topping = ['sausage', 'pepperoni', 'mushrooms', 'olives', 'onions', 'pineapple', 'ham'];
    var selTopping = [];
    for (var i = 0; i < 2; i++) {
        selTopping.push(topping[Math.floor(Math.random() * topping.length)])
    }
    return selTopping;
}

function randomCheese() {
    var cheese = ['mozzarella', 'feta', 'jack']
    var selCheese = [];
    for (var i = 0; i < 1; i++) {
        selCheese.push(cheese[Math.floor(Math.random() * cheese.length)])
    }
    return selCheese;
}

function randomCrust() {
    var crust = ['stuffed', 'cracker', 'flat bread', 'thin', 'thick', 'deep dish', 'hand tossed']
    return crust[Math.floor(Math.random() * crust.length)]
}

function randomSauce() {
    var sauce = ['Spicy Red', 'Peppery Red', 'Sweet', 'Pesto', 'Alfredo', 'BBQ', 'tranditional', 'marinara']
    return sauce[Math.floor(Math.random() * sauce.length)]
}

function randomPizza() {
    return pizzaOven(randomCrust(), randomSauce(), randomCheese(), randomTopping())
}

var pizzas = []

pizzas.push(pizzaOven('deep dish', 'traditional', ['mozzarella'], ['pepperoni', 'sausage']))

pizzas.push(pizzaOven('hand tossed', 'marinara', ['mozzarella', 'feta'], ['mushrooms', 'olives', 'onions']))

pizzas.push(randomPizza())
pizzas.push(randomPizza())

console.log(pizzas)