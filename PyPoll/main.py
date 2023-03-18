import csv
import os

# Open csv file
file = os.path.join('.', 'Resources', 'election_data.csv')

# Output file
output_file = os.path.join('.', 'Analysis', 'election_results.txt')

# Variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# Read the CSV file and iterate over each row
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip header
    header = next(csvreader)

    for row in csvreader:

        
        # Add to total vote count
        total_votes +=1
        # Get candidate names from rows
        candidate_name = row[2]
        # If candiate doesnt not match. Loop is discovering candidates as it goes
        if candidate_name not in candidate_options:
            # Add to the list of candidates in the running
            candidate_options.append(candidate_name)
            # Begins traching candidat voter count
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] +1
# Print results and export to text file
with open (output_file, "w") as txt_file:
    # Print to terminal
    election_results = (
        f"Elections Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------------\n")
    print(election_results, end="")
    
    txt_file.write(election_results)
    
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
    
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print (voter_output, end="")

        txt_file.write(voter_output)

    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"---------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)