#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

#define MAX_SIZE 100000
#define DISK_SPACE 70000000
#define UNUSED 30000000

using namespace std;


int main() {
    // Create a text string, which is used to output the text file
    string myText;

    // Read from the text file
    ifstream MyReadFile("input.txt");

    int score1 = 0;
    int score2;

    vector<int> current_path;
    vector<int> directories;
    int nb_directories = 0;
    int size;

    // Use a while loop together with the getline() function to read the file line by line
    while (getline(MyReadFile, myText)){
        if (myText.find("$ cd ..") != -1){
            current_path.pop_back();
        }
        else if(myText.find("$ cd") != -1){
            directories.push_back(0);
            current_path.push_back(nb_directories);
            nb_directories++;
        }
        else if(myText.find("$ ls") != -1 || myText.find("dir") != -1){
            ;
        }
        else { //size of file
            size = stoi(myText.substr(0,myText.find(' ')));
            for(int i : current_path){
                directories[i] += size;
            }
        }
    }

    for(int i = 0; i < nb_directories; i++){
        if (directories[i] <= MAX_SIZE){
            score1+= directories[i];
        }
        std::cout << i << " : " << directories[i] << endl;
    }

    // PART 2

    int spaceToFree = UNUSED - (DISK_SPACE - directories[0]);
    std::cout << "ToFree = " << spaceToFree << endl;

    vector<int> sorted_directories = directories;
    sort(sorted_directories.begin(), sorted_directories.end());

    for(int i = 0; i < nb_directories; i++){
        std::cout << i << " : " << sorted_directories[i] << endl;
        if (sorted_directories[i] >= spaceToFree){
            score2 = sorted_directories[i];
            break;
        }
    }


    // Close the file
    MyReadFile.close();

    std::cout << "Final Score 1 = " << score1 << endl;
    std::cout << "Final Score 2 = " << score2 << endl;
} 


