import csv

# File to load and file path. This file path changes as new csv's are referenced
file_to_load = "/Users/ncabayan/Desktop/Python-Challenges/PyBank/03_python_homework_Instructions_PyBank_Resources_budget_data.csv"

# Track various revenue parameters
total_months = 0
prev_Profits_Losses = 0
month_of_change = []
Profit_Loss_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as bank_data:
    reader = csv.DictReader(bank_data)

    for row in reader:
        print(row)
        # Track the total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        # Track the revenue change
        revenue_change = int(row["Profit/Losses"]) - prev_Profits_Losses
        prev_Profits_Losses = int(row["Profit/Losses"])
        Profit_Loss_change_list = Profit_Loss_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # Calculate the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # Calculate the greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change
# Calculate the Average Profit/Losses Change
Profit_Loss_change_list.pop(0)  

Profit_Loss_Change_avg = (sum(Profit_Loss_change_list) / len(Profit_Loss_change_list))

# Generate Result Summary
result = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${Profit_Loss_Change_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the result (to terminal)
print(result)