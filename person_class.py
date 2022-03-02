import math

class person:
    def __init__ (self, height, weight, gender, age, power, consumption):
        self.height = height
        self.weight = weight
        self.gender = gender
        self.age = age
        self.power = power, consumption

    def is_good_health(self):
        if self.power > 10:
            return True
        else:
            return False

    def is_over_weight(self):
        bmi = (self.weight / self.height ** 2) * 703

        return bmi > 27.3
