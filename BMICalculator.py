
'''
Requirements:
Metric and imperial
Input method: Options and interact
BMI calculation
Show results : current and history
History diagram
'''

'''
pseudo code:
Input and option function
Metric and imperial function
BMI calculation function
Diagram module
'''
import argparse

parser=argparse.ArgumentParser()
parser.parse_args()




def metric_imperial():
    system = input('Type i for Imperial system, type any other key for Metric System: ')
    return system

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

def cal(weight, height):
    if system !='i':
       BMI = round((weight / height ** 2) * 10000, 2)
    else:
       BMI = round((weight/height**2*703),2)
    return BMI

def range():
    if BMI <= 18.5:
       print(f'BMI={BMI},Underweight')
    elif BMI >= 30:
       print(f'BMI={BMI},Obesity')
    elif BMI >= 25 and BMI <= 29.9:
        print(f'BMI={BMI},Overweight')
    else:
       print(f'BMI={BMI},Normal weight')

'''
system = metric_imperial()
weight, height = get_data()
BMI = cal(weight,height)
range()
'''














