/**
 * Build a binary to string translator in as few characters as possible (white space included!).
 *
 * Rules:
 * • Class implementation IS counted
 * • Import statements ARE counted
 * • Print statements (within reason) ARE NOT counted
 * • The input will be a string and IS NOT counted
 * • Whitespace IS counted
 * • Any Turing complete language is allowed
 * • Sharing solutions is allowed (I will have all my code public on my GitHub)
 * • The string will be only 1s, 0s, and spaces. It will be complete bytes space separated.
 * • Using built in binary translators ARE NOT allowed!
 */

#include <iostream> //Not counted; Only for i/o
#include <cmath>
int main(){
    char z[100]; std::cin>>z; //Not counted; Setting input
    int x;int c=8;char*a;
    for(auto &i:z){--c;i-48?x+=pow(2,c):0;!i-32?*a=x:*a;!i-32?++a:0;!i-32?x=0:x;!i-32?c=0:c;}
    std::cout<<a;
    return 0;
}
