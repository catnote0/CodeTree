#include <iostream>
#include <queue>
using namespace std;
queue<int> Q;
int N;

int main() {
    cin >> N;

    for(int i = 1; i <= N; i++) Q.push(i);
    for(int i = 1; i < N; i++) {
        Q.pop();
        Q.push(Q.front());
        Q.pop();
    }
    cout << Q.front();
    return 0;
}
