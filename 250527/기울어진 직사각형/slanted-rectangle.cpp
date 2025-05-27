#include <iostream>

using namespace std;
int n;
int grid[20][20];
int Result;
bool isValid(int x, int y) {
    if(x < 0 || x >= n || y < 0 || y >= n) return false;
    return true;
}
int getRect(int x, int y, int h, int w) {
    int sum = 0;
    int length[4] = {w, h, w, h};
    int d[4][2] = {1, -1, 1, 1, -1, 1, -1, -1};
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < length[i]; j++) {
            x += d[i][0];
            y += d[i][1];
            if(!isValid(x, y)) return -1;
            sum += grid[x][y];
        }
    }
    return sum;
}
int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            for(int h = 1; h < n; h++) {
                for(int w = 1; w < n; w++) {
                    int sum = getRect(i, j, h, w);
                    if(Result < sum) Result = sum;
                }
            }
        }
    }
    cout << Result;
    return 0;
}
