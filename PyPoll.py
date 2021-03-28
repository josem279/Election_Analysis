# Importing dependencies
import csv
import os

# Assigning a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
# Assigning a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initalizing vote counter variable
total_votes = 0

# Initializing the candidate options list
candidate_options = []

#Initializing an empty dictionary for candidate votes
candidate_votes = {}

# Opening the election results and reading the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Reading the header row
    headers = next(file_reader)

    # Printing each row in the CSV file
    for row in file_reader:
        # Adding to the total vote count
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing cadidate add that candidate to the list of candidates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")
