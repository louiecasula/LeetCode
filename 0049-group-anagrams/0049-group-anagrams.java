class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Create output list
        List<List<String>> output = new ArrayList<>();
        // Create a map: key = sorted element, value = list of indexes
        Map<String, List<Integer>> dic = new HashMap<>();
        // Iterate through input
        for (int i = 0; i < strs.length; i++) {
            char[] arr = strs[i].toCharArray();
            Arrays.sort(arr);
            String sort = new String(arr);
            dic.putIfAbsent(sort, new ArrayList<>());
            dic.get(sort).add(i);
        }
        // Iterate through map values
        for (List<Integer> indexes: dic.values()) {
            List<String> ana = new ArrayList<>();
            // Iterate through list
            for (Integer index : indexes) {
            ana.add(strs[index]);
            }
            // Append list to output
            output.add(ana);
        }
        // Return output
        return output;
    }
}