/**
 * /*
 *   Array: Mode
 *
 *   Create a function that, given an array of ints,
 *   returns the int that occurs most frequently in the array.
 *   What if there are multiple items that occur the same number of time?
 *     - return all of them (in an array)
 *     - what if all items occur the same number of times?
 *       - return empty array
 *
 * @format
 */

const nums1 = []
const expected1 = []

const nums2 = [1]
const expected2 = [1]

const nums3 = [5, 1, 4]
const expected3 = []

const nums4 = [5, 1, 4, 1]
const expected4 = [1]

const nums5 = [5, 1, 4, 1, 5]
const expected5 = [5, 1]

const nums6 = [5, 1, 4, 1, 5, 4]
const expected6 = []
    //  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 * 1. create frequency table object
 * 2. Do edge case check
 * 3. return the result
 */
function mode(nums) {
    let freq = {}
    nums.forEach((e) => (freq[e] === undefined ? (freq[e] = 1) : freq[e]++))
    let mul = 1
    Object.values(freq).forEach((e) => (mul = e > mul ? e : mul))
    let arr = []
    for (key in freq) {
        if (freq[key] === mul) {
            arr.push(Number(key))
        }
    }
    return nums.length === 1 ?
        nums :
        mul === 1 || Object.keys(freq).length === arr.length ?
        [] :
        arr
}

console.log(mode(nums1))
console.log(mode(nums2))
console.log(mode(nums3))
console.log(mode(nums4))
console.log(mode(nums5))
console.log(mode(nums6))