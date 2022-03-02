def sum_upto(end_number):
    sum = 0
    for i in range (1,end_number):
        
        sum = sum + i
    return sum

print ("The sum of 1 through n is: " , sum_upto(10))
