#import OS and CSV
import os
import csv 

#files to load and export
load_file = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join("budget_analysis.txt")

#Set variables
months = 1
month_change = []
net_change_list = []
largest_increase = ["", 0]
greatest_loss = ["", 9999999999999999999]
net = 0

#Read csv and convert into lists. 
with open(load_file) as financial_data:
    reader = csv.reader(financial_data)

    #skip the header
    header = next(reader)

    #extract first row
    first_row = next(reader)

    net = net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        #track totals
        months = months + 1
        net = net + int(row[1])

        #track the change 
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_change = month_change + [row[0]]

        #calc the greatest increase
        if net_change > largest_increase[1]:
            largest_increase[0] = row[0]
            largest_increase[1] = net_change

        #calc the greatest decrease
        if net_change < greatest_loss[1]:
            greatest_loss[0] = row[0]
            greatest_loss[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${net_change}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {largest_increase[0]} (${largest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_loss[0]} (${greatest_loss[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
