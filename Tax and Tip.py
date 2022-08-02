# Project 6: Tax and Tip
'''The program that you create for this exercise will bigan by reading the cost 
of a meal ordered at a restaurant from the user. Then your program will compute
the tax and tip for the meal. Use your local tax rate when computing the amount 
of tax owing.Compute the tip as 18 percent of the meal amount(without the tax).
The output from your program should include the tax amount. the tip amount.and
the grand total for the meal including both the tax and the tip.Format the
output so that all of the values are displayed using two decimal places'''
price=int(input("enter value of food: "))
tax=(price*0.18)
tip=(price*0.18)
total_bill=price+tax+tip
print("the total bill payable is",total_bill)
