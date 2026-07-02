class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        prev2, prev1 = 0, 1
        for _ in range(2, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
        return prev1

# --- Code to run and test inside VS Code ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: n = 2 (0 + 1) -> Expected Output: 1
    print("Fibonacci(2):", sol.fib(2))
    
    # Test Case 2: n = 4 (1 + 1 + 2) -> Expected Output: 3
    print("Fibonacci(4):", sol.fib(4))
    
    # Test Case 3: n = 10 -> Expected Output: 55
    print("Fibonacci(10):", sol.fib(10))
