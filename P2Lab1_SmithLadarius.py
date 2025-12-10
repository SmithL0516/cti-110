#Ladarius Smith
#11/14/25
#P2LAB1
#the program will calculate the diameter, circumference, and area of a circle

#import the math module to use the constant, math.pi
import math

#Get radius from user
radius = float(input("what is the radius of the circle? "))
print()

#calculate diameter
diameter = 2 * radius

#display diameter with 1 decimal point
print(f"The diameter of the cirlce is {diameter:.1f}\n")

#Calculate circumference 
circumference = 2 * math.pi * radius

#Display circumference with 2 decimal places
print(f"the circumference of the cirlce is {circumference:.2f}\n")

#Calculate the area
area = math.pi * radius**2

#Display area with 3 decimal places
print(f"The area of the cirlce is {area:.3f}")
