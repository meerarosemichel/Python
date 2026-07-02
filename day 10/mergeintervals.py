from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by their start times
        intervals = sorted(intervals, key=lambda x: x[0])

        ans = []

        for interval in intervals:
            # If ans is empty or current interval doesn't overlap with the last merged one
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            # If there is an overlap, merge them by updating the end time
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        
        return ans
if __name__ == "__main__":
    sol = Solution()
    case_1 = [[1,3],[2,6],[8,10],[15,18]]
    print(f"Input: {case_1}\nOutput: {sol.merge(case_1)}\nExpected: [[1, 6], [8, 10], [15, 18]]\n")
    case_2 = [[1,4],[2,3]]
    print(f"Input: {case_2}\nOutput: {sol.merge(case_2)}\nExpected: [[1, 4]]\n")
