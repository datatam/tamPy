#!/usr/bin/env python
# coding: utf-8

# ## Part C: Finding the right amount to save away
# In Part B, you had a chance to explore how both the percentage of your salary that you save each month  and your annual raise affect how long it takes you to save for a down payment.  This is nice, but  suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years.  How much should you save each month to achieve this?  In this problem, you are going to write a  program to answer that question.  
# 
# To simplify things, assume:  
# 1. Your semi-annual raise is .07 (7%)  
# 2. Your investments have an annual return of 0.04 (4%)   
# 3. The down payment is 0.25 (25%) of the cost of the house  
# 4. The cost of the house that you are saving for is $1M. 
# 
# You are now going to try to find the best rate of savings to achieve a down payment on a 1 Million USD house in  36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of  the required down payment.
# In <b>ps1c.py</b>, write a program to calculate the best savings rate, as a function of your starting salary.  You should use <b>bisection search</b> to help you do this efficiently. You should keep track of the number of  steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote  for part B in this problem.     Because we are searching for a value that is in principle a float, we are going to limit ourselves to two  decimals of accuracy (i.e., we may want to save at 7.04% -- or 0.0704 in decimal – but we are not  going to worry about the difference between 7.041% and 7.039%).  This means we can search for an  <b>integer</b> between 0 and 10000 (using integer division), and then convert it to a decimal percentage  (using float division) to use when we are calculating the <b>current_savings</b> after 36 months. By using  this range, there are only a finite number of numbers that we are searching over, as opposed to the  infinite number of decimals between 0 and 1. This range will help prevent infinite loops. The reason we  use 0 to 10000 is to account for two additional decimal places in the range 0% to 100%. Your code  should print out a decimal (e.g. 0.0704 for 7.04%).    Try different inputs for your starting salary, and see how the percentage you need to save changes to  reach your desired down payment.  Also keep in mind it may not be possible for to save a down  payment in a year and a half for some salaries. In this case your function should notify the user that it  is not possible to save for the down payment in 36 months with a print statement. <b>Please make your  program print results in the format shown in the test cases below.</b>
# 
# <b>Note: There are multiple right ways to implement bisection search/number of steps so your  results may not perfectly match those of the test case. </b>
# 
# 
# 
# 

# In[70]:


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))


# In[71]:


total_cost = float("1000000") #cost of house
portion_down_payment = float(0.25*total_cost)  #downpayment for this house
semi_annual_raise = float("0.07") #7.00%
r = 0.04 #rate of return


# print(portion_down_payment)
# print(monthly_salary)
# print(r)
# print(current_savings)
# print(portion_saved)

# In[72]:


monthly_salary = annual_salary/12
current_savings = float(0)
i = 0
while current_savings < portion_down_payment:
    current_savings = current_savings + current_savings*r/12 + monthly_salary*portion_saved
    if i==0:
        monthly_salary = monthly_salary
    elif i%6==0:
        monthly_salary = monthly_salary + monthly_salary*semi_annual_raise
    i = i+1
print("Number of months:", i)
print("Number of months:", s)


# In[1]:


tam=float("100.012")


# In[2]:


tam


# In[ ]:




