#include <iostream>
#include <fstream>
#include <string>
#include <tr1/unordered_map>

using namespace std;

int main() {
    // Create a text string, which is used to output the text file
    string myText;

    // Read from the text file
    ifstream MyReadFile("input.txt");

    int score1 = 0;
    int score2 = 0;

    string slice1;
    string slice2;

    int i_middle;

    std::tr1::unordered_map<char,int> pack1;

    std::tr1::unordered_map<char,int> ruckstack1;
    std::tr1::unordered_map<char,int> ruckstackTemp;

    string alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    int group_counter = 0;

    // Use a while loop together with the getline() function to read the file line by line
    while (getline(MyReadFile, myText)){
        
        // PART 1
        i_middle = myText.length()/2;
        slice1 = myText.substr(0,i_middle);
        slice2 = myText.substr(i_middle,myText.length());

        for(char letter : slice1){
            pack1[letter] = alphabet.find(letter) + 1;
        }

        for(char letter : slice2){
            if(pack1.find(letter) != pack1.end()){
                std::cout << "Common Letter = " << letter << '\n';
                score1 += pack1[letter];
                break;
            }
        }
        // PART 2
        if (group_counter == 0){
            for(char letter : myText){
                ruckstack1[letter] = alphabet.find(letter) + 1;

            }
        }
        else{
            for(char letter : myText){
                if(ruckstack1.find(letter) != ruckstack1.end()){
                    ruckstackTemp[letter] = ruckstack1[letter];
                }
            }
            ruckstack1 = ruckstackTemp;
            ruckstackTemp.clear();
        }
        group_counter ++;

        if (group_counter == 3){
            std::cout << "ruckstack1.size() is " << ruckstack1.size() << std::endl;
            std::cout << "value is " << ruckstack1.begin()->first << std::endl;
            score2 += ruckstack1.begin()->second; // rucktack map has only one element in this case

            group_counter = 0;
            ruckstack1.clear();
        }

        pack1.clear();
    }

    
    // Close the file
    MyReadFile.close();

    std::cout << "Final Score 1 = " << score1 << std::endl;
    std::cout << "Final Score 2 = " << score2 << std::endl;
} 


