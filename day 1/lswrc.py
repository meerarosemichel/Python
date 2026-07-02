class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
            
        return max_len
solution = Solution()
test_string = "abcabcbb"
result = solution.lengthOfLongestSubstring(test_string)

print("The length of the longest substring is:", result)  
