class Solution {
    public int singleNumber(int[] nums) {
        // Map number with it's frequency
        Map<Integer,Integer> map = new HashMap<>();
        for (int num: nums) {
            if (!map.containsKey(num)) {
                map.put(num, 1);
            } else {
                map.put(num, map.get(num) + 1);
            }
        }
        // Iterate map
        for (int key: map.keySet()) {
            // Return key where val == 1
            if (map.get(key).equals(1)) {
                return key;
            }
        }
        return -1;
    }
}