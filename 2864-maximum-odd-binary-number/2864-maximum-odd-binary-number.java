class Solution {
    public String maximumOddBinaryNumber(String s) {
        // Remove one 1
        s = s.replaceFirst("1", "");
        // If there are any more 1s, sort in desc order and append a 1 back on
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder(new String(arr));
        sb.reverse();
        sb.append("1");
        return sb.toString();
    }
}