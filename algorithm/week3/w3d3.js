/**
 * /*
 *   Given an arr and a separator string, output a string of every item in the array separated by the separator.
 *
 *   No trailing separator at the end
 *   Default the separator to a comma with a space after it if no separator is provided
 *
 *
 *   1. create a function that takes in a list and a sperator
 *   2. loop through list ....
 *   3.
 *   4.
 *
 * @format
 */

const arr1 = [1, 2, 3]
const separator1 = ", "
const Aexpected1 = "1, 2, 3"

const arr2 = [1, 2, 3]
const separator2 = "-"
const Aexpected2 = "1-2-3"

const arr3 = [1, 2, 3]
const separator3 = " - "
const Aexpected3 = "1 - 2 - 3"

const arr4 = [1]
const separator4 = ", "
const Aexpected4 = "1"

const arr5 = []
const separator5 = ", "
const Aexpected5 = ""

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */
function join(arr, separator) {
    if (arr.length == 0) {
        return ""
    } else if (arr.length == 1) {
        return arr[0]
    }
    joined = arr[0]
    for (var i = 1; i < arr.length; i++) {
        joined += separator + arr[i]
    }
    return joined
}

console.log(join(arr3, separator3))

/*
Book Index
Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums span a consecutive range
*/

const nums1 = [1, 13, 14, 15, 37, 38, 70]
const Bexpected1 = "1, 13-15, 37-38, 70"

const nums2 = [75]
const Bexpected2 = "75"

const nums3 = []
const Bexpected3 = ""

const nums4 = [75, 76, "nooo", 80, 81]
const Bexpected4 = false

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @returns {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 *
 *
 * 1. check case when empty array
 * 2. check case when there is only one element in array and check for if it is a number
 * 3. run iteration
 * 4. run iteration while its consective page
 * 5. make i skip the consective pages
 * 6. check for number and turn false for every element and return false if its not a number
 * 7. boom finished
 *
 */
function bookIndex(nums) {
    if (nums.length == 0) {
        return ""
    } else if (nums.length == 1) {
        if (!Number.isInteger(nums[i])) {
            return false
        }
        return nums[0]
    }
    var exp = nums[0]
    for (var i = 1; i < nums.length; i++) {
        if (!Number.isInteger(nums[i])) {
            return false
        }
        exp += ", " + nums[i]
        if (nums[i + 1] == nums[i] + 1) {
            exp += "-"
            for (var j = i + 1; j < nums.length; j++) {
                if (!Number.isInteger(nums[i])) {
                    return false
                }
                if (nums[j + 1] != nums[j] + 1) {
                    i = j
                    break
                }
            }
            exp += nums[i]
        }
    }
    return exp
}

console.log(bookIndex(nums4))