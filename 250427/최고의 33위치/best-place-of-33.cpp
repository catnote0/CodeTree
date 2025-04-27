#include <iostream>
using namespace std;
int N;
int grid[20][20];
int main() {
    int result = 0;
    cin >> N;
    for(int i = 0; i < N; i++) for(int j = 0; j < N; j++) cin >> grid[i][j];
    for(int i = 0; i < N - 2; i++) {
        for(int j = 0; j < N - 2; j++) {
            int count = 0;
            for(int k = 0; k < 3; k++) for(int l = 0; l < 3; l++) count += grid[i + k][j + l];
            if(result < count) result = count;
        }
    }
    cout << result;
    return 0;
}
