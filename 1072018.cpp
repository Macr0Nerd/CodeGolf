/*
Challenge for the week of 10/07/2018
------------------------------------
This is our first challenge so we are going to start off sort of easy.
This week's challenge is to take a string input and output the string mockingly.

For instance:
"hello world" ---> "HeLlO WoRlD"
"stop mocking me" ---> "StOp mOcKiNg mE"

In order to be considered a valid solution, the capitalization of characters must be alternating.
You may assume the starting string is all lower case
You do not need to define a function with inputs and outputs, accept user input, or hard code a string.
The existence of the string is implied and adding these things in increases character count to an extreme degree in some languages (looking at you, Java).
*/

#include <iostream>
#include <string>
using namespace std;

int main(){
    string x = "stop mocking me";
    int z;
    for (z = 0; z < x.length(); z+=2) {
        x[z] = toupper(x[z]);
    }

    cout << x << endl;
    return 0;
}