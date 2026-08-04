#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iterator>
#include <sstream>

using namespace std;

vector<string> getInput(const char *filename)
{
    vector<string> result;

    ifstream input_stream(filename);
    if (!input_stream)
        cerr << "Can't open input file!";

    string line;
    while (getline(input_stream, line))
    {
        result.push_back(line);
    }

    return result;
}

int main()
{
    vector<string> commands = getInput("2021/day2/input.txt");

    int forward = 0, depth = 0;
    string direction;
    string value;

    for (auto command : commands)
    {
        stringstream ss(command);
        getline(ss, direction, ' ');
        getline(ss, value, ' ');
        
        // Update the forward and depth values based on the direction of the submarine
        if (direction == "forward")
        {
            forward += stoi(value);
        }else if (direction == "down")
        {
            depth += stoi(value);
        }else if (direction == "up")
        {
            depth -= stoi(value);
        }else
        {
            cerr << "Error: wrong direction" << endl;
        }
    }

    cout << forward * depth << endl;
}