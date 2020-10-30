'''
Created on Oct 30, 2020

@author: ITAUser
'''
from cmath import pi
'''
The goal of this function is to calculate the volume of
an object, when the user inputs height, width, and depth.

The function should print the sentence plus the volume and
return the volume.
'''
def volumeCalculator(height, width, depth):
    area = height * width
    volume = depth * area
    sentence = "The volume of this object is: "
    print(sentence + "volume")
    return volume

#Leave the next line alone
volumeCalculator(5, 5, 5)

'''
The goal of this function is to calculate the 
total of an order after tax and shipping.

The function should print and
return the total
'''
def shippingAndTax(subTotal):
    shipping = 10
    tax = .10
    
    taxTotal = subTotal * tax
    total = subTotal + taxTotal + shipping
    print("The total is: total")
    return total

#Leave the next line alone
shippingAndTax(15)

'''
The goal of this function is to calculate the 
total of an order after tax and shipping.

The function should print and
return the total
'''
def circleArea(radius):
    pi= 3.14
    
    squared = radius * radius
    area = "pi * squared" 
    print("The area is: area")
    return area

#Leave the next line alone
circleArea(5)