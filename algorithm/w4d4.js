/** @format */

const str1 = "Y(3(p)p(3)r)s"
const expected1 = true

const str2 = "N(0(p)3"
const expected2 = false
    // Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k"
const expected3 = false
    // Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c"
const expected4 = false

const str5 = "a(b)(c"
const expected5 = false

const str6 = "ab)(c"
const expected6 = false

const str7 = "abc"
const expected7 = true
    // Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {}

// ***********************************************************************************************
// ***********************************************************************************************
// ***********************************************************************************************

/*
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid.
*/

const str11 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!"
const expected1 = true

const str12 = "D(i{a}l[ t]o)n{e"
const expected2 = false

const str13 = "A(1)s[O (n]0{t) 0}k"
const expected13 = false

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    var lib = {}
    for (var i = 0; i < str.length; i++) {
        // console.log(str[i], i)
        switch (str[i]) {
            case "(":
            case "[":
            case "{":
                if (lib[str[i]] == undefined) {
                    lib[str[i]] = 1
                } else {
                    lib[str[i]]++
                }
                break
            case "}":
                // console.log(lib)
                // console.log("check { ", lib[str["{"]])
                if (lib["{"]) {
                    lib["{"]--
                        break
                } else {
                    return false
                }
            case ")":
                // console.log(lib)
                // console.log("check ( ", lib[str["("]])
                if (lib["("]) {
                    lib["("]--
                        break
                } else {
                    return false
                }
            case "]":
                // console.log(lib)
                // console.log(lib[("check [ ", str["["])])
                if (lib["["]) {
                    lib["["]--
                        break
                } else {
                    return false
                }
        }
    }
    for (key in lib) {
        if (lib[key]) return false
    }
    return true
}
const str11 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!"
const expected1 = true

console.log(bracesValid(str11))