#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {
    // Create a text string, which is used to output the text file
    string myText;

    // Read from the text file
    ifstream MyReadFile("input.txt");

    int score1 = 0;
    int score2 = 0;

    int opponentMove;
    int myMove;

    // Use a while loop together with the getline() function to read the file line by line
    while (getline(MyReadFile, myText)){
        opponentMove = myText[0] - 'A';
        myMove = myText[2] - 'X';
        std::cout << opponentMove << " opponent/me " << myMove << '\n';

        score1 += (myMove - opponentMove + 1 +3) % 3 * 3 + (myMove + 1);
        score2 += (myMove * 3) + (opponentMove + myMove - 1 + 3) % 3 +1;
    }
/*
    1 0 0
    0 2 0
    2 1 0
    0 0 1
    1 1 1
    2 2 1
    0 1 2
    1 2 2
    2 0 2
*/
    
    // Close the file
    MyReadFile.close();

    std::cout << "Final Score 1 = " << score1 << '\n';
    std::cout << "Final Score 2 = " << score2 << '\n';
} 


