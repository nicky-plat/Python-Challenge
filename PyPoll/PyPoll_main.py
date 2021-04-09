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
pct_khan = 0
pct_correy = 0
pct_li = 0
pct_otooley = 0
winner = 0

with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file)

    total_votes = 0
    total_khan = 0
    total_correy = 0
    total_li = 0
    total_otooley = 0
    winner = 0
    counts = {}
    # Read the Header
    csv_header = next(csv_file)
    # print(f"Header: {csv_header}")

    for row in csv_reader:
        # Find vote totals
        total_votes = total_votes + 1

        # Find votes for each candidate
        if row[2] == "Khan":
            total_khan = total_khan + 1

        elif row[2] == "Correy":
            total_correy = total_correy + 1

        elif row[2] == "Li":
            total_li = total_li + 1

        else:
            total_otooley = total_otooley + 1

    # Find percent totals for each candidate
    pct_khan = round((total_khan/total_votes)*100,3)
    pct_correy = round((total_correy/total_votes)*100,3)
    pct_li = round((total_li/total_votes)*100,3)
    pct_otooley = round((total_otooley/total_votes)*100,3)


# print(total_votes)
    
    #     voterID.append(col['Voter ID'])
    #     county.append(col['County'])
    #     candidate.append(col['Candidate'])
    #     candlist = Counter(candidate)
    # print(candlist)
    #     for name in candidate:
    #         if name == "Khan":
    #             name_khan.append(name)
    #             total_khan = name_khan.count
    #         elif name == "Correy":
    #             name_correy.append(name)
    #             total_correy = name_correy.count
    #         elif name == "Li":
    #             name_li.append(name)
    #             total_li = name_li.count
    #         else:
    #             name_otooley.append(name)
    #             total_otooley = name_otooley.count
            
    #         total_votes = total_votes + 1
        
        # pct_khan = sum(total_khan) / (total_votes -1) * 100
        # pct_li = sum(total_li) / (total_votes - 1) * 100
        # pct_correy = sum(total_correy) / (total_votes -1) * 100
        # pct_otooley = sum(total_otooley) / (total_months - 1) * 100
       
# Summary table            
output = (
    f"Election Results\n"
    f"------------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------------------------\n"
    f"Khan: {pct_khan}% ({total_khan})\n"
    f"Correy: {pct_correy}% ({total_correy})\n"
    f"Li: {pct_li}$ ({total_li})\n"
    f"O'Tooley: {pct_otooley}% ({total_otooley})\n"
    f"------------------------------------\n"
    f"Winner: {winner}\n"
)
print(output)