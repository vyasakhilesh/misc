# Run this program on the command line like this:
#    python NaiveSequenceMiner.py sequential-data.txt 1000 > frequent_patterns.txt

# Import libraries
import sys
import time

start_time = time.time()
inputfile    = "seq-test.txt"     #sys.argv[1]
abs_min_supp =  1000                     #int(sys.argv[2])

# Read the data
with open(inputfile,"r") as f:
    sequences = f.read().split("\n")

# Naive (Apriori-like) substring miner	

# Initialization

# a list of symbols that appear in the sequences
# NOTE that it should be updated if the script is used with another data
#symbols = ['a','b','c','d','e','f','g','h','i','j']
symbols = ['a','b','c']

all_frequent = [] # List of ALL frequent sequences
curr_frequent = [] # List of frequents sequences that were found in the current iteration of APRIORI
candidates = []
for i in range(len(symbols)): #10
    candidates += [ symbols[i] ]
sum_length = 0
finished = False
	
print("Frequent substrings:")
while not finished: 
    # check the candidates if they are frequent
    #print candidates
    for candidate in candidates:
        #print(candidate)
        support_of_candidate = 0
        for i in range(len(sequences)):
            if candidate in sequences[i]:
                support_of_candidate+=1
        if support_of_candidate >= abs_min_supp:
            curr_frequent += [ candidate ]
            #print(candidate)
            sum_length+=len(candidate)
    
    all_frequent += curr_frequent
    
    # generate candiates for the next iteration
    candidates = []
    for i in range(len(curr_frequent)):
        for j in range(len(curr_frequent)):
            #print curr_frequent
            #print curr_frequent[i][0:]
            #print curr_frequent[j][0:1+len(curr_frequent[j])-1]
            if curr_frequent[i][1:] == curr_frequent[j][0:len(curr_frequent[j])-1]:
                candidates += [ curr_frequent[i]+curr_frequent[j][len(curr_frequent[j])-1]   ]
    print candidates

    if len(candidates)==0:
        finished = True
    
    curr_frequent=[]
print ("Num. fq. substrings:"+str(len(all_frequent)))
#print ("Length of the longest fq. substring: "+str(len(all_frequent[len(all_frequent)-1])))
#print ("Avg. length of fq. substrings:"+str(sum_length/len(all_frequent)))
print ("Execution Time: %s seconds" %(time.time()-start_time))