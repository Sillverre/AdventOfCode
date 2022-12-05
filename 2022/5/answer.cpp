#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <bits/stdc++.h>

using namespace std;


struct order{
    int n_toMove;
    int from;
    int dest;
};

struct order extract_order(string line){
    struct order order;
    string part1 = line.substr(4,line.find(" from "));
    string part2 = line.substr(line.find(" from ") + 6,line.find(" to "));
    string part3 = line.substr(line.find(" to ") + 4,line.size());

    order.n_toMove = stoi(part1);
    order.from = stoi(part2) -1;
    order.dest = stoi(part3) -1;

    return order;
}

void part1(int nStack,std::vector<char>* stacks, ifstream& MyReadFile){
    string myText;
    getline(MyReadFile, myText);

    struct order order;
    while (getline(MyReadFile, myText)){
        order = extract_order(myText);
        std::cout <<"move "<< order.n_toMove <<" from "<< order.from <<" to "<< order.dest << endl;

        for(int i = 0; i < order.n_toMove; i++){
            stacks[order.dest].push_back(stacks[order.from].back());
            stacks[order.from].pop_back();
        }
    
    }


    for (int i = 0; i < nStack; i++){
        
        for(char c : stacks[i]){
            std::cout << c << ' ';
        }
        std::cout << endl;
    }




    for (int i = 0; i < nStack; i++){
        std::cout << stacks[i].back();
    }
}

void part2(int nStack,std::vector<char>* stacks, ifstream& MyReadFile){
    string myText;
    getline(MyReadFile, myText);

    struct order order;
    std::vector<char> temp;

    while (getline(MyReadFile, myText)){
        order = extract_order(myText);
        std::cout <<"move "<< order.n_toMove <<" from "<< order.from <<" to "<< order.dest << endl;

        for(int i = 0; i < order.n_toMove; i++){
            temp.push_back(stacks[order.from].back());
            stacks[order.from].pop_back();
        }
        for(int i = 0; i < order.n_toMove; i++){
            stacks[order.dest].push_back(temp.back());
            temp.pop_back();
        }
    
    }


    for (int i = 0; i < nStack; i++){
        
        for(char c : stacks[i]){
            std::cout << c << ' ';
        }
        std::cout << endl;
    }


    for (int i = 0; i < nStack; i++){
        std::cout << stacks[i].back();
    }
}


int main() {
    // Create a text string, which is used to output the text file
    string myText;

    // Read from the text file
    ifstream MyReadFile("input.txt");
    

    string score1 = "";
    string score2 = "";

    char letter;

    // get first line to get size of input
    getline(MyReadFile, myText);
    int nStack = myText.size() / 4 +1; 

    std::vector<char> stacks[nStack];
    
    // Retrieve input part1

    for (int i = 0; i < nStack; i++){
        letter = myText[1 + 4*i];
        if (letter != ' '){
            stacks[i].push_back(letter);
        }
    }

    // Use a while loop together with the getline() function to read the file line by line
    while (getline(MyReadFile, myText)){
        if(myText[0] == ' ')
            break;

        for (int i = 0; i < nStack; i++){
            letter = myText[1 + 4*i];
            if (letter != ' '){
                stacks[i].push_back(letter);
            }
        }
    }

    for (int i = 0; i < nStack; i++){
        std::reverse(stacks[i].begin(), stacks[i].end());
        for(char c : stacks[i]){
            std::cout << c << ' ';
        }
        std::cout << endl;
    }

    //End Retrieve input part1
    std::cout << " / // // / // / // / / "<< endl;

    part2(nStack, stacks, MyReadFile);

    

    // Close the file
    MyReadFile.close();
} 


