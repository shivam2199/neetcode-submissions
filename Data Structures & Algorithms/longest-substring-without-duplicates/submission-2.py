class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_length = 1
        i,j=0,0
        chars = set()
        while (j < len(s)):
            if s[j] not in chars:
                chars.add(s[j])
                j+=1
            else:
                max_length = max(max_length, j-i)
                while s[j] in chars:
                    chars.remove(s[i])
                    i+=1

        return max(max_length, j-i)
