n = int(input())
if n > 1:
    for i in range(2,n+1):
        if n % 2 == 0:
            print("not prime")
            break
        else:
            print("prime")
else:
    print("not prime")