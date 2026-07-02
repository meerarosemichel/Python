from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            # If count drops to 0, we select a new candidate
            if count == 0:
                candidate = num
            
            # Increment if it matches the candidate, decrement if it doesn't
            count += 1 if num == candidate else -1
            
        return candidate
if __name__ == "__main__":
    sol = Solution()
    case_1 = [3, 2, 3]
    print(f"Input: {case_1} -> Output: {sol.majorityElement(case_1)} (Expected: 3)")
    case_2 = [2, 2, 1, 1, 1, 2, 2]
    print(f"Input: {case_2} -> Output: {sol.majorityElement(case_2)} (Expected: 2)")
