/**
 * /*
 *   Sum To One Digit
 *   Implement a function sumToOne(num)​ that,
 *   given a number, sums that number’s digits
 *   repeatedly until the sum is only one digit. Return
 *   that final one digit result.
 *   Tips:
 *     to access digits from a number, need to convert it .toString() to access each digit via index
 *     parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
 *     isNaN(arg) used to check if something is NaN
 *
 * @format
 */

const num1 = 5
const expected1 = 5

const num2 = 10
const expected2 = 1

const num3 = 25
const expected3 = 7

/**
 * Sums the given number's digits until the number becomes one digit.
 * @param {number} num The number to sum to one digit.
 * @returns {number} One digit.
 * 1. character numberlize check
 *    - return false immediately when there is a nonint in the given "num" ** num is a given var not a predefined int
 * 2. do the calcuation, and the check if the sum if greater than 10
 *    - greater or equal loop algo
 *    - lesser return the value
 */
// function sumToOneDigit(num) {
//     let arr = num.toString().split("")
//     let sum = 0
//     for (var i = 0; i < arr.length; i++) {
//         if (parseInt(arr[i] === NaN)) {
//             return false
//         } else {
//             sum += parseInt(arr[i])
//         }
//     }
//     // return sum > 10 ? sumToOneDigit(sum) : sum
//     if (sum > 10) {
//         return sumToOneDigit(sum)
//     } else {
//         return sum
//     }
// }

// demo of semi one line coding.
function sumToOneDigit(num) {
    let sum = 0
    num.toString()
        .split("")
        .forEach((e) => (parseInt(e) === NaN ? false : (sum += parseInt(e))))
    return sum > 10 ? sumToOneDigit(sum) : sum
}

console.log(sumToOneDigit(num1))
console.log(sumToOneDigit(num2))
console.log(sumToOneDigit(num3))

// ******************************************************

// http://algorithms.dojo.news/static/Algorithms/index.html#LinkTarget_2129
/*
  String Anagrams
  Given a string,
  return array where each element is a string representing a different anagram (a different sequence of the letters in that string).
  Ok to use built in methods
*/

const str1 = "lim"
const expected1 = ["ilm", "iml", "lim", "lmi", "mil", "mli"]
    // Order of the output array does not matter

/**
 * Add params if needed for recursion.
 * Generates all anagrams of the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {Array<string>} All anagrams of the given str.
 * 1. create a empty array that holds the comb of the chars
 * 2. keep swapon the char til duplicate
 * 3. return the array once detect duplicate
 */
function generateAnagrams(str) {
    // if (arr.includes(str)) {
    //     return arr
    // } else {
    //     arr.push(str)
    //     return generateAnagrams(str.substr(1) + str[0], arr)
    // }
    for (var i = 0; i < arr.length; i++) {
        for (var j = 0; j < arr[i].length; j++) {
            for (var k = 0; k < arr[i].length; k++) {}
        }
    }
}

console.log(generateAnagrams(str1))