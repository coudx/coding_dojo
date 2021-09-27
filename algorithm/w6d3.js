/**
 * /*
 *   Recursively reverse a string
 *   helpful methods:
 *   str.slice(beginIndex[, endIndex])
 *   returns a new string from beginIndex to endIndex exclusive
 *
 * @format
 */

const str1 = "abc"
const expected1 = "cba"

const str2 = ""
const expected2 = ""

const str3 = 42
const expected3 = "The answer to the universe"

const str4 = 4
const expected4 = false

/**
 * Recursively reverses a string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given str reversed.
 */
// function reverseStr(str) {
//     return typeof str == "string" ?
//         str.length > 1 ?
//         reverseStr(str.substr(1)) + str.charAt(0) :
//         str :
//         str === 42 ?
//         "The answer to the universe" :
//         false
// }

function reverseStr(str, index = str.length) {
    return typeof str == "string" ?
        index ?
        str[index - 1] + reverseStr(str, index - 1) :
        "" :
        str === 42 ?
        "The answer to the universe" :
        false
}

console.log(reverseStr(str1))
console.log(reverseStr(str2))
console.log(reverseStr(str3))
console.log(reverseStr(str4))

// ***********************************************

/*
  Recursive Binary Search
  Input: SORTED array of ints, int value
  Output: bool representing if value is found
  Recursively search to find if the value exists, do not loop over every element.
  Approach:
  Take the middle item and compare it to the given value.
  Based on that comparison, narrow your search to a particular section of the array
*/

const nums1 = [1, 3, 5, 6]
const searchNum1 = 4
const expected1 = false

const nums2 = [4, 5, 6, 8, 12]
const searchNum2 = 5
const expected2 = true

const nums3 = [3, 4, 6, 8, 12]
const searchNum3 = 3
const expected3 = true

/**
 * Add params if needed for recursion
 * Recursively performs a binary search (divide and conquer) to determine if
 * the given sorted nums array contains the given number to search for.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the searchNum was found in the sortedNums array.
 */
// function binarySearch(sortedNums, searchNum) {
//     let midIndex = Math.floor(sortedNums.length / 2)
//     let mid = sortedNums[midIndex]
//     return sortedNums.length > 0 ?
//         mid === searchNum ?
//         true :
//         mid > searchNum ?
//         binarySearch(sortedNums.slice(0, midIndex), searchNum) :
//         binarySearch(sortedNums.slice(midIndex + 1), searchNum) :
//         false
//         // if (sortedNums.length > 0){
//         //     if (mid === searchNum) {
//         //         return true
//         //     } else if (mid > searchNum){
//         //         return binarySearch(sortedNums.slice(0, midIndex), searchNum)
//         //     } else {
//         //         return binarySearch(sortedNums.slice(midIndex + 1), searchNum)
//         //     }
//         // } else {
//         //     return false
//         // }
// }

function binarySearch(
    sortedNums,
    searchNum,
    begin = 0,
    end = sortedNums.length
) {
    let midIndex = Math.floor((end + begin) / 2)
    let mid = sortedNums[midIndex]
    return begin < end ?
        mid === searchNum ?
        true :
        mid > searchNum ?
        binarySearch(sortedNums, searchNum, 0, midIndex) :
        binarySearch(sortedNums, searchNum, midIndex + 1, end) :
        false
}

console.log(binarySearch(nums1, searchNum1))
console.log(binarySearch(nums2, searchNum2))
console.log(binarySearch(nums3, searchNum3))