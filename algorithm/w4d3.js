/**
 * /*
 *   Given a string,
 *   return a new string with the duplicates excluded
 *   Bonus: Keep only the last instance of each character.
 *
 * @format
 */

const str1 = "abcABC"
const expected1 = "abcABC"

const str2 = "helloo"
const expected2 = "helo"

const str3 = "helololo"
const expected3 = "helo"

// Bonus
const str4 = "helololol"
const expected4 = "heol"

function countLetter(arr) {
    var freq = {}
    for (var i = 0; i < arr.length; i++) {
        if (freq[arr[i]] == undefined) {
            freq[arr[i]] = 1
        } else {
            freq[arr[i]]++
        }
    }
    return freq
}

function split(str, str2) {
    arr = []
    tmp = ""
    for (var i = 0; i < str.length; i++) {
        if (str[i] == str2) {
            arr.push(tmp)
            tmp = ""
        } else {
            tmp += str[i]
        }
    }
    arr.push(tmp)
    return arr
}

function join(arr, str) {
    var tmp = arr[0]
    for (var i = 1; i < arr.length; i++) {
        tmp += str + arr[i]
    }
    return tmp
}

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
    var arr = countLetter(str)
    for (key in arr) {
        if (arr[key] > 1) {
            str = join(split(str, key), "") + key
        }
    }
    return str
}

// ****************************************************************************************

console.log(stringDedupe(str3))

/*
      Given a string containing space separated words
      Reverse each word in the string.
      If you need to, use .split to start, then try to do it without.
    */

const str1 = "hello"
const expected1 = "olleh"

const str2 = "hello world"
const expected2 = "olleh dlrow"

const str3 = "abc def ghi"
const expected3 = "cba fed ihg"

function reverse(str) {
    tmp = ""
    for (var i = str.length - 1; i >= 0; i--) {
        tmp += str[i]
    }
    return tmp
}

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    arr = split(str, " ")
    for (var i = 0; i < arr.length; i++) {
        arr[i] = reverse(arr[i])
    }
    return join(arr, " ")
}

console.log(reverseWords(str3))