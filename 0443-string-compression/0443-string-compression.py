class Solution:
    def compress(self, chars: List[str]) -> int:
        # Keep two pointers, a counter, and current char variable
        j = i = 0
        counter = 0
        curr = ""
        # Iterate chars,
        while i < len(chars):
            # If current char == current index char, increment counter
            if curr == chars[i]:
                counter += 1
            # Else,
            else:
                # If counter > 1, set char[pointer] to counter, increment pointer
                if counter > 1:
                    counter = str(counter)
                    for k in range(len(counter)):
                        chars[j] = counter[k]
                        j += 1
                # Set char[pointer] to curr index char, increment pointer and counter
                chars[j] = chars[i]
                j += 1
                # Reset counter and update current char
                counter = 1
                curr = chars[i]
            i += 1
        # If there's a final counter above 1, add it to chars
        if counter > 1:
            counter = str(counter)
            for k in range(len(counter)):
                chars[j] = counter[k]
                j += 1
        while i > j:
            chars.pop()
            i -= 1
        # Return pointer
        return j + 1