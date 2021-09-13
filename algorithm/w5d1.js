/**
 * /*
 *   Given a string that may have extra spaces at the start and the end,
 *   return a new string that has the extra spaces at the start and the end trimmed (removed)
 *   do not remove any other spaces.
 *
 * @format
 */

const str1 = "   hello world     "
const expected1 = "hello world"

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 * 1. check where the white space stops and use substring to peel out the word part
 */
function trim(str) {
    var i = 0
    var j = str.length - 1
    while (str[i] == " " && str[j] == " ") {
        if (str[i] == " ") {
            i++
        }
        if (str[j] == " ") {
            j--
        }
    }
    return str.substring(i, j)
}
console.log(trim(str1))

function mytrim(str) {
    return str.replace(/^\s+|\s+$/gm, "")
}

console.log(mytrim(str1))
    /*
     * Balance Index
     * Here, a balance point is ON an index, not between indices.
     * Return the balance index where sums are equal on either side
     * (exclude its own value).
     * Return -1 if none exist.
     */

const nums1 = [-2, 5, 7, 0, 3]
const expected1 = 2

const nums2 = [9, 9]
const expected2 = -1

const nums3 = [8, -2, 10, 1, 1, 1, 1, 1, 1]
const expected3 = 2
    /**
     * Finds the balance index in the given array where the sum to the left of the
     *    index is equal to the sum to the right of the index.
     * - Time: O(?).
     * - Space: O(?).
     * @param {Array<number>} nums
     * @returns {number} The balance index or -1 if there is none.
     * 1. check for everything on the left of the index and everything on the right of the index
     * 2. return the index when left and right are the same
     * 3. after the loop, return -1
     */
function balanceIndex(nums) {
    for (var i = 1; i < nums.length; i++) {
        var tmp = 0
        for (var j = 0; j < i; j++) {
            tmp += nums[j]
        }
        for (var k = j + 1; k < nums.length; k++) {
            tmp -= nums[k]
        }
        if (!tmp) {
            return i
        }
    }
    return -1
}

console.log(balanceIndex(nums1))