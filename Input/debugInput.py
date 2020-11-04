'''
Created on Nov 3, 2020

@author: ITAUser
'''
'''The goal of this function is to calculate the 
area of a circle.

The function gets a radius from the user and 
then calculates the area.

The function should print and
return the area.
'''
def circleArea():
    question="What is the radius of your circle?"
    radius = input(question)

    pi = 3.14
    squared = input(radius*2)
    area = input(pi * squared) 
    print("The area is: " + area)
    return area

#Leave the next line alone
circleArea()


'''
This function calculates the area of a rectangle.

The function gets a height and width from the user and then calculates
the area.

The function prints and returns the area.
'''
def rectangleArea():
    height= input("What is the height of your rectangle?")
    width = input()
    
    area = height * width
    print(area)
    return area

#Leave the next line alone
rectangleArea()