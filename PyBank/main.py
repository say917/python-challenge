import os
import csv

csv_path=os.path.join(".",'Resources',"PyBank.csv")

#Lists to store data
def print_profit(date_data):
    date=str(date_data[0])
    profit_loss=int(date_data[1])

    #Count for Month
    total_months=date.count()

print(f"There are + {str(total_months)} + months")


#sourcing from analyticsvidhya.com
#file= open('Resources.csv','r')
#csvpath=os.path.join("PyBank",Resources.csv")

#type(file)

with open(csv_path) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=",")

    header=next(csvreader)

    for row in csvreader:
        #date.append(row[0])
        #profit_loss.append(row[1])
        #print(row[0])
        #print(row[1])