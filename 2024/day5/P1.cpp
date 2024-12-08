#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <sstream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

struct Sommet{
    int value;
    vector<Sommet*> prochains;

    Sommet(int value){
        this->value = value;
    }

    bool isProchain(int n){
        for (Sommet* sommet : prochains){
            if (sommet->value == n){
                return true;
            }
        }
        return false;
    }
};

vector<int> split(string const& s, char const& del){
    istringstream ss(s); // Utilisation d'istringstream pour lire une chaîne
    string word;
    vector<int> listSplited;

    while (getline(ss, word, del)) {
        try {
            listSplited.push_back(stoi(word)); // Convertir chaque partie en entier
        } catch (const invalid_argument& e) {
            cerr << "Erreur : '" << word << "' n'est pas un entier valide." << endl;
        }
    }

    return listSplited;
}

Sommet* findSommet(vector<Sommet*> *graphe, int value, unordered_set<int>& visited) {
    for (Sommet* sommet : *graphe) {
        // Vérifie si ce nœud a déjà été visité
        if (visited.find(sommet->value) != visited.end()) {
            continue;
        }

        // Marque ce nœud comme visité
        visited.insert(sommet->value);

        // Vérifie si c'est le nœud recherché
        if (sommet->value == value) {
            return sommet;
        }

        if (!sommet->prochains.empty()){
            // Explore les prochains nœuds
            Sommet* found = findSommet(&sommet->prochains, value, visited);
            if (found != nullptr) {
                return found;
            }
        }
    }
    return nullptr; // Nœud non trouvé
}

void addToTheGraph(vector<Sommet*> *graphe, vector<int> prev_next){
    unordered_set<int> visited_start;
    unordered_set<int> visited_end;
    Sommet* start = findSommet(graphe, prev_next[0], visited_start);
    Sommet* end = findSommet(graphe, prev_next[1], visited_end);

    if (start == nullptr){
        start = new Sommet(prev_next[0]);
        graphe->push_back(start);
    }

    if (end == nullptr){
        end = new Sommet(prev_next[1]);
    }
    
    start->prochains.push_back(end);

    if (graphe->size() == 1){
        return;
    }

    bool endIsRacine = false;
    for (Sommet* sommet : *graphe){ // Si end se trouve à la racine on l'enlève
        if (sommet == end){
            endIsRacine = true;
        }
    }
    if (endIsRacine){
        graphe->erase(find(graphe->begin(), graphe->end(), end));
    }
}

void afficher(Sommet* graphe, unordered_set<int>* visited, int level = 0) {
    // Vérifier si le sommet a déjà été visité
    if (visited->find(graphe->value) != visited->end()) {
        return; // Éviter les cycles
    }
    visited->insert(graphe->value);
    for (int i = 0; i < level; i++) {
        cout << "  ";
    }
    cout << graphe->value << "\n";

    for (Sommet* prochain : graphe->prochains) {
        afficher(prochain, visited, level + 1);
    }
}

bool isValid(vector<Sommet*> *graphe, vector<int> sequence){
    unordered_set<int> visited;
    Sommet* sommet = findSommet(graphe, sequence[0], visited);
    for (int i=0; i<sequence.size(); i++){
        if (i == sequence.size() - 1){
            return true;
        }

        if (sommet->prochains.empty()){
            return false;
        }

        // Tester que les nombres suivants dans la séquence sont fils de ce noeud
        for (int j = i+1; j<sequence.size(); j++){
            if (!sommet->isProchain(sequence[j])){
                return false;
            }
        }

        // Passer au prochain sommet
        bool find = false;
        for (Sommet* child : sommet->prochains){
            if (child->value == sequence[i+1]){
                sommet = child;
                find = true;
                break;
            }
        }
        if (!find){
            return false;
        }
    }
    return true;
}

int main() {
    string line;
    int result;
    // Create and open a text file
    ifstream MyReadFile("/Users/albin/Documents/Polytech/AdventOfCode/2024/day5/input.txt");

    if (!MyReadFile.is_open()) {
    cerr << "Erreur : Impossible d'ouvrir le fichier ! Vérifiez le chemin ou les permissions." << endl;
    return 1; // Fin du programme
    }

    // Construire le graphe
    vector<Sommet*> graphe;
    int i = 0;
    while(true){
        i++;
        getline(MyReadFile, line);
        vector<int> prev_next = split(line, '|');

        if (prev_next.empty()){
            break;
        }

        addToTheGraph(&graphe, prev_next);
    }
    for (Sommet* sommet : graphe){
        unordered_set<int> visited;
        afficher(sommet, &visited);
    }

    while(!MyReadFile.eof()){
        getline(MyReadFile, line);
        vector<int> sequence = split(line, ',');
        if (isValid(&graphe, sequence)){            
            result += sequence[sequence.size() / 2];
        }
    }

    cout << result << "\n";

    // Close the file
    MyReadFile.close();
}