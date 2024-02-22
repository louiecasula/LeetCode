class Solution {
    public int findJudge(int n, int[][] trust) {
        // Edgecases
        if (n == 1) { return 1; }
        if (trust.length == 0) { return -1; }
        // Iterate through trust
        TreeSet<Integer> uniq = new TreeSet();
        HashMap<Integer, Integer> map = new HashMap();
        for (int[] pair: trust) {
            // Add each first value to a set
            uniq.add(pair[0]);
            int count = map.containsKey(pair[1]) ? map.get(pair[1]) : 0;
            map.put(pair[1], count + 1);
        }
        // If set's size equals n, return -1
        if (uniq.size() != n - 1) { return -1; }
        // Iterate from 1 to n
        for (int i = 1; i <= n; i++) {
            // If i isn't in set, return i
            if (!uniq.contains(i) && map.get(i) == n -1) {
                return i;
            }
        }
        return -1;
    }
}