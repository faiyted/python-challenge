import os
import csv


budget_csv = 'C:/Users/Module 3/Starter_Code/PyBank/Resources/budget_data.csv'
# Path to collect data from the Resources folder
# budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

if not os.path.exists(budget_csv):
    print("File does not exist.")
else:
    # Read in the CSV file
    with open(budget_csv, 'r') as csvfile:

        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')

        # header row
        header = next(csvreader)

        amount = []
        months = []
        changes = []
        # Loop through the data- Total Months/ Total Amount/ 
        for row in csvreader:
            amount.append(int(row[1]))
            months.append(row[0])

            total_months = len(set(months))
            total_amt = sum(amount)
        # Loop through the data- Fidning Average Change/ Greatest Increase/ Greatest Decrease
        for i in range(1, len(amount)):
            changes.append(amount[i] - amount[i-1])
            if len(changes)>0 :
                avg = sum(changes)/ len(changes)
            else:
                avg = 0  
            
            if changes:
                maxIncrease = max(changes)
                minDecrease = min(changes)
                maxMon = months[changes.index(maxIncrease)+1] 
                minMon = months[changes.index(minDecrease)+1] 

            else:
                maxIncrease = 0
                minDecrease= 0
                maxMon = ""
                minMon = ""
        # Print the results
        print("Financial Analysis")
        print("-------------------------")
        print("Total Months:", total_months)
        print("Total: $" + str(sum(amount)))
        print("Average Change: $" + str(round(avg, 2)))
        print(f"Greatest Increase in Profits: {maxMon} (${maxIncrease})")
        print(f"Greatest Decrease in Profits: {minMon} (${minDecrease})")
