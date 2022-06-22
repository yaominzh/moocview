"""
source LYD_Blue_Book
P10
对于k属于[0,35],有2^k mod 37互不相等,且恰好取遍整数1~36
"""
res = []
for i in range(36):

    res.append(2**i % 37)
print(res)
# [1, 2, 4, 8, 16, 32, 27, 17, 34, 31, 25, 13, 26, 15, 30, 23, 9, 18, 36, 35, 33, 29, 21, 5, 10, 20, 3, 6, 12, 24, 11, 22, 7, 14, 28, 19]

res.sort()
print(res)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
"""

"""

if __name__ == '__main__':
    pass