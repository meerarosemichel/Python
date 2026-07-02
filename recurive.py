# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# print("Factorial of 6 is",fact(6))
# print("Factorial of 6 is",factorial(6))

#fibonacci
#with memorization
# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)
# print("The fibonacci series is",fib(10) )


#reverse string
s = "hello"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)




class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2

        return ans