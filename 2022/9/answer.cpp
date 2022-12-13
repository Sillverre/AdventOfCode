#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define GRIDSIZE 1000


void printGrid(char grid[GRIDSIZE][GRIDSIZE]){
    for (int i = 0; i < GRIDSIZE; i++){
        for (int j = 0; j < GRIDSIZE; j++){
            cout << grid[i][j];
        }
        cout << endl;
    }

}

void avanceKnot(int nbKnots, int knots[9][2],char grid[GRIDSIZE][GRIDSIZE]){
    for (int i= 0; i < nbKnots; i++){
        // Move Tail
        if (knots[i][0] - knots[i+1][0] > 1){
            knots[i+1][0] ++;
            if (knots[i+1][1] < knots[i][1])
                knots[i+1][1] ++;
            if (knots[i+1][1] > knots[i][1])
                knots[i+1][1] --;
        }
        else if (knots[i+1][0] - knots[i][0] > 1){
            knots[i+1][0] --;
            if (knots[i+1][1] < knots[i][1])
                knots[i+1][1] ++;
            if (knots[i+1][1] > knots[i][1])
                knots[i+1][1] --;
        }
        else if (knots[i+1][1] - knots[i][1] > 1){
            knots[i+1][1] --;
            if (knots[i+1][0] < knots[i][0])
                knots[i+1][0] ++;
            if (knots[i+1][0] > knots[i][0])
                knots[i+1][0] --;
        }
        else if (knots[i][1] - knots[i+1][1] > 1){
            knots[i+1][1] ++;
            if (knots[i+1][0] < knots[i][0])
                knots[i+1][0] ++;
            if (knots[i+1][0] > knots[i][0])
                knots[i+1][0] --;
        }
    }
}

int main() {
    // Create a text string, which is used to output the text file
    string myText;

    // Read from the text file
    ifstream MyReadFile("input.txt");

    int score1= 0;
    int score2;
    int final_knot = 9;


    char grid[GRIDSIZE][GRIDSIZE];
    std::fill_n(&grid[0][0], GRIDSIZE * GRIDSIZE, '.');

    int knots[10][2];
    std::fill_n(&knots[0][0], 10 * 2, GRIDSIZE/2);


    char direction;
    int step;

    // Use a while loop together with the getline() function to read the file line by line
    while (getline(MyReadFile, myText)){
        direction = myText[0];
        step = stoi(myText.substr(2));
        
        for(int i = 0; i < step; i++){
            // Move Head
            switch(direction){
                case 'U':
                    knots[0][0] --;
                    break;
                case 'D':
                    knots[0][0] ++;
                    break;
                case 'R':
                    knots[0][1] ++;
                    break;
                case 'L':
                    knots[0][1] --;
                    break;
            }
            avanceKnot(final_knot, knots, grid);

            //Mark tail trace
            if (grid[knots[final_knot][0]][knots[final_knot][1]] == '.'){
                grid[knots[final_knot][0]][knots[final_knot][1]] = '#';
                score1++;
            }

            //printGrid(grid);
            std::cout << "line Head = " << knots[0][0] << " ; col Head = " << knots[0][1] << endl;
            std::cout << "line Tail = " << knots[final_knot][0] << " ; col Tail = " << knots[final_knot][1] << endl;
            cout << "--------------------------------------------" <<endl;
        }


    }
    
    // Close the file
    MyReadFile.close();

    std::cout << "Final Score 1 = " << score1 << endl;
    std::cout << "Final Score 2 = " << score2 << endl;
} 


