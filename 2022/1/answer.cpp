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

    int food = 0;
    std::vector<int> elves; 
    int max1 = 0;
    int max_i1 = 0;
    int max2 = 0;
    int max_i2 = 0;
    int max3 = 0;
    int max_i3 = 0;

    // Use a while loop together with the getline() function to read the file line by line
    while (getline(MyReadFile, myText)){
        if (myText != ""){
            food += std::stoi(myText);
        }
        else{
            elves.push_back(food);
            if (food > max1){
                max3 = max2;
                max_i3 = max_i2;
                max2 = max1;
                max_i2 = max_i1;
                max1 = food;
                max_i1 = elves.size();
            }
            else if(food > max2){
                max3 = max2;
                max_i3 = max_i2;
                max2 = food;
                max_i2 = elves.size();
            }
            else if(food > max3){

                max3 = food;
                max_i3 = elves.size();
            }
            food=0;
        }   
    }

    // Close the file
    MyReadFile.close();

    std::cout << "Max1: " << max1 << "// Index1:" << max_i1 << '\n';
    std::cout << "Max2: " << max2 << "// Index2:" << max_i2 << '\n';
    std::cout << "Max3: " << max3 << "// Index3:" << max_i3 << '\n';

    std::cout << "Sum of them = " << max1 + max2 + max3 ;
} 


