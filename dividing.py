n = 10

for divisor in range(n):
    n % 2 == 0
    n % 3 == 0
    n % 4 == 0

    if (n % divisor == 0):
        print(n, 'is not a prime number.')
        break
    else:
        print(n, 'is not a prime number.')
        
