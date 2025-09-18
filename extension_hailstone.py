# extension_hailstone.py

from turtle import *
from random import randint

print("--- Hailstone Sequence ---")
print()
colormode(255)

# get the starting number from the user 
# create a variable to count the number of steps it takes to find the sequence
# loop until the number is equal to 1

num = int(input("Input a starting number: "))
steps = 0
speed(10)

while num != 1:
    color(randint(0,255), randint(0,255), randint(0,255))
    # forward(num)
    circle(num, 180)
    penup()
    goto(0,0)
    pendown()
    left(10)
    steps += 1
    if num%2 == 0: # if num is an even number
        num = num/2
    else:
        num = num*3+1
    print(int(num))

print(f"It took {steps} steps to complete the sequence")

