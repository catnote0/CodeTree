#include <iostream>
using namespace std;
int num, n;
int blocks[100];
int s, e;
int main() {
    cin >> n;
    num = n;
    for(int i = 0; i < n; i++) cin >> blocks[i];
    for(int i = 0; i < 2; i++) {
        cin >> s >> e;
        int count = 0;
        for(int j = 0; j < n; j++) {
            if(blocks[j] > 0) {
                count++;
                if(s <= count && count <= e) blocks[j] = --num - n;
            }
        }
    }
    cout << num << endl;
    for(int i = 0; i < n; i++) if(blocks[i] > 0) cout << blocks[i] << endl;
    return 0;
}
