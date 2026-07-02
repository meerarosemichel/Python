class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}
        for char in magazine:
            if char not in chars: 
                chars[char] = 1
            else: 
                chars[char] += 1

        for char in ransomNote:
            if char in chars and chars[char] > 0: 
                chars[char] -= 1
            else: 
                return False
        
        return True
if __name__ == "__main__":
    sol = Solution()
    print("Test 1 Result:", sol.canConstruct("a", "b"))
    print("Test 2 Result:", sol.canConstruct("aa", "ab"))
    print("Test 3 Result:", sol.canConstruct("aa", "aab"))
