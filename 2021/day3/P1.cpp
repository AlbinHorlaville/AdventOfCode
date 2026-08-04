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

unsigned int inverseBits(unsigned int n)
{
    if (n==0) return 1;

    // How many bits we have to inverse
    int nbBits = 0;
    unsigned int temp = n;
    while (temp > 0){
        nbBits++;
        temp >>= 1;
    }

    // Mask for inverse only desired bits
    unsigned int mask = (1UL << nbBits) - 1;

    return (~n) & mask;
}

int main()
{
    vector<string> bits = getInput("2021/day3/input.txt");

    unsigned int gamma = 0, epsilon = 0; // Epsilon is the negative of gamma

    // Loop for iterate on collums
    for (int i = 0; i < bits[0].length(); i++)
    {
        int sum_of_1 = 0, sum_of_0 = 0;

        // Loop for iterate on lines
        for (int j = 0; j < bits.size(); j++)
        {
            if (bits[j][i] == '1')
            {
                sum_of_1++;
            }
            else
            {
                sum_of_0++;
            }
        }

        // update epsilon and gamma
        int value = max(sum_of_0, sum_of_1) == sum_of_0 ? 0 : 1;
        gamma = (gamma << 1) + value;
    }
    epsilon = inverseBits(gamma);

    cout << gamma * epsilon << endl;
}
