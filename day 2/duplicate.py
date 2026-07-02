class Solution:
    def removeDuplicates(self, nums) -> int:
        # Edge case: if the array is empty, return 0
        if not nums:
            return 0
            
        slow, fast = 0, 1
        
        # FIX: Changed 'in range()' to a direct inequality check
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow + 1] = nums[fast]
                fast += 1
                slow += 1

        return slow + 1

solution = Solution()
test_nums = [1, 1, 2, 2, 3, 4, 4]

unique_length = solution.removeDuplicates(test_nums)

print("Length of unique elements:", unique_length)
print("Modified array (first elements):", test_nums[:unique_length])
