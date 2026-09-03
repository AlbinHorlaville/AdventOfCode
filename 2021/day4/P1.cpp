#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iterator>
#include <sstream>

using namespace std;

vector<int> draw_numbers;

typedef struct {
    int number;
    bool is_marked;

    void print(){
        cout << number << " ";
    }
} Box;

typedef struct {
    Box (*boxes)[5] = new Box[5][5]; // double tableau

    void print() {
        for (int i=0; i<5; i++)
        {
            for (int j=0; j<5; j++)
            {
                boxes[i][j].print();
            }
            cout << endl;
        }
        cout << endl;
    }
} Board;

vector<Board*> boards;
int winning_number = -1;

vector<string> getInput(const char *filename)
{
    vector<string> result;

    ifstream input_stream(filename);
    if (!input_stream)
        cerr << "Can't open input file!";

    // Get draw numbers
    string line;
    getline(input_stream, line);
    stringstream s1(line);
    while (getline(s1, line, ','))
    {
        draw_numbers.push_back(stoi(line));
    }

    // Get boards
    int i = 0;
    Board *board;
    while (getline(input_stream, line))
    {
        if (line == "") continue;
        if (i == 0) {
            board = new Board();
        }
        
        string row;
        stringstream s2(line);
        int j = 0; // Compteurs pour former la board
        while (getline(s2, row, ' '))
        {
            if (row == "") continue;
            
            Box box{stoi(row), false};
            board->boxes[i][j] = box;

            j++;
            if (j % 5 == 0)
            {
                j = 0;
            }
        }
        i++;
        if (i % 5 == 0)
        {
            i = 0;
            boards.push_back(board);
        }
    }

    return result;
}


/**
 * @brief Find and return the victorious board, otherwise it returns nullptr
 * 
 * @return Board* 
 */
Board* findVictoriousBoard()
{
    for (const auto draw_number : draw_numbers) // Draw Numbers loop
    {
        for (auto board : boards) // Boards loop
        {
            // Check the box inside boards
            for (int i=0; i<5; i++) // Row loop
            {
                for (int j=0; j<5; j++) // Column loop
                {
                    if (draw_number == board->boxes[i][j].number)
                    {
                        board->boxes[i][j].is_marked = true;
                    }
                }
            }

            // Check for full row or column
            for (int i=0; i<5; i++)
            {
                bool full_col = true;
                bool full_row = true;
                for (int j=0; j<5; j++) // Column loop
                {
                    // Check row
                    if (!board->boxes[i][j].is_marked)
                    {
                        full_col = false;
                    }
                    // Check col
                    if (!board->boxes[j][i].is_marked)
                    {
                        full_row = false;
                    }
                }
                if (!full_col && !full_row) continue;

                // Cas victorieux
                winning_number = draw_number;
                return board;
            }
        }
    }
    return nullptr;
}

int main()
{
    vector<string> bits = getInput("2021/day4/input.txt");
    Board* board = findVictoriousBoard();
    if (board == nullptr) {
        cout << "Error: can't find victorious board." << endl;
        return 0;
    }
    int sum = 0;
    for (int x=0; x<5; x++)
    {
        for (int y=0; y<5; y++)
        {
            if (!board->boxes[x][y].is_marked)
            {
                sum += board->boxes[x][y].number;
            }
        }
    }
    cout << sum*winning_number;
}
