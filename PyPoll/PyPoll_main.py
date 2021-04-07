# import modules / dependencies
import os
import csv

csv_file_path = os.path.join(".", "Resources", "election_data.csv")
# print(csv_file_path)
# Initialize variables
total_votes = 0
total_khan = 0
total_correy = 0
total_li = 0
total_otooley = 0
winner = 0

with open(csv_file_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    
    # # Read the Header
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        if row[3] == str(khan):


output = (
    f"Election Results\n"
    f"------------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------------------------\n"
    f"Khan: {total_khan}\n"
    f"Correy: {total_correy}\n"
    f"Li: {total_li}\n"
    f"O'Tooley: {total_otooley}\n"
    f"------------------------------------\n"
    f"Winner: {winner}\n"
)

print(output)