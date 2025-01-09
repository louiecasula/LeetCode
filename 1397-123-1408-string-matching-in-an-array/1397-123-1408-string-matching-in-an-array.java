class Solution {
    public List<String> stringMatching(String[] words) {
        // Keep an output String array
        ArrayList<String> out = new ArrayList<String>();
        int wlen = words.length;
        // Iterate to penultimate word
        for (int i = 0; i < wlen - 1; i++) {
            // Iterate from next to final word
            for (int j = i + 1; j < wlen; j++) {
                // If words[i] is in words[j] or vice versa, append that word to output if it hasn't already been added
                if (words[i].contains(words[j]) && !out.contains(words[j])) { out.add(words[j]); }
                if (words[j].contains(words[i]) && !out.contains(words[i])) { out.add(words[i]); }
            }
        }
        // Return output
        return out;
    }
}