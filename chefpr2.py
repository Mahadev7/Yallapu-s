import math
for _ in range(int(input())):
    n = int(input())
    x = math.isqrt(n)
    if n % 2 == 1:
        x += 1
    print(x // 2)
