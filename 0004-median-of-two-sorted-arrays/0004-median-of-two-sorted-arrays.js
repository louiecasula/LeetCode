/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    // Append arrays and sort
    nums1 = (nums1.concat(nums2)).sort(function(a,b){return a - b});
    // If length is odd, return middle element
    if (nums1.length % 2 === 1) {
        return nums1[Math.floor(nums1.length / 2)];
    }
    // Else, return mean of two middle elements
    return (nums1[nums1.length / 2] + nums1[(nums1.length / 2) - 1]) / 2;
};