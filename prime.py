for n in range(2, 7):
    for x in range(2, n):
        print( n,'%',x ,' ==',n % x )
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')