# Importing dependencies
import csv
import os

# Assigning a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
# Assigning a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initalizing vote counter variable
total_votes = 0
# Initializing the candidate options list and candiate votes dictionary
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
            # Add the candidate to the candidate list
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results \n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n")
    print (election_results, end= "")
    # Save the final vote count to the text file
    txt_file.write(election_results)
    
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their vote count, and percentage to the terminal
        candidate_results = print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #Print the winning candidates' resutls to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Saving the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)