print('1st---------\n')
print('Nida Mirza')
print('180630107030')
print('2nd---------\n')
a=1
b=10
print(a+b)
print('3rd---------\n')
import math  
  
# print the square root of  1  
print(math.sqrt(1))  
  
# print the square root of 45 
print(math.sqrt(45))  
  
# print the square root of 2.5 
print(math.sqrt(2.5))
print('4th---------\n')
# Three sides of the triangle is a, b and c:  
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)
print('5th---------\n')
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculate the discriminant  
d = (b**2) - (4*a*c)  
  
# find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))
print('6th---------\n')
# swapping of two variables 
  
x = 10
y = 50
  
temp = x 
x = y 
y = temp 
  
print("Value of x:", x) 
print("Value of y:", y)
print('7th---------\n')

# importing the random module
import random

print('Generated Random Number:',random.randint(0,50))
print('8th---------\n')


kilometers = float(input('How many kilometers?: '))  
# conversion factor  
conv_fac = 0.621371  
# calculate miles  
miles = kilometers * conv_fac  
print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))
print('9th---------\n')
celsius = float(input('Enter temperature in Celsius: '))  
  
# calculate temperature in Fahrenheit  
fahrenheit = (celsius * 1.8) + 32  
print('%0.1f  Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))  

