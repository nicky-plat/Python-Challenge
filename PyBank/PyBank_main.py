# import modules / dependencies
import os                        # os to join elements of the file path
import csv                       # read csv file using .reader method

csv_file_path = os.path.join(".", "Resources", "budget_data.csv")
# print(csv_file_path)


# Initialize variables
total_months = 0
total = 0 
total_change = 0
average_change = 0
amount_diff = 0
increase_amt = 0
decrease_amt = 0
greatest_increase = ["", 0] # positive change
greatest_decrease = ["", 999999999] # negative change

#-------------------------------------------------------------------
# Open and read the csv_file called budget_data.csv
with open(csv_file_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    
    # # Read the Header
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # # Read through each row in the csv file from row 2 to end
    previous_row_total = 0
    counter = 0
    list_difference = []
    total_change = []
    total = 0

    for row in csv_reader:
        # print(row[0], row[1])
        # print(row[1], previous_row_total, counter, list_difference)
        if counter >= 1:
            list_difference.append(int(row[1]) - int(previous_row_total))
            # taking m-t-m diff and storing in variable
            amount_diff =  (int(row[1]) - int(previous_row_total))
            counter = counter + 1
            previous_row_total = row[1]
                # take stored m-t-m data and compare to previous amt
            if amount_diff > increase_amt:
                # update to new amt
                increase_amt = amount_diff
                increase_date = row[0]
            elif amount_diff < decrease_amt:
                # update to new amt
                decrease_amt = amount_diff
                decrease_date = row[0]

        else:
            counter = counter + 1
            previous_row_total = row[1]

        # sort list_difference values to identify greatest increase/decrease
        list_difference.sort()
        # print to test output
        # print(max(list_difference))
        # calculate total months
        total_months = total_months + 1        
        # print(total_months)
        # calculate total profit/loss
        total = total + int(row[1])
        # print(total)  
        
    # print(row[1], previous_row_total, counter, list_difference)

    # calculate month-to-month change
    # print(sum(list_difference))
    # calculate average change
    average_change = sum(list_difference) / (total_months -1)
    # print(average_change)
    # print(row[0], row[1])

# print(total_change)

    
#         # use conditional to see if current change greater than greatest_increase
#             #if greater than replace current values in greatest_increase

#         # USE CONDITIONAL TO SEE IF CURRENT CHANGE BIGGER THAN greatest_decrease
#             # if bigger negative number then replsce values in greatest_decrease

# # calculate total

# # calculate total change

# # average_change = total_change / (total months - 1)
# # print()
# # -------------------------------------------------------


# #Create summary table
output = (
    f"Financial Analysis\n"
    f"-----------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase}\n"
    f"Greatest Decrease in Profits: {greatest_decrease}\n"
)

print(output)

print(increase_amt)
print(decrease_amt)
print(increase_date)
print(decrease_date)