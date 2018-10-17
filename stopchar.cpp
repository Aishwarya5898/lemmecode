#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    string str1;
    getline(cin,str1);
    int n = str1.size() - 1;
    if( str1[n] != '.')
    {
    str1.push_back('.');
    cout<<str1;
    }
    else
    {
     cout<<"Invalid input";
    }
    return 0;
}
