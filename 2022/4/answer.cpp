#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct elfPair{
    int elf1_start;
    int elf1_end;
    int elf2_start;
    int elf2_end;
};

struct elfPair extract_elfPair(string line){
    struct elfPair pair;
    string part1 = line.substr(0,line.find(','));
    string part2 = line.substr(line.find(',') + 1,line.size());

    pair.elf1_start = stoi(part1.substr(0, part1.find('-')));
    pair.elf1_end = stoi(part1.substr(part1.find('-') + 1, part1.size()));
    pair.elf2_start = stoi(part2.substr(0, part2.find('-')));
    pair.elf2_end = stoi(part2.substr(part2.find('-') + 1, part2.size()));

    return pair;
}

int main() {
    // Create a text string, which is used to output the text file
    string myText;

    // Read from the text file
    ifstream MyReadFile("input.txt");

    int score1 = 0;
    int score2 = 0;
  
    struct elfPair pair;

    // Use a while loop together with the getline() function to read the file line by line
    while (getline(MyReadFile, myText)){
        pair = extract_elfPair(myText);

        if((pair.elf1_start <= pair.elf2_start && pair.elf1_end >= pair.elf2_end) || (pair.elf2_start <= pair.elf1_start && pair.elf2_end >= pair.elf1_end)){
            score1++;
            score2++;
        }else if((pair.elf2_start <= pair.elf1_end && pair.elf2_end >= pair.elf1_start) || (pair.elf1_start <= pair.elf2_end && pair.elf1_end >= pair.elf2_start)){
            score2++;
        }
    }
    
    // Close the file
    MyReadFile.close();

    std::cout << "Final Score 1 = " << score1 << '\n';
    std::cout << "Final Score 2 = " << score2 << '\n';
} 


