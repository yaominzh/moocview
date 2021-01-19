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
