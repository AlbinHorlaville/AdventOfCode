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
    if (n == 0)
        return 1;

    // How many bits we have to inverse
    int nbBits = 0;
    unsigned int temp = n;
    while (temp > 0)
    {
        nbBits++;
        temp >>= 1;
    }

    // Mask for inverse only desired bits
    unsigned int mask = (1UL << nbBits) - 1;

    return (~n) & mask;
}

unsigned int getRating(const vector<string> &array, bool fewer_bits)
{
    vector<string> copy_array(array);

    // Loop for iterate on collums
    for (int i = 0; i < copy_array[0].length(); i++)
    {
        int sum_of_1 = 0, sum_of_0 = 0;

        // Loop for iterate on lines
        for (int j = 0; j < copy_array.size(); j++)
        {
            if (copy_array[j][i] == '1')
            {
                sum_of_1++;
            }
            else
            {
                sum_of_0++;
            }
        }

        char bit_criteria;
        if (fewer_bits)
        {
            bit_criteria = min(sum_of_0, sum_of_1) == sum_of_0 ? '0' : '1';
        }
        else
        {
            bit_criteria = max(sum_of_0, sum_of_1) == sum_of_1 ? '1' : '0';
        }

        // Erase bytes that doesn't check bit criteria
        vector<string> temp_list;
        for (auto byte : copy_array)
        {
            if (byte[i] == bit_criteria)
            {
                temp_list.push_back(byte);
            }
        }
        copy_array = temp_list;

        // Stop if there remains only one byte in the list
        if (copy_array.size() == 1)
        {
            return stoi(copy_array[0], nullptr, 2); // Conversion in base 2
        }
    }
    return 0;
}

int main()
{
    vector<string> bits = getInput("2021/day3/input.txt");

    unsigned int oxygen = 0, co2 = 0;
    oxygen = getRating(bits, false);
    co2 = getRating(bits, true);

    cout << oxygen * co2 << endl;
}
