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
candidates = {}

with open(csv_file_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    
    # # Read the Header
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    counter = 0
    candidates = []
    previous_candidate = 0
    for row in csv_reader:
        # calculate total votes
        total_votes = total_votes + 1
        candidates = str(row[2])
        candidates = set(candidates)
        print(candidates)

        # # create variable to hold candidates
        # for name in candidates:
        #     # if counter >= 1
        #     #     candidates.append(str(row[2])
        #     # if row[2] == previous_candidate
        #     # print(candidates)
            

# output = (
#     f"Election Results\n"
#     f"------------------------------------\n"
#     f"Total Votes: {total_votes}\n"
#     f"------------------------------------\n"
#     f"Khan: {total_khan}\n"
#     f"Correy: {total_correy}\n"
#     f"Li: {total_li}\n"
#     f"O'Tooley: {total_otooley}\n"
#     f"------------------------------------\n"
#     f"Winner: {winner}\n"
# )

# print(output)