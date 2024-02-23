class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        // Copy and sort candies and save final indexed element as max val
        Boolean[] output = new Boolean[candies.length];
        Arrays.fill(output, false);
        int[] sorted = Arrays.copyOf(candies, candies.length);
        Arrays.sort(sorted);
        int max = sorted[sorted.length - 1];
        // Iterate candies, 
        for (int i = 0; i < candies.length; i++) {
            // if current element + extra is greater than or equal to max val, 
            if (candies[i] + extraCandies >= max) {
                // add true to output array
                output[i] = true;
            }
        }
        // Return output array
        return Arrays.asList(output);
    }
}