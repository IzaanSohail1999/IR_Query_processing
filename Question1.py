import io
import os
import json
import string

split_string = ""
Dict = {}
freqcounter = 1
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


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
                            else:
                                counter = counter + 1

def search(term):
    lst = ['1','2','3','4','5','6','7','8','9','10,',
    '11','12','13','14','15','16','17','18','19','20',
    '21','22','23','24','25','26','27','28','29','30',
    '31','32','34','34','35','36','37','38','39','40',
    '41','42','43','44','45','46','47','48','49','50']
    
    num = 0
    dist = 0
    value = []
    ans = []
    cont1 = []
    cont2 = []
    temp = []
    nlst = []
    s = Stack()
    stack = Stack()
    wordstk = Stack()
    term = term.split(' ')
    
    for x in term:
       s.push(x)

    while not s.isEmpty():
        word = s.peek()
        s.pop()
        stack.push(word)

        

    while not stack.isEmpty():
        # print(stack.peek())
        if stack.peek() != 'and' and stack.peek() != 'or' and stack.peek() != 'not':
            slash = stack.peek() 
            if ord(slash[0]) == 47:
                diff = int(slash[1])
                # print(diff)
                cont1 = value[-1]
                value.remove(value[-1])
                cont2 = value[-1]
                value.remove(value[-1])
                nlst = set(cont1).intersection(set(cont2))
                # print(nlst)
                # print(" ")
                word1 = Dict[wordstk.pop()][0]
                # print(word1)
                # print(" ")
                word2 = Dict[wordstk.pop()][0]
                # print(word2)
                # print(" ")
                for docid in nlst:
                    # print("doc id is: ", docid)                    
                    if docid in word1:
                        poswrd1 = word1[docid]
                        # print("positions are: ", poswrd1)
                        # print(" ")
                    if docid in word2:
                        poswrd2 = word2[docid]
                        # print("positions are: ", poswrd2)
                        # print(" ")
                    # print(len(poswrd1))
                    # print(len(poswrd2))
                    for i in range(len(poswrd1)):
                        for j in range(len(poswrd2)):
                            match = poswrd1[i] - poswrd2[j]
                            # print("match: ", match)
                            if match < 0:
                                match = match * -1
                            if match == diff+1:
                                # print("Valid document id is: " , docid)
                                ans = docid
                            else:
                                continue
                # print("Valid document id is: ", ans)
                # print("intersection is: " )
                stack.pop()
            else:
                value.append(Dict[stack.peek()][0].keys())
                ans = value[-1]
                wordstk.push(stack.peek()) 
                stack.pop()
                num = num + 1
        
        else:
            if stack.peek() == 'and':
                stack.pop()
                if stack.peek() == 'not':
                    stack.pop()
                    value.append(Dict[stack.peek()][0].keys())
                    stack.pop()
                    temp = set(lst).difference(set(value[-1]))
                    value.remove(value[-1])
                    ans = set(temp).intersection(set(ans))
                
                else:
                    value.append(Dict[stack.peek()][0].keys())
                    stack.pop()
                    temp = value[-1]
                    value.remove(value[-1])
                    ans = set(ans).intersection(set(temp))

            elif  stack.peek() == 'or':
                stack.pop()
                if stack.peek() == 'not':
                    stack.pop()
                    value.append(Dict[stack.peek()][0].keys())
                    stack.pop()
                    temp = set(lst).difference(set(value[-1]))
                    value.remove(value[-1])
                    ans = set(temp).union(set(ans))
                
                else:
                    value.append(Dict[stack.peek()][0].keys())
                    stack.pop()
                    temp = value[-1]
                    value.remove(value[-1])
                    ans = set(ans).union(set(temp))
            
            elif stack.peek() == 'not':
                stack.pop()
                value.append(Dict[stack.peek()][0].keys())
                stack.pop()
                ans = set(lst).difference(set(value[-1]))
                value.remove(value[-1])

    print(ans)

def main():
    global freqcounter
    Dir = "D:\\izaan\\Work\\University\\university docs\\Semester 6\\IR\\Assignment\\Assignment 1\\ShortStories\\"
    Dir1 = "D:\\izaan\\Work\\University\\university docs\\Semester 6\\IR\\Assignment\\Assignment 1\\"
    fileread(Dir,Dir1)
    query = input()
    query = query.lower()
    search(query)
main()
