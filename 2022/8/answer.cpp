#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;


void printGrid(vector<vector<int>> grid){
    for(int i=0; i< grid.size();i++){
        for(int j=0; j< grid[i].size();j++){
            std::cout << grid[i][j] ;
        }
        std::cout << endl;
    }
}

bool checkIsMax(vector<int> direction, int tree){
    sort(direction.begin(),direction.end(), greater<int>());
    if( tree > direction[0])
        return true;
    else
        return false;
}

int part1(vector<vector<int>> grid){
    int score1 = grid.size()*2 + grid[0].size()*2 - 4;
    
    vector<int> bufferVisible;
    int current;

    for (int i = 1; i < grid.size() - 1; i++){
        for (int j = 1; j < grid[0].size() - 1; j++){
            current = grid[i][j];
            cout << "i: " << i << " j: " << j << " value: " << current <<endl;
            
            //UP
            bufferVisible.clear();
            for (int k = 0; k < i; k++)
                bufferVisible.push_back(grid[k][j]);
            if(checkIsMax(bufferVisible,current)){
                cout << "IS MAX UP" <<endl;
                score1++;
                continue;
            }
            

            //DOWN
            bufferVisible.clear();
            for (int k = i + 1; k < grid.size(); k++)
                bufferVisible.push_back(grid[k][j]);
            if(checkIsMax(bufferVisible,current)){
                cout << "IS MAX DOWN" <<endl;
                score1++;
                continue;
            }

            //LEFT
            bufferVisible.clear();
            for (int l = 0; l < j; l++)
                bufferVisible.push_back(grid[i][l]);
            if(checkIsMax(bufferVisible,current)){
                cout << "IS MAX LEFT" <<endl;
                score1++;
                continue;
            }

            //RIGHT
            bufferVisible.clear();
            for (int l = j+1 ; l < grid[0].size(); l++)
                bufferVisible.push_back(grid[i][l]);
            if(checkIsMax(bufferVisible,current)){
                cout << "IS MAX RIGHT" <<endl;
                score1++;
                continue;
            }

            
        }
    }

    return score1;
}

int part2(vector<vector<int>> grid){
    int max_scenic = 1;
    int current;
    int current_scenic;
    int direction_buffer;

    int k,l;

    for (int i = 0; i < grid.size() ; i++){
        for (int j = 0; j < grid[0].size() ; j++){
            current = grid[i][j];
            current_scenic = 1;

            //UP
            direction_buffer = 1;
            for (k = i - 1; k > 0 && current > grid[k][j]; k--){
                direction_buffer++;
            }
            cout << "UP : " << direction_buffer << endl;
            current_scenic*= direction_buffer;

            
            //DOWN
            direction_buffer = 1;
            for (k = i + 1; k < grid.size() - 1 && current > grid[k][j]; k++){
                direction_buffer++;
            }
            cout << "DOWN : " << direction_buffer << endl;
            current_scenic*= direction_buffer;

            //LEFT
            direction_buffer = 1;
            for (l = j - 1; l > 0 && current > grid[i][l]; l--){
                direction_buffer++;
            }
            cout << "LEFT : " << direction_buffer << endl;
            current_scenic*= direction_buffer;

            
            //RIGHT
            direction_buffer = 1;
            for (l = j + 1; l < grid.size() - 1 && current > grid[i][l]; l++){
                direction_buffer++;
            }
            cout << "RIGHT : " << direction_buffer << endl;
            current_scenic*= direction_buffer;

            if (i == 0 || j == 0 || i == grid.size() - 1 || j == grid[0].size() - 1)
                current_scenic = 0;

            cout << "i: " << i << " j: " << j << " value: " << current << " scenic: " << current_scenic <<endl;
            
            if(current_scenic > max_scenic)
                max_scenic = current_scenic;
        }
    }

    return max_scenic;
}

int main() {
    // Create a text string, which is used to output the text file
    string myText;

    // Read from the text file
    ifstream MyReadFile("input.txt");

    vector<vector<int>> grid;
    int i = 0;
    // COPY
    while (getline(MyReadFile, myText)){
        grid.push_back(vector<int>());
        for(int j=0; j< myText.size() ; j++){
            grid[i].push_back(myText[j] - '0');
        }
        i++;
    }

    printGrid(grid);


    
    


    // Close the file
    MyReadFile.close();

    int score1 = part1(grid);
    std::cout << "/*/*/*/*/*/*/*/*//*/*/*/*/*//*" << '\n';
    int score2 = part2(grid);

    std::cout << "Final Score 1 = " << score1 << '\n';
    std::cout << "Final Score 2 = " << score2 << '\n';
} 


