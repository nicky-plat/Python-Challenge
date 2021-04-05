# import modules / dependencies
import os                        # os to join elements of the file path
import csv                       # read csv file using .reader method

csv_file_path = os.path.join(".", "Resources", "budget_data.csv")
# print(csv_file_path)

def print_profitloss(column):
    # Define variables
    month = column[0]
    money = column[1]

# Initialize variables
total_months = 0
total = 0
total2 = 0
total3 = 0
average_change = 0
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

    for row in csv_reader:
        previous_row_total = row[1]
        counter = counter + 1
        if counter > 2:
            if row[1] > previous_row_total:
                print(previous_row_total)
                print(counter)
            else 



        # if int(row[1]  > int(row[1]):
        #     print(row[1])


        # total2 = row[1]
        # sum = sum(total2)
        # print(sum)

#         print(row[0], row[1])

#         # increased total_months by 1
#         total_months = total_months + 1

#         if total_months + 1 > total_months:
#             # go to next row
#             print("what now")

#         else:
#             print("what")

#         # calculate the month to month change
#          # sum total Profit/Losses (second column of csv file)
#         # total_change
        
#         # Need to start on second month 
    
#         # use conditional to see if current change greater than greatest_increase
#             #if greater than replace current values in greatest_increase

#         # USE CONDITIONAL TO SEE IF CURRENT CHANGE BIGGER THAN greatest_decrease
#             # if bigger negative number then replsce values in greatest_decrease
            
#         #----------------------------------------------
#         # setup variables for next iteration (next row)
#         # set prior_value = current_row

# # calculate total

# # calculate total change

# # average_change = total_change / (total months - 1)
# # print()
# # -------------------------------------------------------


# # #Create summary table
# output = (
#     f"Financial Analysis\n"
#     f"-----------------------------------\n"
#     f"Total Months: {total_months}\n"
#     f"Total: {total}\n"
#     f"Average Change: {average_change}\n"
#     f"Greatest Increase in Profits: {greatest_increase}\n"
#     f"Greatest Decrease in Profits: {greatest_decrease}\n"
# )

# print(output)
