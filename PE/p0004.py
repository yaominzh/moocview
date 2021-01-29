"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
def solve(x):
    i = 2
    aux = []
    while i<= x//i:
        if(x%i==0):
            s = 0
            while x % i ==0:
                x //= i
                s += 1
            aux.append(i)
        i+=1
    # 可能大于sqrt(n) 的质因子只有一个
    if x>1:
        aux.append(x)
    return max(aux)
if __name__ == '__main__':
    print(solve(600851475143))
