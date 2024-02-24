class Solution {
    public int maxProfit(int[] prices) {
        // Keep a count
        int count = 0;
        // Iterate through prices
        for (int i = 0; i < prices.length - 1; i++) {
            // If next - curr is positive, add to count
            if (prices[i + 1] - prices[i] > 0) {
                count += prices[i + 1] - prices[i];
            }
        }
        // Return count
        return count;
    }
}