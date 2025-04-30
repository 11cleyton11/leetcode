class Solution(object):
    def climbStairs(self, n):

        fib1 = 0
        fib2 = 1

        for i in range(n):
            t = fib2
            fib2 += fib1
            fib1 = t
        return fib2