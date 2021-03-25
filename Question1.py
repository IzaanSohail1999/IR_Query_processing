import io
import os
import string

def fileread(txtDir):
    for txt in os.listdir(txtDir): 
        filename = txtDir + txt
        textFile = open(filename, "r+", encoding="utf-8")
        if str(txt) == "50.txt":
            print("Filename is: " + filename)
            for my_line in textFile:
                if len(my_line) > 5:
                    # my_line.lstrip()
                    split_string = my_line.split(" ")
                    # print(my_line)
                    print("    ")
                    # print(len(split_string))
                    for i in range(len(split_string)):
                        if len(split_string[i]) >= 1:
                            split_string[i] = split_string[i].lower()
                            split_string[i] = split_string[i].replace('\n','')
                            print(split_string[i])
                            for x in range(len(split_string[i])):
                                # print(ord(split_string[i][x]))
                                if ord(split_string[i][x]) < 97 or ord(split_string[i][x]) > 122:
                                    print(split_string[i][x])
                                    split_string[i] =  split_string[i].replace(split_string[i][x],'')
                                    # del split_string[i][x]
                                    print(split_string[i])


def main():
    Dir = "D:\\izaan\\Work\\University\\university docs\\Semester 6\\IR\\Assignment\\Assignment 1\\ShortStories\\"
    fileread(Dir)


main()
