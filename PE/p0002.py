def solve(coins, amount):
    N = len(coins)
    V = amount
    dp = [0] * (V + 1)
    dp[0] = 1
    for v in coins:
        for j in range(v, V + 1):
            dp[j] = dp[j] + dp[j - v]
    return dp[-1]
if __name__ == '__main__':
    c = [1,2,5,10,20, 50,100,200]
    t = 200
    print(solve(c,t))