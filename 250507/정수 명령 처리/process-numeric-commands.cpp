#include <iostream>

using namespace std;

int N;
string command[10000];
int value[10000];
int stack[10000];
int stack_size;

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> command[i];
        if (command[i] == "push") {
            cin >> value[i];
            stack[stack_size++] = value[i];
        }
        if(command[i] == "pop") cout << stack[--stack_size] << endl;
        if(command[i] == "size") cout << stack_size << endl;
        if(command[i] == "empty") cout << (stack_size ? 0 : 1) << endl;
        if(command[i] == "top") cout << stack[stack_size - 1] << endl;
    }

    return 0;
}
