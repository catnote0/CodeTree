#include <iostream>
using namespace std;
int K, N;
int arr[10];
void comb(int pos, int ll, int l) {
    if(pos > N) {
        for(int i = 1; i <= N; i++) cout << arr[i] << " ";
        cout << endl;
        return;
    }
    for(int i = 1; i <= K; i++) {
        if(ll == l && l == i) continue;
        arr[pos] = i;
        comb(pos + 1, l, i);
        arr[pos] = 0;
    }
}
int main() {
    cin >> K >> N;
    comb(1, 0, 0);
    return 0;
}
