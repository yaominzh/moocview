"""
Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def check(num):
    aux = str(num)
    l = 0
    r = len(aux) - 1
    while l<r:
        if aux[l] != aux[r]:
            return False
        l += 1
        r -= 1
    return True

def solve():
    start = 999
    res = []
    while start > 100:
        for i in range(start-1, 99,-1):
            if check(start*i):
                res.append(start * i)
        start -=1
    return max(res)
if __name__ == '__main__':
    print(solve())
