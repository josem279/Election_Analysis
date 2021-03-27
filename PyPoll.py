import pandas as pd
import numpy as np

# The data we need to retrieve

# 1. The total number of votes cast

election_results = pd.read_csv("resources/election_results.csv", )

total_votes = election_results["Ballot ID"].count()
print(total_votes)

# 2. A complete list of candidates who received votes
candidates = election_results["Candidate"].unique()
print(candidates)

# # 3. The percentage of votes each candidate won.
# candidate_percent = election_results["Candidate"].groupby("Candidate") / total_votes
# print(candidate_percent)

# 4. The total number of votes each candidate won.
votes_by_candidate = dict(election_results.groupby("Candidate").count()["Ballot ID"])
print(votes_by_candidate)

# 5. The winner of the election based on popular vote.
print(sorted(votes_by_candidate.keys()))