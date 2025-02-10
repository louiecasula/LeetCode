class Solution {
    public String clearDigits(String s) {
        // Keep a pointer for chars
        int cp = 0;
        // Keep an output StringBuilder
        StringBuilder out = new StringBuilder(s);
        // Iterate s,
        for (int i = 0; i < s.length(); i++) {
            // If curr is an int, set char at cp to "1" and decrement cp until it isn't an int
            if (Character.isDigit(out.charAt(i))) {
                out.setCharAt(cp, '1');
                while (cp > 0 && Character.isDigit(out.charAt(cp))) { cp--; }
            }
            // Else, set cp to i
            else { cp = i; }
        }
        String res = out.toString();
        // Replace all digits in output
        res = res.replaceAll("\\d", "");
        // Return output
        return res;
    }
}