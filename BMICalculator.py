'''

#! /usr/bin/python3

# Measurement System Input
def metric_imperial():
    system = input('Type i for Imperial system, type any other key for Metric System: ')
    return system

# Data Input
def get_data():
   if system != 'i':
      weight = float(input("weight(kg): "))
      height = float(input("height(cm): "))
   else:
      weight = float(input("weight(LBS): "))
      feet = float(input("height(Feet): "))
      inches = float(input("height(inches): "))
      height = float(feet*12 + inches)
   return weight, height

# Calculation
def cal(weight, height):
    if system !='i':
       BMI = round((weight / height ** 2) * 10000, 2)
    else:
       BMI = round((weight/height**2*703),2)
    return BMI

# Weight Range
def range():
    if BMI <= 18.5:
       print(f'BMI={BMI},Underweight')
    elif BMI >= 30:
       print(f'BMI={BMI},Obesity')
    elif BMI >= 25 and BMI <= 29.9:
        print(f'BMI={BMI},Overweight')
    else:
       print(f'BMI={BMI},Normal weight')


system = metric_imperial()
weight, height = get_data()
BMI = cal(weight,height)
range()

'''

class BMI_Cal:
    def __init__(self):
        self. system = ''
        self.Weight = 0
        self.height = 0
        self.BMI = 0
        self.feet = 0
        self.inches = 0
    def cal_BMI(self):
        ## def metric_imperial(self):
        self.system = input('Type i for Imperial system, type any other key for Metric System: ')
        ## def get_data(self):
        if self.system != 'i':
            self.weight = float(input("weight(kg): "))
            self.height = float(input("height(cm): "))
        else:
            self.weight = float(input("weight(LBS): "))
            self.feet = float(input("height(Feet): "))
            self.inches = float(input("height(inches): "))
            self.height = float(self.feet * 12 + self.inches)
        ## def bmi_cal(self,weight,height):
        if self.system != 'i':
            self.BMI = round((self.weight / self.height ** 2) * 10000, 2)
        else:
            self.BMI = round((self.weight / self.height ** 2 * 703), 2)
        ## def weight_range(self,self.BMI):
        if self.BMI <= 18.5:
            print(f'BMI={self.BMI},Underweight')
        elif self.BMI >= 30:
            print(f'BMI={self.BMI},Obesity')
        elif self.BMI >= 25 and self.BMI <= 29.9:
            print(f'BMI={self.BMI},Overweight')
        else:
            print(f'BMI={self.BMI},Normal weight')


test = BMI_Cal()
system = test.cal_BMI()















