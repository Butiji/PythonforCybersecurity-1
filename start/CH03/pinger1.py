#!/usr/bin/env python3
# First example of pinging from Python
# By 





name =input('What is your name: ')
color = input('What is your favorite color: ')
pet_name = input('What was your first pets name: ')
mother_maiden_name = input('What is your mothers maiden name: ')
elementary_school = input('What elementary school did you attend: ')
file = open("hackme.txt", mode = 'w',    encoding = 'utf-8')
file.write("Name =" + name + "\n"   +"color = "+color + "\n"+"Pet's Name = "+pet_name +"\n"+"Mother's Maiden Name = " + mother_maiden_name + "\n" +"Name of Elementary School = " + elementary_school)
file.close()










