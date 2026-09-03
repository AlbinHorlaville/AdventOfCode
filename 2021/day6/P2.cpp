#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iterator>
#include <unordered_map>
#include <cmath>

using namespace std;

unordered_map<int, long long int> getInput(const char *filename)
{
    unordered_map<int, long long int> result;

    ifstream input_stream(filename);
    if (!input_stream)
        cerr << "Can't open input file!";

    string line;
    while (getline(input_stream, line, ','))
    {
        int internal_timer = stoi(line);
        result[internal_timer] += 1;
    }

    return result;
}

int main()
{
    unordered_map<int, long long int> lanternfishs = getInput("2021/day6/input.txt");

    for (int day=0; day < 256; day++)
    {
        long long int new_lanternfishs = lanternfishs[0]; // Sauvegarde du nombre de lanternfish qui s'apprètent à accoucher
        // Update de tous les internal timer des lanternfish
        for (int internal_timer=0; internal_timer<8; internal_timer++)
        {
            lanternfishs[internal_timer] = lanternfishs[internal_timer+1];
        }
        // Naissance des nouveaux lanternfishs + reset des mamans
        lanternfishs[8] = new_lanternfishs;
        lanternfishs[6] += new_lanternfishs;
    }

    // Calcul de la somme de tous les lanternfishs au bout de 80 jours
    long long int sum = 0;
    for (int i=0; i<9; i++)
    {
        sum += lanternfishs[i];
    }
    cout << sum << endl;
}