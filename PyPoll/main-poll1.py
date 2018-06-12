#hello this is main body
import csv
import os

csvpath = os.path.join('.', 'raw_data', 'election_data_1.csv')
output_path = os.path.join('election_results1.txt')

voter_list = []
candidate_list = []
unique1_list = []
votes = []
total_votes = 0
num = 0
pct_votes=[]
temp = 0

#---------------Unique FUNC------------
def unique(list1, unique_list):
    
    # intilize a null list
    unique_list = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)

    return unique_list

#--------------end func-----------------------

#Mental DMZ

#----------------------main program  code---------------


with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header and capture candidates and number of votes
    for row in csvreader:
        candidate_list.append(row[2])
        total_votes = total_votes + 1

#determine the unique candidatesd via function
unique1_list = unique(candidate_list, unique1_list)

#create vote list and percentage list analogous in size to the unique1_list
for i in range(0,(len(unique1_list))):
    votes.append(i)
    pct_votes.append(i)

#tabulate votes for each candidate within the unique list length or range
for i in range (0, len(unique1_list)):
    votes[(i)] = 0
    for x in candidate_list:
        if x == unique1_list[i]:
            votes[i] = votes[i] + 1
    pct_votes[i] = votes[i]/total_votes

# results output to screen and file in parallel
file = open("election1_results.txt", "w")


print("\n\nElection Results\n")
print ("-------------------")
print ("Total Votes: ", total_votes)

file.write("\n\nElection Results\n")
file.write("-------------------")
file.write("\nTotal Votes: ")
file.write(str(total_votes))


win_count = 0
winner = ""

print ("-------------------")
file.write("\n-------------------\n")

# there HAS GOT TO BE A BETTER WAY TO WRITE A TXT FILE THAN THIS :-))

for i in range (0, (len(votes))):
    if votes[i] > win_count:
        win_count = votes[i]
        winner = unique1_list[i]

    print (unique1_list [i], "{:.1%}".format(pct_votes[i]), "(", votes [i],")")
    file.write(str(unique1_list [i]))
    file.write(" ")
    temp = float((pct_votes[i]))
    file.write(str("{:.1%}".format(temp)))
    file.write("% ")
    file.write(" ")
    file.write("(")
    file.write(str(votes [i]))
    file.write(")")
    file.write("  \n")

print ("-------------------")
file.write("\n-------------------\n")

print ("Winner: ", winner, " with the winning number of Votes: ", win_count)
file.write("Winner: ")
file.write(winner)
file.write(" with the winning number of Votes: ")
file.write(str(win_count))
print ("-------------------\n\n")
file.write("\n-------------------\n\n")


file.close() #This close() is important

