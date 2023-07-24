#!/usr/bin/env python3
# Fifth example of pinging from Python
# Reading IPs from a file
# By 

def is_divisible(number, divisor):
    if number % divisor == 0:
        return True
    else:
            return False
num = int(input("What is the number:")) 
div = int(input("What is the divisor:"))

if is_divisible(num, div):
    print(f"{num} is divisible by {div}")
          
else:
  print(f"{num} is not divisible by {div}")
