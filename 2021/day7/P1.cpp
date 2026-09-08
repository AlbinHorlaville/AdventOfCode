#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>

using namespace std;

vector<int> getInput(const char *filename)
{
    vector<int> result;

    ifstream input_stream(filename);
    if (!input_stream)
        cerr << "Can't open input file!";

    string line;
    while (getline(input_stream, line, ','))
    {
        result.push_back(stoi(line));
    }

    return result;
}

int main()
{
    vector<int> positions = getInput("2021/day7/input.txt");
    sort(positions.begin(), positions.end()); // Tri croissant

    // Calcul médiane
    int médiane;
    int n = positions.size();
    médiane = (n%2==0) ? (positions[n/2] + positions[(n+1)/2]) / 2 : positions[(n+1)/2];

    // Somme de la quantité de fuel utilisée
    int fuel = 0;
    for (auto position: positions)
    {
        fuel += abs(médiane - position);
    }

    cout << fuel << endl;
}