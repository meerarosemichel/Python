from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Formula for the sum of numbers from 0 to n: n * (n + 1) / 2
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum

# --- LOCAL RUNNER FOR VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    case_1 = [3, 0, 1]
    print(f"Input: {case_1} -> Output: {sol.missingNumber(case_1)} (Expected: 2)")
    
    # Test Case 2
    case_2 = [0, 1]
    print(f"Input: {case_2} -> Output: {sol.missingNumber(case_2)} (Expected: 2)")
    
    # Test Case 3
    case_3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"Input: {case_3} -> Output: {sol.missingNumber(case_3)} (Expected: 8)")
