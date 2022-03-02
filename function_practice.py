import math
import random



def area_circle(radius):
    return 3.14159 * radius * radius


def area_square(side_S):
    area_S = side_S ** 2
    return area_S


def area_equilateral_triangle(side_T):
    area_T = (math.sqrt(3)/4) * (side_T ** 2)
    return area_T


def mile_to_kilometer(mile):
    kilometer = mile * 1.60934
    return kilometer


def pound_to_kilogram(pound):
    kilogram = pound/2.20462262
    return kilogram


def year_to_minute(year):
    days = year * 365
    hours = days * 24
    minutes = hours * 60
    return minutes

    
def abs(n):
    if (n > 0):
        return n
    else:
        return -n


def difference(m , n):
    if (m > n):
        larger = m
        smaller = n
    else:
        larger = n
        smaller = m

    difference = larger - smaller

    return difference


def larger(a_L , b_L):
    if (a_L > b_L):
        larger = a_L
    elif (a_L = b_L)
        larger = 'They are Equal'
    else:
        larger = b_L

    return larger
    
def largest_out_of_three(a_3 , b_3 , c_3):
    if 

def distance(x1,y1,x2,y2):
    # returns the distance between two points (x1,y1) and (x2,y2)
    # Use math.sqrt(). 

def optimal_coin_change(price,payment):
    # return the number of quarters, dimes, nickles, cents for the change
    # For example, when price = 3.36 dollars, payment = 4 dollars
    #              the change is 0.64 dollar and 2 quarter, 1 dime, 4 cents
    #              are the right answer. So it returns (2,1,0,4)
    # Use // and % operator for quotient and remainder.

def coin_flip():
    # return a string "Head" or "Tail" randomly.
    # use random.randint(a,b)

def random_direction():
    # return one of the strings "East","West","North","South" randomly.
    # use random.randint(a,b)

def isEven(number_E):
    # return true if n is an even number, false if not
    
def is_divisible_by_five(number_5):
    # return true if n is divisible by 5 (if 5 can divide n) 
    # return false if not

def is_prime(n):
    for i in range(2,n):
        if (n % i == 0):
            return False:
    return True


def printPrimeNumbers(max_number):
    for i in range(2, max_number):
        
    # print all prime numbers that are no larger than maxN
    # use the function 'isPrime(n)' above in a for loop
