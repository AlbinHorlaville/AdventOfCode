#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <sstream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

struct position{
    int x;
    int y;
    char direction; // ^ > v <

    position(int x, int y, char d) : x(x), y(y), direction(d){}
};

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

    void goToposition(position const& point){
        this->x = point.x;
        this->y = point.y;
        this->direction = point.direction;
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

    bool hasPosition(position const& pos){
        return x == pos.x && y == pos.y && direction == pos.direction;
    }

    vector<int> getForwardPosition(){
        vector<int> caseForward;
        caseForward.push_back(x);
        caseForward.push_back(y);
        switch (this->direction){
            case '^':
                caseForward[0]--;
                break;
            case '>':
                caseForward[1]++;
                break;
            case 'v':
                caseForward[0]++;
                break;
            case '<':
                caseForward[1]--;
                break;
        }
        return caseForward;
    }

    bool isOut(vector<string> const& map){
        return x<0 || x>map.size() || y<0 || y>map[0].size();
    }

    bool forwardIsOut(vector<string> const& map){
        vector<int> pos = getForwardPosition();
        return pos[0]<0 || pos[0]>map.size() || pos[1]<0 || pos[1]>map[0].size();
    }

    bool isBlocked(vector<string> const& map){
        switch (this->direction){
            case '^':
                return map[x-1][y] == '#' || map[x-1][y] == 'O';
            case '>':
                return map[x][y+1] == '#' || map[x][y+1] == 'O';
            case 'v':
                return map[x+1][y] == '#' || map[x+1][y] == 'O';
            case '<':
                return map[x][y-1] == '#' || map[x][y-1] == 'O';
        }
    }

    bool boucle(vector<position> const& chemin){
        for (position pos : chemin){
            if (pos.x == x && pos.y == y && pos.direction == direction){
                return true;
            }
        }
        return false;
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

void bloquerCase(vector<string> *map, Guard guard){
    vector<int> caseForward = guard.getForwardPosition();
    (*map)[caseForward[0]][caseForward[1]] = 'O';
}

void débloquerCase(vector<string> *map, Guard guard){
    vector<int> caseForward = guard.getForwardPosition();
    (*map)[caseForward[0]][caseForward[1]] = '.';
}

void afficher(vector<string> const& map){
    for (auto line : map){
        cout << line << "\n";
    }
    cout << "\n";
}

int testBoucleInfinie(vector<string> *map, Guard *guard){
    vector<position> chemin; // Cases que le guard traverse
    position checkpoint(guard->x, guard->y, guard->direction);
    while(true){
        position pos(guard->x, guard->y, guard->direction);
        chemin.push_back(pos);
        if (guard->isBlocked(*map)){
            guard->turnRight();
        }
        else{
            guard->moveForward();
        }
        if (guard->boucle(chemin)){
            guard->goToposition(checkpoint);
            return 1;
        }

        if (guard->isOut(*map)){
            guard->goToposition(checkpoint);
            return 0;
        }
    }
}

int main(){
    vector<string> map = getMap();

    Guard guard;
    for (int i=0; i<map.size(); i++){
        for (int j=0; j<map[i].size(); j++){
            if (map[i][j] != '.' && map[i][j] != '#'){
                guard = Guard(i, j, map[i][j]);
            }
        }
    }

    int countCaseBloquable = 0;
    while (!guard.isOut(map)){
        if (guard.isBlocked(map)){
            guard.turnRight();
        }
        else{
            guard.moveForward();
        }
        if (!guard.forwardIsOut(map)){
            bloquerCase(&map, guard);
            countCaseBloquable += testBoucleInfinie(&map, &guard);
            débloquerCase(&map, guard);
        }
        
        cout << countCaseBloquable << "\n";
    }

    afficher(map);

    cout << countCaseBloquable << "\n";
}

// Il faut moins que 1365