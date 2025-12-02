#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <sstream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Guard{
public:
    int x;
    int y;
    char direction; // ^ > v <

    Guard(){}
    Guard(int x, int y, char dir) : x(x), y(y), direction(dir){}

    void setPosition(int x, int y){
        this->x = x;
        this->y = y;
    }

    void turnRight(){
        switch (this->direction){
            case '^':
                this->direction = '>';
                break;
            case '>':
                this->direction = 'v';
                break;
            case 'v':
                this->direction = '<';
                break;
            case '<':
                this->direction = '^';
                break;
        }
    }

    void moveForward(){
        switch (this->direction){
            case '^':
                this->x--;
                break;
            case '>':
                this->y++;
                break;
            case 'v':
                this->x++;
                break;
            case '<':
                this->y--;
                break;
        }
    }

    bool isOut(vector<string> const& map){
        return x<0 || x>map.size() || y<0 || y>map[0].size();
    }

    bool isBlocked(vector<string> const& map){
        switch (this->direction){
            case '^':
                return map[x-1][y] == '#';
            case '>':
                return map[x][y+1] == '#';
            case 'v':
                return map[x+1][y] == '#';
            case '<':
                return map[x][y-1] == '#';
        }
    }
};

vector<string> getMap(){
    vector<string> map;
    string line;
    // Create and open a text file
    ifstream MyReadFile("/Users/albin/Documents/Polytech/AdventOfCode/2024/day6/input.txt");

    if (!MyReadFile.is_open()) {
        cerr << "Erreur : Impossible d'ouvrir le fichier ! Vérifiez le chemin ou les permissions." << endl;
        return map; // Fin du programme
    }

    while (!MyReadFile.eof()){
        getline(MyReadFile, line);
        map.push_back(line);
    }
    return map;
}

int main(){
    vector<string> map = getMap();

    Guard guard;
    for (int i=0; i<map.size(); i++){
        for (int j=0; j<map[i].size(); j++){
            if (map[i][j] != '.' && map[i][j] != '#'){
                guard = Guard(i, j, map[i][j]);
                map[i][j] = 'X';
            }
        }
    }

    int countCase = 0;

    while (!guard.isOut(map)){
        cout << "Position : " << guard.x << " " << guard.y <<  " " << map[guard.x][guard.y] << "\n";
        if (guard.isBlocked(map)){
            guard.turnRight();
        }
        guard.moveForward();
        if (map[guard.x][guard.y] != 'X' && !guard.isOut(map)){
            map[guard.x][guard.y] = 'X';
            countCase++;
        }
    }

    cout << countCase << "\n";

    for (auto line : map){
        cout << line << "\n";
    }
    cout << "\n";
}
