#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <map>

using namespace std;

#define ADDCYCLES 2
#define NOOPCYCLES 1

void printGrid(char grid[6][40]){
    for (int i = 0; i < 6; i++){
        for (int j = 0; j < 40; j++){
            cout << grid[i][j];
        }
        cout << endl;
    }
}


int main() {
    // Create a text string, which is used to output the text file
    string myText;

    // Read from the text file
    ifstream MyReadFile("input.txt");

    int score1=0;
    int score2=0;

    int X = 1;
    int next_op;
    vector<int> s_strenghts;
    char grid[6][40];
    std::fill_n(&grid[0][0], 6 * 40, '*');
    int line = 0;
    
    int nb_cycles = 1;

    // Use a while loop together with the getline() function to read the file line by line
    while (getline(MyReadFile, myText)){
        if(myText.substr(0,4) == "noop"){
            cout << "noop ";

            //CYCLE
            if (nb_cycles % 40 == 20)
                    s_strenghts.push_back(nb_cycles * X);
            else if ((nb_cycles % 40 == 0))
                line++;
            if ((nb_cycles)%40 >= X && (nb_cycles)%40 <= X+2)
                grid[line][(nb_cycles-1)%40] = '#';
            else
                grid[line][(nb_cycles-1)%40] = '.';
            nb_cycles++;

        }
        else if (myText.substr(0,4) == "addx"){
            next_op = stoi(myText.substr(5,string::npos));
            cout << "addx "<< next_op << " ";
            for(int i= 0; i< ADDCYCLES; i++){
                
                //CYCLE
                if (nb_cycles % 40 == 20)
                    s_strenghts.push_back(nb_cycles * X);
                else if ((nb_cycles % 40 == 0))
                    line++;
                if ((nb_cycles)%40 >= X && (nb_cycles)%40 <= X+2)
                    grid[line][(nb_cycles-1)%40] = '#';
                else
                    grid[line][(nb_cycles-1)%40] = '.';
                nb_cycles++;

            }
            X += next_op;
        }
        else{
            cerr << "WHAT THE FUCK INSTRUCTION UNKNOWN !!" << endl;
            return -1;
        }
        cout << "X= " << X << " cycle = " << nb_cycles << endl;
    }

    cout << "------------READING OVER------------" << endl;
    for(std::vector<int>::iterator it = s_strenghts.begin(); it != s_strenghts.end(); ++it){
        score1 += *it;
        cout << "element: " << *it << endl;
     }

    // Close the file
    MyReadFile.close();

    std::cout << "Final Score 1 = " << score1 << endl;
    printGrid(grid);

} 


