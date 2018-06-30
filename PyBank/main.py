import os
import csv

print ("Financial Analysis")
print ("-----------------------------------------------")

csv_path = os.path.join("Resources","budget_data.csv")

total_months = 0
total_revenue = 0
last_revenue = 0
new_change = 0
all_change = 0

minmax = {
    "min":["",0],
    "max":["",0]}


# Open and read csv
with open(csv_path, newline="", encoding = "utf-8") as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")
    csvheader = next(budget_data)

#Calculate the total months and total revenue
    for row in budget_data:
        total_months += 1
        revenue = int(row[1])
        total_revenue += revenue
        
        #Calculating the change
        if last_revenue != 0 :
            new_change = revenue - last_revenue
            all_change += new_change

        last_revenue = revenue
        
        if new_change >= minmax["max"][1]:
            minmax["max"][0]=row[0]
            minmax["max"][1]=new_change

        if new_change < minmax["min"][1]:
            minmax["min"][0] = row[0]
            minmax["min"][1] = new_change

    average_change = all_change / (total_months -1)


    print ("Total Months: "+ str(total_months)) 
    print ("Total: $" + str(total_revenue))
    print ("Average Change: $"+str(average_change))
    print("Greatest Increase in Profits: " + minmax["max"][0] + " $" + str(minmax["max"][1]))
    print("Greatest Decrease in Profits: " + minmax["min"][0] + " $" + str(minmax["min"][1]))


