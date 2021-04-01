import io
import os
import json
import string
from tkinter import *
os.system('python pos_index.py')
split_string = ""
Dict = {}
freqcounter = 1

# This class is made to process query inside a stack and take care of precedence
# The query is pushed inside a stack and turn by turn popoed and processed 
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


# This function is made to process query where query is pushed inside a stack
# The stack is then popped term by term and processed and answer stored and appended 
def search(term,Dict):
    lst = ['1','2','3','4','5','6','7','8','9','10,',
    '11','12','13','14','15','16','17','18','19','20',
    '21','22','23','24','25','26','27','28','29','30',
    '31','32','34','34','35','36','37','38','39','40',
    '41','42','43','44','45','46','47','48','49','50']
    
    num = 0
    dist = 0
    answer = []
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
        if stack.peek() != 'and' and stack.peek() != 'or' and stack.peek() != 'not':
            slash = stack.peek() 
            if ord(slash[0]) == 47:
                diff = int(slash[1])
                cont1 = value[-1]
                value.remove(value[-1])
                cont2 = value[-1]
                value.remove(value[-1])
                nlst = set(cont1).intersection(set(cont2))
                word1 = Dict[wordstk.pop()][0]
                word2 = Dict[wordstk.pop()][0]
                for docid in nlst:                    
                    if docid in word1:
                        poswrd1 = word1[docid]
                    if docid in word2:
                        poswrd2 = word2[docid]
                    for i in range(len(poswrd1)):
                        for j in range(len(poswrd2)):
                            match = poswrd1[i] - poswrd2[j]
                            if match < 0:
                                match = match * -1
                            if match <= diff+1:
                                print(diff, match, docid)
                                answer.append(docid)
                                ans = answer
                            else:
                                continue
                stack.pop()
            else:
                if stack.peek() in Dict:
                    value.append(Dict[stack.peek()][0].keys())
                    ans = value[-1]
                    wordstk.push(stack.peek()) 
                    stack.pop()
                    num = num + 1
                else:
                    stack.pop()
        
        else:
            if stack.peek() == 'and':
                stack.pop()
                if stack.peek() == 'not':
                    stack.pop()
                    if stack.peek() in Dict:
                        value.append(Dict[stack.peek()][0].keys())
                        stack.pop()
                        temp = set(lst).difference(set(value[-1]))
                        value.remove(value[-1])
                        ans = set(temp).intersection(set(ans))
                
                else:
                    if stack.peek() in Dict:
                        value.append(Dict[stack.peek()][0].keys())
                        stack.pop()
                        temp = value[-1]
                        value.remove(value[-1])
                        ans = set(ans).intersection(set(temp))

            elif  stack.peek() == 'or':
                stack.pop()
                if stack.peek() == 'not':
                    stack.pop()
                    if stack.peek() in Dict:
                        value.append(Dict[stack.peek()][0].keys())
                        stack.pop()
                        temp = set(lst).difference(set(value[-1]))
                        value.remove(value[-1])
                        ans = set(temp).union(set(ans))
                
                else:
                    if stack.peek() in Dict:
                        value.append(Dict[stack.peek()][0].keys())
                        stack.pop()
                        temp = value[-1]
                        value.remove(value[-1])
                        ans = set(ans).union(set(temp))
            
            elif stack.peek() == 'not':
                stack.pop()
                if stack.peek() in Dict:
                    value.append(Dict[stack.peek()][0].keys())
                    stack.pop()
                    ans = set(lst).difference(set(value[-1]))
                    value.remove(value[-1])
    return ans

# This is thr main function which gives directories of all stories present and the stopword list
# Here using tkinter a GUI is made where query is taken stored
# sent to concerned functions and answered displayed in answer box 
def main():
    with open('Dictionary.json') as json_file:
      Dict = json.load(json_file)
      
    root = Tk()
    root.title('Query Search Box')
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)

    Labeltext = StringVar()
    Label(bottomframe, textvariable=Labeltext).pack(side=LEFT)
    # This function is triggered on button press to process query and display answer
    def click():
        s = entry.get()
        s= s.lower()
        answer = search(s,Dict)
        if len(answer) == 0:
            Labeltext.set("no result found")
        else:    
            Labeltext.set(str(answer))
    
    topframe = Frame(root)
    Label(topframe, text='Text to find:').pack(side=LEFT)
    entry = Entry(topframe)
    entry.pack()
    button = Button(topframe, text="search", command = click)
    button.pack()
    topframe.pack(side = TOP)
    root.mainloop()

    
main()
