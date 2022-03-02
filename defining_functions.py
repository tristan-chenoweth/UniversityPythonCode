def add_two(a,b):
    return a + b


print(add_two(2,3))


def gallon_to_liter(gallon):
    return gallon * 3.78541

print(gallon_to_liter(2))

def cm_to_feet_in(cm):
    inch = cm / 2.54
    feet = inch//12
    inch = inch%12
    return feet,inch


def feet_inch_to_cm(feet,inch):
    cm_foot = (feet * 12) * 2.54
    cm_inch = inch * 2.54
    return cm_foot + cm_inch

print(feet_inch_to_cm(5,9))


def tip(subtotal,percentage):
    tip = subtotal * (percentage / 100)
    grand_total = subtotal + tip
    return grand_total

print(tip(15.65,15))
