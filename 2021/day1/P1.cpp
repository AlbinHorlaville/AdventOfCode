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

    int prev = depths[0]; // Starting at 2nd element
    for (auto current = next(depths.begin()); current != depths.end(); current++)
    {
        if (prev < *current)
            increasment++;
        prev = *current;
    }

    cout << increasment << endl;
}