import os 
import csv
import statistics

# Open csv file
file = os.path.join('.', 'Resources', 'budget_data.csv')
# Variables
total_months = []
total_profit = []
monthly_profit_change = []
 
# Open csv
with open(file) as csvfile:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(csvfile,delimiter=",") 

    # Skip header 
    header = next(csvreader)  

    # Iterate through the rows
    for row in csvreader: 

        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through profits in order to get the monthly change in profits
    for month_change in range(len(total_profit)-1):
        
        # Difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[month_change+1]-total_profit[month_change])
        
# Max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Max and min to the proper month using month list and index from max and min
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_file = os.path.join('.', 'Analysis', 'Financial_analysis.txt')

with open(output_file,"w") as file:
    
# Write methods to print to Financial Analysis 
    file.write("Financial Analysis\n")
    
    file.write("----------------------------\n")
    
    file.write(f"Total Months: {len(total_months)}\n")
    
    file.write(f"Total: ${sum(total_profit)}\n")
    
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n")
    
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
    
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")

