# import modules / dependencies
from collections import Counter
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
name_khan = 0
name_correy = 0
name_li = 0
name_otooley = 0
winner = 0
counts = {}

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # creating empty lists
    voterID = []
    county = []
    candidate = []
    total_votes = 0
    total_khan = 0
    total_correy = 0
    total_li = 0
    total_otooley = 0
    name_khan = []
    name_correy = []
    name_li = []
    name_otooley = []
    winner = 0
    counts = {}
    # # Read the Header
    # csv_header = next(csv_file)
    # print(f"Header: {csv_header}")
    count = 0
    counter = 0
    previous_candidate = 0

    # create variable to hold candidates
    for col in csv_reader:
        voterID.append(col['Voter ID'])
        county.append(col['County'])
        candidate.append(col['Candidate'])
        # print('Candidates:', candidate)
        for name in candidate:
            if name == "Khan":
                name_khan.append(name)
                total_khan = name_khan.count
                print(total_khan)
            
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