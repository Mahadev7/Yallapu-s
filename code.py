for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    c = input()
    c1 = 0
    for i  in range(n):
        if a[i] == c[i] or b[i] == c[i]:
            c1 += 1
    if c1 == n:
        print('NO')
    else:
        print('YES')
