"""
Multiples of 3 and 5

Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
def solve(n):
    ans = 0
    for v in range(1, n+1):
        if v % 3 == 0:
            ans += v
        elif v % 5 == 0:
            ans += v
    return ans
if __name__ == '__main__':
    print(solve(1000-1))
