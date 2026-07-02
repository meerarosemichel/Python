import sys
sys.setrecursionlimit(2000)

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        
        def climb(n: int) -> int:
            if n in memo: 
                return memo[n]
            
            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]
        
        return climb(n)
if __name__ == "__main__":
    sol = Solution()
    print("Test n=2 Result:", sol.climbStairs(2))
    print("Test n=3 Result:", sol.climbStairs(3))
    print("Test n=5 Result:", sol.climbStairs(5))
