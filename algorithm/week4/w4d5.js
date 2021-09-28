/**
 * /*
 *   An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 *   typically using all the original letters exactly once.
 *   Is there a quick way to determine if they aren't an anagram before spending more time?
 *   Given two strings
 *   return whether or not they are anagrams
 *
 * @format
 */

const strA1 = "yes"
const strB1 = "eys"
const expected1 = true

const strA2 = "yes"
const strB2 = "eYs"
const expected2 = true

const strA3 = "no"
const strB3 = "noo"
const expected3 = false

const strA4 = "silent"
const strB4 = "listen"
const expected4 = true

const strA5 = "yes1y"
const strB5 = "e1yss"
const expected5 = true

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */
function isAnagram(s1, s2) {
    // check if two string are the same length if not return false
    if (s1.length !== s2.length) {
        return false
    }
    arr = {}
        // log the number of each character in the first string
    for (var i = 0; i < s1.length; i++) {
        if (arr[s1[i].toLowerCase()] === undefined) {
            arr[s1[i].toLowerCase()] = 1
        } else {
            arr[s1[i].toLowerCase()]++
        }
    }
    // check and remove the character from the logged first string, remove if existing
    // return flase if does not exist
    for (var i = 0; i < s2.length; i++) {
        if (
            arr[s2[i].toLowerCase()] === undefined ||
            !arr[s2[i].toLowerCase()]
        ) {
            return false
        } else {
            arr[s2[i].toLowerCase()]--
        }
    }
    // return true
    return true
}

console.log(isAnagram(strA5, strB5))

/*
  String: Rotate String
  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

const str = "Hello World"

const rotateAmnt1 = 0
const expected1 = "Hello World"

const rotateAmnt2 = 1
const expected2 = "dHello Worl"

const rotateAmnt3 = 2
const expected3 = "ldHello Wor"

const rotateAmnt4 = 4
const expected4 = "orldHello W"

const rotateAmnt5 = 13
const expected5 = "ldHello Wor"
    /*
                    Explanation: this is 2 more than the length so it ends up being the same
                    as rotating it 2 characters because after rotating every letter it gets back
                    to the original position.
                    */

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 *  1. check if amnt is greater the length of the string and
 *      - if it is greater then the length of the string, make it short then it is
 *  2. loop though the back part of the string that need to be in the front of the
 *  3. loop though the rest of the string that need to be in the back
 *  4. return the new string
 */
function rotateStr(str, amnt) {
    tmp = ""
    while (amnt > str.length) {
        amnt -= str.length
    }

    for (var i = str.length - amnt; i < str.length; i++) {
        tmp += str[i]
    }

    for (var i = 0; i < str.length - amnt; i++) {
        tmp += str[i]
    }
    return tmp
}

console.log(rotateStr(str, rotateAmnt5))