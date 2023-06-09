#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem Set 1a
# In Part A, we are going to determine how long it will take you to save enough 
# money to make the down payment given the following assumptions: 
 
# 1. Call the cost of your dream home ​total_cost​. 
# 2. Call the portion of the cost needed for a down payment ​portion_down_payment​. For 
# simplicity, assume that portion_down_payment = 0.25 (25%). 
# 3. Call the amount that you have saved thus far ​current_savings​. You start with a current 
# savings of $0. 
# 4. Assume that you invest your current savings wisely, with an annual return of ​r ​(in other words, 
# at the end of each month, you receive an additional ​current_savings*r/12​ funds to put into 
# your savings – the 12 is because ​r​ is an annual rate). Assume that your investments earn a 
# return of r = 0.04 (4%). 
# 5. Assume your annual salary is ​annual_salary​. 
# 6. Assume you are going to dedicate a certain amount of your salary each month to saving for 
# the down payment. Call that ​portion_saved​. This variable should be in decimal form (i.e. 0.1 
# for 10%). 
# 7. At the end of each month, your savings will be increased by the return on your investment, 
# plus a percentage of your ​monthly salary ​(annual salary / 12). 
 
# Write a program to calculate how many months it will take you to save up enough money for a down 
# payment. You will want your main variables to be floats, so you should cast user inputs to floats.   1

# Your program should ask the user to enter the following variables: 
# 1. The starting annual salary (annual_salary) 
# 2. The portion of salary to be saved (portion_saved) 
# 3. The cost of your dream home (total_cost)

#P# prompt user for annual salary, portion saved, and total_cost
anual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))


#P# initialize variables
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = anual_salary / 12
monthly_savings = monthly_salary * portion_saved
months = 0

#P# Calulate basic constant values
down_payment = total_cost * portion_down_payment

#P# loop until current savings is greater than or equal to down payment
while current_savings < down_payment:
    #P# calculate monthly savings due to investment return
    monthly_return = current_savings * r / 12
    #P# add monthly savings to current savings
    current_savings += monthly_return + monthly_savings
    #P# increment number of months
    months += 1

#P# print number of months
print("Number of months:", months)



# Test Case 1
# Enter your annual salary: 120000
# Enter the percent of your salary to save, as a decimal: .10
# Enter the cost of your dream home: 1000000
# Number of months: 183

# Test Case 2
# Enter your annual salary: 80000
# Enter the percent of your salary to save, as a decimal: .15
# Enter the cost of your dream home: 500000
# Number of months: 105

# Test Case 3
# Enter your annual salary: 75000
# Enter the percent of your salary to save, as a decimal: .05
# Enter the cost of your dream home: 1500000
# Number of months: 261

