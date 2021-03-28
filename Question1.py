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
    type = 0
    value = []
    term = term.split(' ')
    for x in term:
        if x == 'and':
            print("boolean operator is : ", x)
            type = 1
        elif x == 'or':
            print("boolean operator is : ", x)
            type = 2
        elif x == 'not':
            print("boolean operator is : ", x)
            type = 3
        elif x in Dict:
            value.append(Dict[x][0].keys())
            
    
    if type == 0:
        print(Dict[term][0])
    if(type == 1):
        print(set(value[0]).intersection(set(value[1])))
        print(len(set(value[0]).intersection(set(value[1]))))
    if(type == 2):
        print(set(value[0]).union(set(value[1])))
        print(len(set(value[0]).union(set(value[1]))))
        
    # for num in range(len(value[0])):
    #     if value[0][num] == value[1][num]:
    #         print(value[0][num])

    # value[0].sort()
    # value[1].sort()
    # print(value[0])
    # print(value[1])
    # print(max(value[0]))
    # print(max(value[1]))
    # print(value[0][1])
    # print(value[1][1])
    # count = 0
    # if type1 == 1:
    # if len(value[0]) <= len(value[1]):
    #         for num in range(len(value[0])):
    #             if value[0][count] == value[1][count]:
    #                 print(value[0][count])
    #                 count = count + 1
    # elif len(value[0]) > len(value[1]):
    #         for num in range(len(value[1])):
    #             if value[1][count] == value[0][count]:
    #                 print(value[1][count])
    #                 count = count + 1
    # return Dict[term][0]

def main():
    # Dict1 = {}
    global freqcounter
    Dir = "D:\\izaan\\Work\\University\\university docs\\Semester 6\\IR\\Assignment\\Assignment 1\\ShortStories\\"
    Dir1 = "D:\\izaan\\Work\\University\\university docs\\Semester 6\\IR\\Assignment\\Assignment 1\\"
    fileread(Dir,Dir1)
    # print(json.dumps(Dict,sort_keys=True, indent=4))
    # print(Dict)
    # print(freqcounter)
    # query = input()
    query = "beard"
    search(query)
    # print(query.split(' '))
    # query = query.split(' ')
    # print(len(query))
    # for x in query:
    #     if x == "and":
    #         type = "1"
    #         continue
    #     else:
    #         print(x)
    #         search(x)
main()
