# Import dependencies
import os
import csv

# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Assign file location with the pathlib library
csvpath = os.path.join('Resources', 'election_data.csv')

# Open csv in default read mode with context manager
with open(csvpath, newline='') as csvfile:

    # Store data under the csvreader variable
    csvreader = csv.reader(csvfile, delimiter=',') 

    # Skip the header so we iterate through the actual values
    csv_header = next(csvfile)    

    #Read each row of data after the Header
    for row in csvreader:

        #Calculate Total Number of Votes Cast
        total_votes += 1

        #Calculate Total Number of Votes Each Candidate Won
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

           # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output files Assign output file location and with the pathlib library
output_file = os.path.join("Resources", "Election_Data_Revised.txt")

with open(output_file,'w') as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"----------------------------\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})\n")
    file.write(f"----------------------------\n")
    file.write(f"Winner: {key}\n")
    file.write(f"----------------------------\n")



