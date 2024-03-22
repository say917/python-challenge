import os
import csv

csv_path=os.path.join("PyBank.csv")

with open(csv_path) as csvfile:
    header=csvfile.__next__()
    totalMonths=csvfile.readlines()

with open(csv_path) as csvfile:
    header=csvfile.__next__()
    totals=0
    for row in csv.reader(csvfile):
        totals += int(row[1]) 

with open(csv_path) as csvfile:
    header=csvfile.__next__()
    total_months = 0
    total_amount = 0
    previous_amount = 0
    current_amount = 0
    changes = []
    change_months = list()
    total_change = 0
    average_change = 0 
    max_change = 0
    min_change = 0
    
    for row in csv.reader(csvfile,delimiter=","):
        current_amount = int(row[1])
        if total_months > 0:
            changes.append(int(current_amount)-int(previous_amount))
            change_months.append(str(row[0]))
        total_months = total_months + 1
        total_amount = total_amount + int(current_amount)
        previous_amount=current_amount
    
    for change in changes:
        total_change = total_change + change
    
    average_change = total_change/total_months
    max_change = max(changes)
    min_change = min(changes)

    max_counter = 0
    for change in changes:
        max_counter = max_counter + 1
        if change == max_change:
            break

    min_counter = 0
    for change in changes:
        min_counter = min_counter + 1
        if change == min_change:
            break


with open("analysis.txt",'w') as file:
    file.write("\n")
    file.write("Financial Analysis")
    file.write("\n")
    #file.newlines
    file.write("\n")
    file.write("-----------------------")
    file.write("\n")

    file.write(f"Total Months: {total_months}")
    file.write("\n")
    
    file.write(f"Total: ${total_amount}")
    file.write("\n")
    
    file.write(f"Average Change: {int(average_change)}")
    file.write("\n")
    
    file.write(f"Greatest Increase in Profits: {str(change_months[max_counter])} {max_change}")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {str(change_months[min_counter])} {min_change}")
 