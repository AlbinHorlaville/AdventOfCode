#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iterator>

using namespace std;

vector<int> getInput(const char *filename)
{
    vector<int> result;

    ifstream input_stream(filename);
    if (!input_stream)
        cerr << "Can't open input file!";

    string line;
    while (getline(input_stream, line))
    {
        result.push_back(stoi(line));
    }

    return result;
}

int main()
{
    vector<int> depths = getInput("2021/day1/input.txt");
    
    int increasment = 0;

    int prev = depths[0] + depths[1] + depths[2]; // Starting at 2nd sliding window
    for (int i=1; i<depths.size()-2; i++)
    {
        int sliding_window = depths[i] + depths[i+1] + depths[i+2];
        
        if (prev < sliding_window)
            increasment++;

        prev = sliding_window;
    }

    cout << increasment << endl;
}