#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int solve(int size_signal, string myText){

    int n_following = size_signal; 

    char buffer[n_following];
    int counter_full = 0;

    int before_next=0;

    for (int i=0; i < n_following; i++){
        
        std::cout << std::endl;
        for (int j = 0; j < counter_full; j++){
            std::cout << buffer[j] << " ";
            if (myText[i] == buffer[j]){
                if (j > before_next)
                    before_next = j;
            }
            
        }
        counter_full++;
        buffer[i] = myText[i];
        std::cout << before_next << std::endl;
    }

    std::cout << "\nFILL OVER --------------------"<<std::endl;

    char next;
    int answer;
    

    for (int i = n_following ; i < myText.size();i++){
        next = myText[i];


        for (int j = 0; j < n_following; j++){
            std::cout << buffer[j] << " ";
            if (next == buffer[j]){
                if (j > before_next)
                    before_next = j;
            }
        }

        std::cout << before_next << std::endl;

        if (before_next == 0){
            answer = i + 1;
            break;
        }
        for (int n = 0; n < n_following - 1; n++)
            buffer[n] = buffer[n+1];
        buffer[n_following - 1] = next;
        before_next --;
        
    }

    return answer;

}



int main() {
    // Create a text string, which is used to output the text file
    string myText;

    // Read from the text file
    ifstream MyReadFile("input.txt");

    // Use a while loop together with the getline() function to read the file line by line
    getline(MyReadFile, myText);

    int answer1 = solve(4,myText);
    int answer2 = solve(14,myText);



    cout << "Answer 1: " << answer1 << endl;
    cout << "Answer 2: " << answer2 << endl;

    // Close the file
    MyReadFile.close();
} 


