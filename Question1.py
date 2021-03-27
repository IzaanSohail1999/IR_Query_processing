import io
import os
import json
import string

split_string = ""
Dict = {}
freqcounter = 1

def clean(split_string):
    for x in range(len(split_string)):
        if ord(split_string[x]) < 97 or ord(split_string[x]) > 122:
            split_string =  split_string.replace(split_string[x],' ')
    return split_string

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

def fileread(txtDir,Dir1):
    stopword = []
    stopfile = "Stopword-List.txt"
    stopfile = Dir1 + stopfile;
    stopFile1 = open(stopfile, "r+", encoding="utf-8")
    for line in stopFile1:
        if(len(line) >= 2):
            word = line
            word = clean(word)
            word = word.replace(' ', '')
            stopword.append(word)
    
    # print(stopword)
    # print(len(stopword))
    
    for txt in os.listdir(txtDir):
        filenum = txt.split('.')[0] 
        filename = txtDir + txt
        textFile = open(filename, "r+", encoding="utf-8")
        # if str(txt) == "50.txt":
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
                                    # print(split_string[i],x) 
                                    check = True
                                    break
                                else:
                                    continue

                            if check == False:
                                formindex(filenum, counter, split_string[i])
                                counter = counter + 1

def search(term):
    if term in Dict:
        return Dict[term][0]

def main():
    Dict1 = {}
    global freqcounter
    Dir = "D:\\izaan\\Work\\University\\university docs\\Semester 6\\IR\\Assignment\\Assignment 1\\ShortStories\\"
    Dir1 = "D:\\izaan\\Work\\University\\university docs\\Semester 6\\IR\\Assignment\\Assignment 1\\"
    fileread(Dir,Dir1)
    # print(json.dumps(Dict,sort_keys=True, indent=4))
    # print(Dict)
    # print(freqcounter)
    # query = input()
    query = "old man"
    # print(query.split(' '))
    query = query.split(' ')
    # print(len(query))
    for x in query:
        if x == "and":
            type = "1"
            continue
        else:
            print(x)
            Dict1 = search(x)
main()
