#daily temperature
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  
        
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
            
        return res
if __name__ == "__main__":
    test_temps = [73, 74, 75, 71, 69, 72, 76, 73]
    sol = Solution()
    output = sol.dailyTemperatures(test_temps)
    
    # Print the result
    print("Input Temperatures: ", test_temps)
    print("Days until warmer:  ", output)
