input_num = (input ('Enter a inch amount you would like to covert: '))

num = eval (input_num)

print ("")

print (num, "inches is ", num/12, "feet")
print (num, "inches is ", (num/12)/3 , "yards")
print (num, "inches is ", (num/12)/5280, "miles")

print ("")

print (num, "inches is ", num**2, "inches squared")
print (num, "inches is ", (num/12)**2, "feet squared")
print (num, "inches is ", ((num/12)/3)**2, "yards squared")

print ("")

print (num, "inches is ", num * 25.4, "millimeters")
print (num, "inches is ", num * 2.54, "centimeters")
print (num, "inches is ", num * .0254, "meters")
print (num, "inches is ", num * .0000254, "kilometers")

print ("")

print (num, "inches is ", (num * 25.4)**2, "millimeters squared")
print (num, "inches is ", (num * 2.54)**2, "centimeters squared")
print (num, "inches is ", (num * .0254)**2, "meters squared")
print (num, "inches is ", (num * .0000254)**2, "kilometers squared")

