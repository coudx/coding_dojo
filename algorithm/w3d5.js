/** @format */

// const str1 = "a x a"
// const expected1 = true

// const str2 = "racecar"
// const expected2 = true

// const str3 = "Dud"
// const expected3 = false

// const str4 = "oho!"
// const expected4 = false

/**
 * /*
 *   Longest Palindrome
 *   For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring.
 *   Strings longer or shorter than complete words are OK.
 *   All the substrings of "abc" are:
 *   a, ab, abc, b, bc, c
 *
 * @format
 */

const str1 = "what up, daddy-o?"
const expected1 = "dad"

const str2 = "uh, not much"
const expected2 = "u"

const str3 = "Yikes! my favorite racecar erupted!"
const expected3 = "e racecar e"

const str4 = "a1001x20002y5677765z"
const expected4 = "5677765"

const str5 = "a1001x20002y567765z"
const expected5 = "567765"

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
function isPalindrome(str) {
    for (var i = 0; i < str.length / 2; i++) {
        if (str[i] != str[str.length - i - 1]) {
            return false
        }
    }
    return true
}
/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */
function longestPalindromicSubstring(str) {
    let pal = ""
    for (var i = 0; i < str.length; i++) {
        let tmp = ""
        for (var j = i; j < str.length; j++) {
            tmp += str[j]
            if (isPalindrome(tmp) && tmp.length > pal.length) {
                pal = tmp
            }
        }
    }
    if (pal.length == 0) {
        pal = str[0]
    }
    return pal
}

console.log(longestPalindromicSubstring(str1))

console.log(longestPalindromicSubstring(str2))

console.log(longestPalindromicSubstring(str3))

console.log(longestPalindromicSubstring(str4))

console.log(longestPalindromicSubstring(str5))