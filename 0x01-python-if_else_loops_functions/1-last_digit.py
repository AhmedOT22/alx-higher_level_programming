#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number > 5 :
	message = "and is greater than 5"
elif number < 6 and number != 0 :
	message = "and is less than 6 and not 0"
elif number == 0 :
	message = "and is zero"
print(f"Last digit of {number} is {last_digit} {message}")
