import os
import csv

csv_path = os.path.join("Resources","election_data.csv")

total_votes = 0
candidates = {}

print ("Election Results")
print ("------------------------")

# Open and read csv
with open(csv_path, newline="", encoding = "utf-8") as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    csvheader = next(election_data)

    for row in election_data:
        total_votes += 1

        if row[2] not in candidates:
            candidates[row[2]]=0
        candidates [row[2]] +=1

    winner_name = max(candidates, key=candidates.get)
        
print ("Total Votes:"+ str(total_votes))
print ("------------------------")

for row in candidates:
    print (row + ": " + str(round(candidates[row]/total_votes*100)) + "% (" + str(candidates[row]) + ")")
print ("------------------------")
print ("Winner: "+ str(winner_name))
print ("------------------------")

