#import OS and CSV
import os
import csv
#create the path
csvpath = os.path.join('Resources', 'budget_data.csv')

dates = []
nums = []

#open that stuff
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skip first header 
    for row in csvreader:
        dates.append(row[0]) # put everything into lists
        nums.append(row[1])

#remove column headers from each list               
del dates[0]
del nums[0]

#convert string into integer
for i in range (dates):
    







    

        
        