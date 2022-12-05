#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;


int main() {
    // Create a text string, which is used to output the text file
    string myText;

    // Read from the text file
    ifstream MyReadFile("input.txt");

    int score1;
    int score2;

    // Use a while loop together with the getline() function to read the file line by line
    while (getline(MyReadFile, myText)){
        
    }
    
    // Close the file
    MyReadFile.close();

    std::cout << "Final Score 1 = " << score1 << '\n';
    std::cout << "Final Score 2 = " << score2 << '\n';
} 


