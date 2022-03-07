#The data we need to retrieve. (Add our dependencies.)
import csv
##dir(csv)
import os
##dir(os.path)

#Location of csv file. 
#Assign a variable for the file to load from a path (indirect path).
##?csvpath=os.path.join("Resources","election_results.csv")
file_to_load=os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")

#open & read election results csv file
##?with open(csvpath) as csvfile:
with open(file_to_load,encoding='utf-8') as election_data:
    #?code to read file
##?    real_csv_file=csv.reader(csvfile)
    #Print the file object.
    ##print(election_data)

#To do: read and analyze the data here
#Read the file object with the reader function.
    file_reader=csv.reader(election_data)
        
    #Print the header row.
    headers=next(file_reader)
    print(headers)


#1. The total number of votes cast.
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.




###  Below are practice coding from Module 3.  ###

#Import the datetime class from the datatime module.
#import datetime as dt
#Use the now() attribute on the datetime class to get the present time.
##now=dt.datetime.now()
#Print the present time.
##print("The time right now is ",now)


#Assign a variable for the file to load and the path (direct path).
##file_to_load="Resources/election_results.csv"
#Open the election results and read the file.
##election_data=open(file_to_load,'r')
#To do: perform analysis
#Close the file.
##election_data.close()
#Allows file to be referenced throughout the script without open/close code. (encoding='utf-8' code from https://stackoverflow.com/questions/42070668/python-3-default-encoding-cp1252)
##with open(file_to_load,encoding='utf-8') as election_data:
##    print(election_data)

#Using the open() function with the "w" mode we will write data to the file.
##outfile=open(file_to_save,"w")
#Write some data to the file.
##outfile.write("Hello World")
#Close the file
##outfile.close()

#Create a filename variable to a direct or indirect path to the file.
##file_to_save=os.path.join("analysis","election_analysis.txt")
#Using the with statement open the file as a text file.
##with open(file_to_save,"w") as txt_file:
    #Write some data to the file. (\n adds data to new line)
    ##txt_file.write("Counties in th Election\n-\nArapahoe\nDenver\nJefferson")

    #Print each row in the CSV file.
    ##for row in file_reader:
        ##print(row)
        
        #To print the first item in each row.
        ##for i in range(len(row)):
            ##print (row[0])