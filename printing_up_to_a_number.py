n = eval (input("Enter a number to whuch you want to print: "))

i = 0

for i in range (i , n+1):
    if i % 10 == 0:
        print (i)
        print (end = "")
        i += 1    
    else:
        print (i, end = "     " )
        i += 1
