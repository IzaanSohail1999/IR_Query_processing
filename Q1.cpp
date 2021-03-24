#include<iostream>
#include <fstream>
#include<string.h>
#include <bits/stdc++.h>
using namespace std;

int compare(string output,string stopwords)
{
        int check = stopwords.compare(output);
        if (check == 0)
        {
            cout << output << endl;
        }
}

void tokenize(string output, string stopwords[], int size)
{
    vector<string> tokens;
    string line = "GeeksForGeeks is a must try";
    stringstream check1(line);
    string intermediate;
    while (getline(check1, intermediate, ' '))
    {
        tokens.push_back(intermediate);
    }

    // Printing the token vector
    for (int i = 0; i < tokens.size(); i++)
        cout << tokens[i] << endl;
}
    // for (int i = 0; i < 26; i++)
    // {
    //     compare(output, stopwords[i]);
    // }
// }

void fileread()
{
    string stopwords[33];
    ifstream myReadFile1;
    string dirname = "Stopword-List.txt";
    myReadFile1.open(dirname);
    string output;
    int i = 0;
    if (myReadFile1.is_open())
    {
        while (!myReadFile1.eof() && i <= 26)
        {
            myReadFile1 >> output;
            stopwords[i] = output;
            i++;
        }
    }
    for(int j = 0; j < 26;j++)
    {
        //cout << stopwords[j] << endl;
    }

    myReadFile1.close();
    cout << endl;

    ifstream myReadFile;
    string filename;
    for (int i = 50; i <= 50; i++)
    {
        string dirname = "ShortStories\\";
        if (i > 9)
        {
            string tmp = to_string(i);
            char const *num_char = tmp.c_str();
            filename = num_char;
        }
        else if (i <= 9)
        {
            int num = i + 48;
            filename = char(num);
        }
        string ext = ".txt";
        string directory = dirname + filename + ext;
        myReadFile.open(directory);
        string output;
        if (myReadFile.is_open())
        {
            while (!myReadFile.eof())
            {
                myReadFile >> output;
                cout << output;
                //tokenize(output,stopwords,26);
            }
        }
        myReadFile.close();
        cout << endl;
    }
}

int main()
{
    fileread();
    return 0;    
}