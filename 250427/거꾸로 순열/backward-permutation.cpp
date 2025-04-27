#include <iostream>
using namespace std;
int n;
int arr[10];
bool check[10];
void perm(int pos) {
    if(pos > n) {
        for(int i = 1; i <= n; i++) cout << arr[i] << " ";
        cout << endl;
        return;
    }
    for(int i = n; i > 0; i--) {
        if(!check[i]) {
            check[i] = true;
            arr[pos] = i;
            perm(pos + 1);
            arr[pos] = 0;
            check[i] = false;
        }
    }
}
int main() {
    cin >> n;
    perm(1);
    return 0;
}
