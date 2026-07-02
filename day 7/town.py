from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score = [0] * (n + 1)
        for a, b in trust:
            score[a] -= 1
            score[b] += 1
            
        for i in range(1, n + 1):
            if score[i] == n - 1:
                return i
        return -1
if __name__ == "__main__":
    sol = Solution()
    n1 = 2
    trust1 = [[1, 2]]
    print("Test 1 Result:", sol.findJudge(n1, trust1))
    n2 = 3
    trust2 = [[1, 3], [2, 3]]
    print("Test 2 Result:", sol.findJudge(n2, trust2))
    n3 = 3
    trust3 = [[1, 3], [2, 3], [3, 1]]
    print("Test 3 Result:", sol.findJudge(n3, trust3))
