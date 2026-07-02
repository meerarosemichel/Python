class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count_s, count_t = {}, {}
        
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
            
        return count_s == count_t

# --- HOW TO RUN AND PRINT THE RESULT ---
solution = Solution()
s1 = "anagram"
t1 = "nagaram"

result = solution.isAnagram(s1, t1)
print("Is anagram:", result)  # Output: True
