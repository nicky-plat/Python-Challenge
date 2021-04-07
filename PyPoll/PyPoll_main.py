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




output = (
    f"Election Results\n"
    f"------------------------------------"
    f"Total Votes: {total_votes}\n"
    f"------------------------------------"
    f"Khan: {total_khan}\n"
    f"Correy: {total_correy}\n"
    f"Li: {total_li}\n"
    f"O'Tooley: {total_otooley}\n"
    f"------------------------------------"
    f"Winner: {winner}\n"
)

print(output)