import math
import random

def addTwo(a,b):
    return a+b

# write a function to convert a gallon to a liter.
def gallon2liter(gallon):
    # convert gallon to liter and return
    liter = 3.78*gallon
    return liter

def feetInch2cm(feet,inch):
    # 1 foot = 12 inches
    # 1 inch = 2.54cm
    inches = 12*feet + inch
    cm = 2.54 * inches
    return cm
    # return 2.54*(12*feet + inch)
    
def cm2feetInch(cm):
    inch = cm / 2.54
    feet = inch//12
    inch = inch%12
    return feet, inch
    
def calTips(subtotal,rate):
    # return tips. rate is assumed to be percentage.
    tip = subtotal*(rate/100)
    total = tip + subtotal
    return tip, total
    
def sayGoodMorning(hello,repeat):

    morning = "Good Morning"
    if hello == "hello":
        morning = "Good Morning"
    elif hello == "bonjour":
        morning = "Bonjour"
    elif hello == "halo":
        morning = "Buenos dias"
        
    for i in range(repeat):
        print(morning)

def areaCircle(side):
    return 3.14159*side*side
#------------------------------------------------
# Implement the following functions.
# Read the description in each function.
#------------------------------------------------

def areaSquare(side):
    # return the area of an equilateral triangle given the side

def areaEqTriangle(side):
    # return the area of an equilateral triangle given the side

def mile2km(mile):
    # convert mile to km and returns it
    # 1 mile is 1.61 km

def lb2kg(mile):
    # convert pound(lb) to kg and returns it
    # 1 pound is 0.45 kg

def year2minute(year):
    # convert years to minutes
    # 1 year is 365 days
    # 1 day is 24 hours
    # 1 hour is 60 minutes
    
def abs(n):
    # return absolute value of n
    # if n is positive, returns n
    # else returns -n

def diff(m, n):
    # return the difference between two numbers m and n
    # if m is larger, then returns m - n, else n - m
    # or you can use abs() function above

def larger(a,b):
    # return the larger value between the two values a,b
    # don't use the built-in function max()
    
def largestAmongThree(a,b,c):
    # return the largest value among three values a,b,c
    # use the function larger() above

def distance(x1,y1,x2,y2):
    # returns the distance between two points (x1,y1) and (x2,y2)
    # Use math.sqrt(). 

def optimalCoinChange(price,payment):
    # return the number of quarters, dimes, nickles, cents for the change
    # For example, when price = 3.36 dollars, payment = 4 dollars
    #              the change is 0.64 dollar and 2 quarter, 1 dime, 4 cents
    #              are the right answer. So it returns (2,1,0,4)
    # Use // and % operator for quotient and remainder.

def coinFlip():
    # return a string "Head" or "Tail" randomly.
    # use random.randint(a,b)

def randomDirection():
    # return one of the strings "East","West","North","South" randomly.
    # use random.randint(a,b)

def isEven(n):
    # return true if n is an even number, false if not
    
def isDivisibleByFive(n):
    # return true if n is divisible by 5 (if 5 can divide n)
    # return false if not

def isPrime(n):
    # return true if n is a prime number
    # return false if not.
    # Hint. Use for loop "for i in range(n):" to divide n with i
    #       If any i can divide n, n is not a prime
    #       If no i can divide n, n is a prime number

def printPrimeNumbers(maxN):
    # print all prime numbers that are no larger than maxN
    # use the function 'isPrime(n)' above in a for loop


#-------------------------------------------------------------
# Add your code to test the functions you implemented above.
#-------------------------------------------------------------

#print(addTwo(-10,3))
#print(gallon2liter(2))
#print(calTips(5,1000))
#print(feetInch2cm(6,2))
#print(cm2feetInch(187.96))
#sayGoodMorning("bonjour",3)

