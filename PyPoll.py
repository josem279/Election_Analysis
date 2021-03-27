# Importing dependencies
import csv
import os

# Assigning a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
# Assigning a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initalizing vote counter variable
total_votes = 0

# Opening the election results and reading the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Reading the header row
    headers = next(file_reader)

    # Printing each row in the CSV file
    for row in file_reader:
        total_votes += 1
    
print(total_votes)