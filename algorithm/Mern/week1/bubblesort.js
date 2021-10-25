/** @format */

const numsOrdered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const numsRandomOrder = [9, 2, 5, 6, 4, 3, 7, 10, 1, 8]
const numsReversed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
const expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

/**
 * Sorts the given nums in-place by mutating the array.
 * Best: O(n) linear when array is already sorted.
 * Average: O(n^2) quadratic.
 * Worst: O(n^2) quadratic when the array is reverse sorted.
 * @param {Array<number>} nums
 * @returns {Array<number>} The given nums after being sorted.
 */
function bubbleSort(nums) {
    for (var i = 0; i < nums.length - 1; i++) {
        for (var j = 0; j < nums.length - 1 - i; j++) {
            if (nums[j] > nums[j + 1]) {;
                [nums[j], nums[j + 1]] = [nums[j + 1], nums[j]] //swap the two elements if the first one is greater
            }
        }
    }
    return nums
}
// CHALLENEGE: AN EARLY EXIT IF YOUR ARRAY IS ALREADY SORTED