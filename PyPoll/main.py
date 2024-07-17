import os
import csv
# Path to collect data from the Resources folder
# vote_csv = os.path.join('..', 'Resources', 'election_data.csv')
vote_csv = r"C:\Users\Module 3\Starter_Code\PyPoll\Resources\election_data.csv"
if not os.path.exists(vote_csv):
    print("File does not exist.")
else:
    # Read in the CSV file
    with open(vote_csv,"r") as cscfile:
        # Split the data on commas
        csvreader = csv.reader(cscfile, delimiter=",")
        # header row
        header = next(csvreader)

        votes = {}
        total_votes = 0
        persons = []
        # Loop through the data - total votes
        for row in csvreader:
            total_votes += 1
            person = row[2]
            persons.append(person)
            if person in votes:
                votes[person] +=1
            else:
                votes[person] = 1
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    # Loop through the data - Each candidate’s total votes and percent of votes
    for person, vote_count in votes.items():
        percentage = (vote_count / total_votes) * 100
        print(f"{person}: {percentage:.3f}% ({vote_count})")
    # using Mac function finding the winner
    winner = max(votes, key=votes.get)
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")