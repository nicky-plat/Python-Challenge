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

    # # Read through each row in the csv file from row 2 to end
    previous_row_total = 0
    counter = 0
    list_difference = []
    total_change = []
    total = 0

    for row in csv_reader:
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
    
        # calculate total months
        total_months = total_months + 1        
        # print(total_months)
        # calculate total profit/loss
        total = total + int(row[1])
        # print(total)  
        

    # calculate average change
    average_change = sum(list_difference) / (total_months -1)
    # print(average_change)
    # print(row[0], row[1])


# #Create summary table
output = (
    f"Financial Analysis\n"
    f"-----------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {increase_date} (${increase_amt})\n"
    f"Greatest Decrease in Profits: {decrease_date} (${decrease_amt})\n"
)

print(output)
