import os
import csv

csv_path=os.path.join("election_data.csv")

#Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
total_votes=0

with open(csv_path) as csvfile:
    header=csvfile.__next__()
    
    for row in csv.reader(csvfile):
        total_votes = total_votes + 1
        names = row[2]
        
        if names not in candidate_options:
            candidate_options.append(names)
            candidate_votes[names] = 0
        candidate_votes[names] = candidate_votes[names] + 1
print(candidate_votes)

for win in candidate_votes:
    votes = candidate_votes.get(win)
    

    vote_percentage = float(votes) / float(total_votes) * 100
    

    if (votes > winning_count):
        winning_count = votes
        winning_candidate = win
                 


with open("analysis.txt",'w') as file:
    file.write("Election Results")
    file.write("\n")
    file.write("-----------------------")
    file.write("\n")
    #total_votes = 369711
    file.write(f"Total Votes: {total_votes}")

    file.write("\n")
    file.write("-----------------------")
    file.write("\n")
    for win in candidate_votes:
        votes = candidate_votes.get(win)
        vote_percentage = float(votes) / float(total_votes) * 100
    
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = win
        voters_details = f"{win}: {vote_percentage:.3f}% ({votes})\n"
        file.write(f"{voters_details}")
    file.write("-----------------------")
    file.write("\n")
    file.write(f"Winner: {winning_candidate}")
    file.write("\n")
    file.write("-----------------------")
