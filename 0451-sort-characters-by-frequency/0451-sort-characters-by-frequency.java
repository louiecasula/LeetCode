class Solution {
    public String frequencySort(String s) {
        // Map the characters to their frequency
        Map<Character, Long> map = new HashMap<>();
        char[] arr = s.toCharArray();
        for (char c : arr) {
            if (!map.containsKey(c)) {
                map.put(c, 1L);
            } else {
                map.put(c, map.get(c) + 1L);
            }
        }
        // Save values to set
        Set<Long> list = new HashSet<>(map.values());
        // Convert set to list
        List<Long> freq = new ArrayList<>(list);
        // Sort the list in descending order
        Collections.sort(freq, Collections.reverseOrder());
        // StringBuilder
        StringBuilder sb = new StringBuilder();
        // Iterate through list
        for (Long f : freq) {
            // Iterate through keys
            for (Character key : map.keySet()) {
                // If the current key's value == the current list element,
                if (map.get(key).equals(f)) {
                    // Append the key by value number of times
                    for (long i = 0; i < f; i++) {
                        sb.append(key);
                        map.put(key, 0L);
                    }
                }
            }
        }
        // Return String
        return sb.toString();
    }
}