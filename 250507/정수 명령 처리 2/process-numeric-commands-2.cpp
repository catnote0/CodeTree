#include <iostream>
#include <string>
using namespace std;
int N;
string command[10000];
int A[10000];
int queue[10000];
int l = 0, r = -1;

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> command[i];
        if (command[i] == "push") {
            cin >> A[i];
            queue[++r] = A[i];
        }
        if(command[i] == "pop") cout << queue[l++] << endl;
        if(command[i] == "size") cout << (r - l + 1) << endl;
        if(command[i] == "empty") cout << ((r - l + 1) ? 0 : 1) << endl;
        if(command[i] == "front") cout << queue[l] << endl;
    }


    return 0;
}