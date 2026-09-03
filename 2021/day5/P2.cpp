#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iterator>
#include <unordered_map>
#include <sstream>

using namespace std;

unordered_map<string, int> getInput(const char *filename)
{
    unordered_map<string, int> result;

    ifstream input_stream(filename);
    if (!input_stream)
        cerr << "Can't open input file!";

    string line;
    while (getline(input_stream, line))
    {
        if (line.empty())
            continue; // Ignore les lignes vides

        std::stringstream ss(line);
        int x1, y1, x2, y2;
        char virgule;
        std::string arrow;

        // nombre, virgule, nombre, flèche, nombre, virgule, nombre
        if (ss >> x1 >> virgule >> y1 >> arrow >> x2 >> virgule >> y2)
        {
            int i = x1;
            int j = y1;
            while (true)
            {
                // Initialise ou incrémente la valeur de ce point
                string key(to_string(i) + ',' + to_string(j));
                result[key] += 1;

                // Incrémente i et j
                i += (i == x2) ? 0 : (i < x2) ? 1 : -1;
                j += (j == y2) ? 0 : (j < y2) ? 1 : -1;

                if (i==x2 && j==y2) // Condition de sortie de la boucle
                {
                    key = to_string(i) + ',' + to_string(j);
                    result[key] += 1;
                    break;
                }
            }
        }
    }

    return result;
}

int main()
{
    unordered_map<string, int> vent_map = getInput("2021/day5/input.txt");
    int result = 0;
    for (const auto& [key, value] : vent_map)
    {
        result += (value > 1) ? 1 : 0;
    }
    cout << result << endl;
}