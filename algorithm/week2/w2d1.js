// Dice Roller
// Using what we've learned about the Math library in JavaScript, complete the following function that should return a value between 1 through 6 at random.
function d6() {
    var roll = Math.floor(Math.random() * 6 + 1);
    // your code here
    return roll;
}

var playerRoll = d6();
console.log("The player rolled: " + playerRoll);

// Consult the Oracle
// Using the following array, write a function that will answer all of our questions by randomly choosing a response
var lifesAnswers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
];

var answer = (ans) => ans[Math.floor(Math.random() * ans.length)]

console.log(answer(lifesAnswers))