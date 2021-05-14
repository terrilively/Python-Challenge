# Import Modules
import os
import csv

# Declare Variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greates_decrease_month = 0

#Set Path for File
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open and Read CSV File
with open(csvpath, newline='') as csvfile:

    #CSV Reader - Delimiter & Variable
    csvreader = csv.reader(csvfile, delimiter=',')

    #CSV Reader - Read the Header Row - Skip if there is no Header
    csv_header = next(csvreader)
    #row = next(csvreader)

    
 #Read each row of data after the header
    for row in csvreader:
     #Calculate Total Number of Months, Net Amount of "Profit/Losesses" & Set Variable for Rows
        previous_row = int(row[1])
        total_months += 1
        net_amount += int(row[1])
        greatest_increase = int(row[1])
        greatest_increase_month = row[0]


        #Calculate Total Number of Months Included in Dataset
        total_months +=1
        #Calcualte Net Amount of Profit/Losses over the entire period
        net_amount += int(row[1])

        #Calculate Change From Current month to Previous Month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        #Calculate The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        #Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

        #Calculate The Average & Date
        average_change = sum(monthly_change)/ len(monthly_change)

        highest = max(monthly_change)
        lowest = min(monthly_change)

     
# Print Statements
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${lowest})")

# Output files
output_file = os.path.join('Resources', 'budget_data_revised.txt')

#Open file using "Write" Mode.  Indicate Variables to hold the contents
with open(output_file,'w') as file:

    
# Write methods to print to Financial_Analysis_Summary 
    file.write(f"Financial Analysis\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_amount}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month}, (${highest})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${lowest})\n")

    file.close()