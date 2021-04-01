import io
import os
import json
import string

split_string = ""
Dict = {}
freqcounter = 1

# This function is made to form dictionary where each term arrives
# The term is processed if it is already present in dictionary
# If yes then the document id and positions are appended to the already present term
# If no then the term is added to dictionary along with document id and positions 
def formindex(filenum, counter, term):
    global freqcounter
    if term in Dict:
        if filenum not in Dict[term][0]:
            Dict[term][0][filenum] = []
        Dict[term][0][filenum].append(counter)
    else:
        Dict[term] = []
        Dict[term].append({})
        Dict[term][0][filenum] = [counter]
        freqcounter += 1

# This function is made to clean every coming term and return its base form
def clean(split_string):
    for x in range(len(split_string)):
        if ord(split_string[x]) < 97 or ord(split_string[x]) > 122:
            split_string =  split_string.replace(split_string[x],' ')
    return split_string

# This function is made to read file and one by one extract words and send them to first clean function
# Then to the form index function 
def fileread(txtDir):
    stopword = []
    stopfile = "Stopword-List.txt"
    stopFile1 = open(stopfile, "r+", encoding="utf-8")
    for line in stopFile1:
        if(len(line) >= 2):
            word = line
            word = clean(word)
            word = word.replace(' ', '')
            stopword.append(word)
    
    for txt in os.listdir(txtDir):
        filenum = txt.split('.')[0] 
        filename = txtDir + txt
        textFile = open(filename, "r+", encoding="utf-8")
        counter = 1
        for my_line in textFile:
                if len(my_line) > 5:
                    split_string = my_line.split(" ")
                    for i in range(len(split_string)):
                        if len(split_string[i]) >= 1:
                            split_string[i] = split_string[i].lower()
                            split_string[i] = split_string[i].replace('\n','')
                            split_string[i] = clean(split_string[i])
                            split_string[i] = split_string[i].replace(' ','')
                            check = False
                            for x in stopword:
                                if split_string[i] == x:
                                    check = True
                                    break
                                else:
                                    continue

                            if check == False:
                                formindex(filenum, counter, split_string[i])
                                counter = counter + 1
                            else:
                                counter = counter + 1

# This is thr m ain function which gives directories of all stories present and the stopword list
# Here using tkinter a GUI is made where query is taken stored
# sent to concerned functions and answered displayed in answer box 
def main():
    global freqcounter
    Dir = "./ShortStories\\"
    fileread(Dir)
    with open ("Dictionary.json" , "w") as f:                                                               
        f.write(json.dumps(Dict, sort_keys=False, indent=4))   #Writing the index to JSON File.
main()
