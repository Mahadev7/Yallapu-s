for _ in range(int(input())):
    n = int(input())
    s = input()
    f = input()
    c = 0
    c1 = 0
    for i in range(len(s)):
        if s[i] == '1' and f[i] == '0':
            c += 1
        if s[i] == '0' and f[i] == '1':
            c1 += 1
    print(max(c,c1))
