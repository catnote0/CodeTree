#include <iostream>
using namespace std;
int N;
int main() {
    cin >> N;
    int n = 1;
    while(n * 2 <= N) n *= 2;
    if(n == N) cout << N;
    else cout << (N - n) * 2;
    return 0;
}
