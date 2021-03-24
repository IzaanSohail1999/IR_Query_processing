#include<iostream>
#include <fstream>
#include<string.h>
using namespace std;

int compare(string output,string stopwords)
{
    for (int i = 0; i < 26; i++)
    {
        int check = stopwords.compare(output);
        if (check != 0)
        {
            cout << output << endl;
        }
    }
}

void tokenize(string output)
{
    string stopwords[] = {"a","is" ,"the","of" ,"all","and" ,"to","can","be","as","once" ,"for","at","am","are","has","have","had","up","his","her","in","on","no","we","do"};
    for (int i = 0; i < 26; i++)
    {
        compare(output, stopwords[i]);
    }
}

void fileread()
{
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
                // cout << output;
                tokenize(output);
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