#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iterator>
#include <unordered_map>
#include <sstream>
#include <ranges>
#include <string_view>

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
            // Ajouter/incrémenter chaque point de segment au dictionnaire
            if (x1 != x2 && y1 != y2) continue; // Passer à la ligne suivante si le segment n'est ni une ligne ni une colonne

            // On part du principe que x1, y1 <= x2, y2
            int min_x = min(x1, x2);
            int max_x = max(x1, x2);
            int min_y = min(y1, y2);
            int max_y = max(y1, y2);
            for (int i = min_x; i <= max_x; i++)
            {
                for (int j = min_y; j <= max_y; j++)
                {
                    string key(to_string(i) + ',' + to_string(j));
                    result[key] += 1; // Initialise ou incrémente la valeur de ce point
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
    for (int i=0; i<10; i++)
    {
        for (int j=0; j<10; j++)
        {
            string key = to_string(j) + ',' + to_string(i);
            cout << ((vent_map.contains(key)) ? to_string(vent_map[key]) : ".");
        }
        cout << endl;
    }
    cout << result << endl;
}