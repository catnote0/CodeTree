#include <iostream>
#include<deque>
using namespace std;
int Arr[5100];
int N, K;
deque<int> dq;
int main() {
    cin >> N >> K;
    for(int i = 1; i <= N; i++) dq.push_back(i);
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j < K; j++) {
            dq.push_back(dq.front());
            dq.pop_front();
        }
        cout << dq.front() << " ";
        dq.pop_front();
    }
    return 0;
}
