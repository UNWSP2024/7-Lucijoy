# Author: Lucia Floan
# Date: March 7, 2025
# Title: Rainfall

# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

def calculate_rainfall():
  rainfall = []
  for i in range(12):  # A loop for 1-12 months
    rainfall.append(float(input(f'Enter the rainfall for month {i + 1}: ')))  

  print('The total rainfall was:', sum(rainfall))
  print('The average rainfall was:', sum(rainfall) / 12)
  print('The highest rainfall was:', max(rainfall), 'in month', rainfall.index(max(rainfall)) + 1)
  print('The lowest rainfall was:', min(rainfall),'in month', rainfall.index(min(rainfall)) + 1)

calculate_rainfall()

  
