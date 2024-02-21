class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        //// Compare only left with right ////
        // Find the largest common prefix between the two ints in bin
        char[] larr = (String.format("%32s", Integer.toBinaryString(left)).replace(' ', '0')).toCharArray();
        char[] rarr = (String.format("%32s", Integer.toBinaryString(right)).replace(' ', '0')).toCharArray();
        StringBuilder sb = new StringBuilder();
        int i = 0;
        for (; i < 32; i++) {
            if (larr[i] != rarr[i]){
                break;
            }
            sb.append(larr[i]);
        }
        // Append the necessary amount of zeroes
        for (int j = 0; j < 32 - i; j++) {
            sb.append(0);
        }
        // Return that value as an int
        return Integer.parseInt(sb.toString(), 2);
    }
}