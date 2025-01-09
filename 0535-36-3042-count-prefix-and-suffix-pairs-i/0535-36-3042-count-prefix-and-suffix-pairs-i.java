class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        // Keep an output variable
        int out = 0;
        int wlen = words.length;
        // Iterate to penultimate word
        for (int i = 0; i < wlen - 1; i++) {
            // Iterate from next to final word
            String affix = words[i];
            for (int j = i + 1; j < wlen; j++) {
                // If words[i] is a prefix and suffix of words[j], increment output
                if (words[j].startsWith(affix) && words[j].endsWith(affix)) { out++; }
            }
        }
        // Return output
        return out;
    }
}