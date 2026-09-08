#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <cmath>

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
    vector<int> crabs = getInput("2021/day7/input.txt");
    sort(crabs.begin(), crabs.end()); // Tri croissant

    // Calcul moyennes
    int somme = 0;
    for (auto crab : crabs) {
        somme += crab;
    }
    int moyenne_basse = ceil(somme / static_cast<double>(crabs.size()));
    int moyenne_haute = floor(somme / static_cast<double>(crabs.size()));

    // Somme de la quantité de fuel utilisée
    int fuel_moy_basse = 0;
    int fuel_moy_haute = 0;
    for (auto crab: crabs)
    {
        int n1 = abs(moyenne_basse - crab);
        int n2 = abs(moyenne_haute - crab);
        fuel_moy_basse += n1 * (n1 + 1) / 2;
        fuel_moy_haute += n2 * (n2 + 1) / 2;
    }

    if (fuel_moy_basse < fuel_moy_haute)
    {
        cout << fuel_moy_basse << endl;
    }
    else
    {
        cout << fuel_moy_haute << endl;
    }
}