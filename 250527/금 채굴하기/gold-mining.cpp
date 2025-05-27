#include <iostream>
#include <cstdlib>

using namespace std;

int n, m;
int grid[20][20];
int result;
bool isValid(int x, int y) {
    if(x < 0 || x >= n || y < 0 || y >= n) return false;
    return true;
}
int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            int count = grid[i][j];
            for(int k = 1; k < n; k++) {
                for(int x = -k; x <= k; x++) {
                    int y = k - abs(x);
                    if(isValid(i + x, j - y)) count += grid[i + x][j - y];
                    if(y && isValid(i + x, j + y)) count += grid[i + x][j + y];
                }
                int size = k * k + (k + 1) * (k + 1);
                if(size <= count * m && result < count) result = count;
            }
        }
    }
    cout << result;
    return 0;
}
