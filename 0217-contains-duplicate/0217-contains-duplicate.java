class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Make a set from nums
        HashSet<Integer> set = new HashSet();
        for (int i: nums) {
            set.add(i);
        }
        // Return false if size of set equals size of list
        return nums.length != set.size();
    }
}