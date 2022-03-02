input_nums = input ("Enter three points for your triangle(Ex. 1,1 2,2 3,3): ")

nums = input_nums.split(" ")

#point inputs

pt_1 = nums[0].split(",")

pt_1_x = eval (pt_1[0])
pt_1_y = eval (pt_1[1])

print ("X1 = ", pt_1_x)
print ("Y1 = ", pt_1_y)


pt_2 = nums[1].split(",")

pt_2_x = eval (pt_2[0])
pt_2_y = eval (pt_2[1])

print ("X2 = ", pt_2_x)
print ("Y2 = ", pt_2_y)

pt_3 = nums[2].split(",")

pt_3_x = eval (pt_3[0])
pt_3_y = eval (pt_3[1])

print ("X2 = ", pt_3_x)
print ("Y2 = ", pt_3_y)


#distance calculations

