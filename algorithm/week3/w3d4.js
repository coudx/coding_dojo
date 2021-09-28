/**
 * /*
 *   Given in an alumni interview in 2021.
 *   String Encode
 *   You are given a string that may contain sequences of consecutive characters.
 *   Create a function to shorten a string by including the character,
 *   then the number of times it appears.
 *
 *   If final result is not shorter (such as "bb" => "b2" ),
 *   return the original string.
 *
 * @format
 */

const str1 = "aaaabbcddd"
const expected1 = "a4b2c1d3"

const str2 = ""
const expected2 = ""

const str3 = "a"
const expected3 = "a"

const str4 = "bbcc"
const expected4 = "b2c2"

const str5 = "aaaabbcdddaaa"
const expected5 = "a4b2c1d3a3"

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs only if the
 * character occurs more than two time.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */
function encodeStr(str) {
    let encoded = ""
    for (var i = 0; i < str.length; i++) {
        encoded += str[i]
        for (var counter = 1; counter < str.length; counter++) {
            if (str[i] !== str[counter + i]) {
                i += counter - 1
                encoded += counter
                break
            }
        }
    }
    return encoded
}

console.log(encodeStr(str5))

/*
 * String Decode
 */

const str1 = "a3b2c1d3"
const expected1 = "aaabbcddd"

const str2 = "a3b2c12d10"
const expected2 = "aaabbccccccccccccdddddddddd"

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */

function decodeStr(str) {
    let decode = ""
    for (var i = 0; i < str.length; i++) {
        let num = ""
        let ct = 1
        for (var j = i + 1; j < str.length; j++) {
            if (Number.isInteger(parseInt(str[j]))) {
                num += str[j]
                ct++
            } else {
                ct--
                break
            }
        }

        for (var j = 0; j < parseInt(num, 10); j++) {
            decode += str[i]
        }
        i += ct
    }
    return decode
}

console.log(decodeStr(str2))