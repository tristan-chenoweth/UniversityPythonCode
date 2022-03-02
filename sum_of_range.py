def sum_from_to(a,b):
    sum = 0
    for i in range(a,b + 1):
        sum = sum + i
        i += 1
    print('The sum from', a , 'to' , b , 'is' , sum)


sum_from_to(1,10)
sum_from_to(20,37)
sum_from_to(35,49)


    


##sum_1 = 0
##sum_2 = 0
##sum_3 = 0
##
##for i in range(1,11):
##    sum_1 = sum_1 + i
##    i += 1
##
##for i in range(20,38):
##    sum_2 = sum_2 + i
##    i += 1
##
##for i in range(35,50):
##    sum_3 = sum_3 + i
##    i += 1
##
##
##print('Sum of 1 to 10 is: ', sum_1)
##print('Sum of 20 to 37 is: ', sum_2)
##print('Sum of 35 to 49 is: ', sum_3)
