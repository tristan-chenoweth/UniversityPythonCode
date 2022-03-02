import math


class bmi:
    def __init__(self , name , age , weight , height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def get_bmi(self):
        return (self.__weight/(self.__height ** 2))

    def get_status(self):
        bmi = self.get_bmi()

        if (bmi >= 40):
            bmi_info = 'Extreme Obesity'

        elif (bmi <= 39.99) and (bmi >= 30):
            bmi_info = 'Obese'

        elif (bmi <= 29.99) and (bmi >= 25):
            bmi_info = 'Overweight'

        elif (bmi <= 24.99) and (bmi >= 18.50):
            bmi_info = 'Normal'

        else:
            bmi_info = 'Underweight'

        return bmi_info
