class Solution {
    public String firstPalindrome(String[] words) {
        for (String word: words) {
            StringBuilder sb = new StringBuilder(word);
            if (sb.toString().equals(sb.reverse().toString())) {
                return sb.toString();
            }
        }
        return "";
    }
}