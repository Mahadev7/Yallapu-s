for _ in range(int(input())):
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    e,f = map(int,input().split())
    g,h = map(int,input().split())
    area = 0
    if a == e:
        area = abs((e-a)**2 + (f-b)**2)
    elif a == g:
        area = abs((g-a)**2 + (h-b)**2)
    elif a == c:
        area = abs((c-a)**2 + (d-b)**2)
    else:
        area = abs((g-e)**2 + (h-f)**2)
    print(area)
