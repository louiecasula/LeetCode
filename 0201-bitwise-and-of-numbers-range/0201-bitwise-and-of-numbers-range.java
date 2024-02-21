class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        //// Compare only left with right ////
        // Find the largest common prefix between the two ints in bin
        String lbinStr = Integer.toBinaryString(left);
        String lbin = String.format("%32s", lbinStr).replace(' ', '0');
        String rbinStr = Integer.toBinaryString(right);
        String rbin = String.format("%32s", rbinStr).replace(' ', '0');
        StringBuilder sb = new StringBuilder();
        int i = 0;
        char[] larr = lbin.toCharArray();
        char[] rarr = rbin.toCharArray();
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