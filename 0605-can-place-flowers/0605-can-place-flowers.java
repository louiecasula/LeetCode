class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int len = flowerbed.length;
        if (len == 1 && flowerbed[0] == 0) { return true; }
        if (len == 1 && flowerbed[0] == 1 && n == 1) { return false; }
        if (n == 0) { return true; }
        // Iterate through array
        for (int i = 0; i < len; i++) {
            try {
                if (flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0) {
                    flowerbed[i] = 1;
                    n--;
                }
            }
            catch (ArrayIndexOutOfBoundsException e) {
                if (i == 0 && flowerbed[0] == 0 & flowerbed[1] == 0) {
                    flowerbed[i] = 1;
                    n--;
                }
                if (i == len - 1 && flowerbed[i - 1] == 0 && flowerbed[i] == 0) {
                    flowerbed[i] = 1;
                    n--;
                }
            }
        }
        return n <= 0;
    }
}