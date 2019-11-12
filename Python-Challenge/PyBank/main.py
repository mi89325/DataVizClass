#import OS and CSV
import os
import csv
from statistics import mean

#create the path
csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
nums = []

#open that stuff
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    for row in csvreader:
        #put everything into lists
        months.append(row[0])
        nums.append(row[1])

#remove column headers from each list
del months[0]
del nums[0]

#convert string into integer
numsFloat = [float(i) for i in nums]

#Total of the row
Net = sum(numsFloat)

#Average of the row
Avg = Net/len(nums)

#Find max and min in the 
max_increase_value = max(nums)
max_decrease_value = min(nums)

#get the index 
max_increase_pos = nums.index(max(nums))
max_decrease_pos = nums.index(min(nums))


print("Financial Analysis")
print("-----------------------------")
print(f'The total months: {len(months)}')
print(f'Total number ${sum(numsFloat)}')
print(f'Average Change: ${Avg:,.2f}')
print(f'Greatest increase in profit: {months[max_increase_pos]} {float(max_increase_value)}') 
print(f'Greatest decrease in profit: {months[max_decrease_pos]} {float(max_decrease_value)}')

output = os.path.join("..","PyBank", "Financial_Analysis_Summary.txt")

with open(output, "w") as txtfile:
    print(f"Financial Analysis", file=txtfile)
    print(f"-----------------------------", file=txtfile)
    print(f'The total months: {len(months)}', file=txtfile)
    print(f'Total number ${sum(numsFloat)}', file=txtfile)
    print(f'Average Change: ${Avg:,.2f}', file=txtfile)
    print(f'Greatest increase in profit: {months[max_increase_pos]} {float(max_increase_value)}', file=txtfile) 
    print(f'Greatest decrease in profit: {months[max_decrease_pos]} {float(max_decrease_value)}', file=txtfile)





    

        
        