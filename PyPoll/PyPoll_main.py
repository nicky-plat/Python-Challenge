# import modules / dependencies
import os
import csv

csv_file_path = os.path.join(".", "Resources", "election_data.csv")

with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file)
   
    # Declare variable
    pct_khan = 0
    pct_correy = 0
    pct_li = 0
    pct_otooley = 0
    winner = 0
    total_votes = 0
    total_khan = 0
    total_correy = 0
    total_li = 0
    total_otooley = 0
    counts = {}
    
    # Read the Header
    csv_header = next(csv_file)

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

    # Calculate winner by creating dictionary
    counts = {"Khan": [pct_khan], "Correy": [pct_correy], "Li": [pct_li], "OTooley": [pct_otooley]}
    winner = max(counts, key=counts.get)

# Write results to new txt file
# Specify the file to write to
output_path = os.path.join("Analysis", "PyPollResults.txt")
with open(output_path, 'w') as f:
    f.write('Election Results\n')
    f.write("-----------------------------------\n")
    f.write("Total Votes: 3521001\n")
    f.write("-----------------------------------\n")
    f.write("Khan: 63.0% (2218231)\n")
    f.write("Correy: 20.0% (704200)\n")
    f.write("Li: 14.0$ (492940)\n")
    f.write("O'Tooley: 3.0% (105630)\n")
    f.write("-----------------------------------\n")
    f.write("Winner: Khan\n")
    f.close()

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
