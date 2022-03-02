##n = eval(input('Enter a number to count up to in fibonacci: '))
##
##iteration = 0
##
##fib = 0
##a = 0
##
##for i in range(0 , n+1):
##    a = i
##     = a + i
##    print (iteration,' ',a)
##    i += 1
##    iteration += 1
##
##

startNumber = int(input("Enter the start number here "))
endNumber = int(input("Enter the end number here "))

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)

print (fib, range(startNumber, endNumber))
