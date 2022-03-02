input_num = (input ('Enter a gallon amount you would like to covert: '))

num = eval (input_num)

print ("")

print (num, "gallons is ", (num * 3.78541)/1000, "kiloliters")
print (num, "gallons is ", num * 3.78541, "liters")
print (num, "gallons is ", num * 3.78541 * 1000, "milliliters")

print ("")

print (num, "gallons is ", (num * .133681)/147197952000, "cubic miles")
print (num, "gallons is ", num * .133681, "cubic feet")
print (num, "gallons is ", num * 231, "cubic inches")

print ("")

print (num, "gallons is ", num * .00378541, "cubic meters")
print (num, "gallons is ", num * .00378541 * 100, "cubic centimeters")

print ("")

print (num, "gallons is ", num * 4, "quarts")
print (num, "gallons is ", num * 8, "quarts")
print (num, "gallons is ", num * 15.7725, "cups")
print (num, "gallons is ", num * 128, "ounces")
print (num, "gallons is ", num * 256, "tablespoons")
print (num, "gallons is ", num * 768, "teaspoons")
