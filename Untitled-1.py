#The data we need to retrieve. (Add our dependencies.)
import csv
##dir(csv)
import os
##dir(os.path)

#Location of csv file. 
#Assign a variable for the file to load from a path (indirect path).
#file_to_load=os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path.
#file_to_save=os.path.join("analysis","election_analysis.txt")



#Assign a variable for the file to load and the path (direct path).
file_to_load="Resources/election_results.csv"
#Open the election results and read the file.
    election_data=open(file_to_load,'r')
#To do: perform analysis
#Close the file.
election_data.close()
#Allows file to be referenced throughout the script without open/close code. (encoding='utf-8' code from https://stackoverflow.com/questions/42070668/python-3-default-encoding-cp1252)
with open(file_to_load,encoding='utf-8') as election_data:
##    print(election_data)



#Initialize a total vote counter.
    total_votes=0

#Create list for candidate options.
candidate_options=[]

#Declare the empty dictionary.
candidate_votes={}

#Winning candidate and winning count tracker.
winning_candidate=""
winning_count=0
winning_percentage=0

#open & read election results csv file
with open(file_to_load,encoding='utf-8') as election_data:
    #Print the file object.
    ##print(election_data)

#To do: read and analyze the data here
#Read the file object with the reader function.
    file_reader=csv.reader(election_data)
        
    #Print the header row.
    headers=next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
         #2. Add to the total vote count.
        total_votes+=1
        
        #Print the candidate name from each row.
        candidate_name=row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0
        #Add increment votes to that candidate's count.
        candidate_votes[candidate_name]+=1

#Save the results to our text file.
with open(file_to_save,"w") as txt_file:
    
    #Print each candidate, their voter count and percentage to the terminal.
    election_results=(
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------")
    print(election_results)
   
    #Save the candidate results to the text file.
    txt_file.write(election_results)

    #Determine the % of votes for each candidate by looping through the counts.
    #Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate.
        votes=candidate_votes[candidate_name]
        #Calculate the % of votes.
        vote_percentage=float(votes)/float(total_votes)*100

        #Print the candidate name and % of votes
        ##print(f"{candidate_name}:received{vote_percentage:.2f}% of the vote.")

        #Print out each candidate's name, vote count, % of votes to the terminal.
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        
        #Save the candidate results to the text file.
        txt_file.write(candidate_results)       

        #Determine winning vote count and candidate.
        #Determine if the votes is greater than the winning count.
        if(votes>winning_count) and (vote_percentage>winning_percentage):
        #If true then set winning_count=votes and winning_percent=vote_percentage
            winning_count=votes
            winning_percentage=vote_percentage
        #And set the winning_candidate equal to the candidates's name.
            winning_candidate=candidate_name

    #Print the winning candidate's results to the terminal.
    winning_candidate_summary=(
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")

    print(winning_candidate_summary)
    #Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)