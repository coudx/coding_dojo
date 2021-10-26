/** @format */

const numsOrdered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const numsRandomOrder = [9, 2, 5, 6, 4, 3, 7, 10, 1, 8]
const numsReversed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
const expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

/**
 * Sorts given array in-place.
 * Best: O(n^2) quadratic.
 * Average: O(n^2) quadratic.
 * Worst: O(n^2) quadratic.
 * @param {Array<number>} nums
 * @returns {Array<number>} The given array after being sorted.
 */
function selectionSort(nums) {
    for (var i = 0; i < nums.length - 1; i++) {
        for (var j = i + 1; j < nums.length; j++) {
            if (nums[i] > nums[j]) {
                let tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
            }
        }
    }
    return nums
}