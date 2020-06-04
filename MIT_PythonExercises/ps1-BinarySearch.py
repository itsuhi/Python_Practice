# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:23:28 2019

@author: kakuitsuhi
"""
#
#total_cost = float(input("Tell me the cost of your house: "))
#portion_down_payment = 0.25
#down_payment = total_cost * portion_down_payment
#current_savings = 0
#investment_return = 0.04
#portion_saved = float(input("What is the portion of salary to be saved? "))
#annual_salary = float(input("Please enter your annual salary: "))
#monthly_salary = annual_salary / 12
#saved_salary = monthly_salary * portion_saved
#months_take = 0
#while current_savings < down_payment:
#    current_savings = current_savings + current_savings * (investment_return / 12) #order is important with 
#    current_savings = current_savings + saved_salary                                #these two statements
#    
#    months_take = months_take + 1
#print(months_take)


### Now consider salary raise
###total_cost = float(input("Tell me the cost of your house: "))
###portion_down_payment = 0.25
###down_payment = total_cost * portion_down_payment
###current_savings = 0
###investment_return = 0.04
###semi_annual_raise = float(input("Please enter your salary raise percentage: "))
###portion_saved = float(input("What is the portion of salary to be saved? "))
###annual_salary = float(input("Please enter your annual salary: "))
###monthly_salary = annual_salary / 12
###saved_salary = monthly_salary * portion_saved
###months_take = 0
###while current_savings < down_payment:
#     current_savings = current_savings + current_savings * (investment_return / 12)
##        
###    current_savings = current_savings + saved_salary
###    
###    months_take = months_take + 1
###    if months_take % 6 == 0:
###        annual_salary = annual_salary + annual_salary * semi_annual_raise
###        monthly_salary = annual_salary / 12
###        saved_salary = monthly_salary * portion_saved
###print(months_take + 1)

#Problem C
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0
investment_return = 0.04
semi_annual_raise = 0.07
annual_salary = float(input("Please enter your annual salary: "))
monthly_salary = annual_salary / 12
target_month = 36
high_rate = 10000
low_rate = 0
target_rate = (high_rate + low_rate) // 2   #integer division
step = 0

while abs(current_savings - down_payment) >= 100:
    # I want to calculate the savings after 36months for each target rate;
    # Therefore for each new cycle I need to rest some value
    current_savings = 0
    base_annual_salary = annual_salary
    monthly_salary = base_annual_salary / 12
    salary_saved = monthly_salary * (target_rate / 10000)
    for month in range(1, 37):
        
        cuurent_savings = current_savings + current_savings * (investment_return / 12)
        current_savings = current_savings + salary_saved
        if month % 6 == 0:
            base_annual_salary = base_annual_salary + base_annual_salary * semi_annual_raise
            monthly_salary = base_annual_salary / 12
            salary_saved = monthly_salary * (target_rate / 10000)
    
    savings_total = current_savings
    temp_rate = target_rate
    if current_savings > down_payment:
        high_rate = target_rate
    else:
        low_rate = target_rate
    target_rate = int((high_rate + low_rate) // 2)
    step = step + 1
    if temp_rate == target_rate:
        print("It is not possible to save for the down payment.")
        break

        
print(target_rate / 10000)
print(step)
        
    
    
