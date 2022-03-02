import math

def max(num_1, num_2):
    if num_1 > num_2:
        result = num_1
    else:
        result = num_2
    return result

def sum_2(a,b):
    return a + b

def abs(n):
    if n > 0:
        return n
    else:
        return -n

def power(a,b):
    res = 1
    for i in range(b):
        res = res * a 
    return res
        
def main():
    i = -5
    j = 2
    k = max(i, j)
    print('The larger number of', i , 'and' , j , 'is' , k)
    print(sum_2(10,5))
    print(abs(5.1), abs(-5.1))
    print(power(3,2), power(2,3))
    
main()
