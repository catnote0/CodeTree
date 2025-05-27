#include <iostream>

using namespace std;

int n, m;
int grid[200][200];
int result;
int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    for(int i = 1; i < n; i++) {
        for(int j = 1; j < n; j++) {
            int s = grid[i - 1][j - 1] + grid[i - 1][j] + grid[i][j - 1] + grid[i][j];
            int m1 = grid[i - 1][j - 1] < grid[i - 1][j] ? grid[i - 1][j - 1] : grid[i - 1][j];
            int m2 = grid[i][j - 1] < grid[i][j] ? grid[i][j - 1] : grid[i][j];
            int m = m1 < m2 ? m1 : m2;
            if(s - m > result) result = s - m;
        }
    }
    for(int i = 0; i < n; i++) {
        for(int j = 2; j < n; j++) {
            int s = grid[i][j - 2] + grid[i][j - 1] + grid[i][j];
            if(s > result) result = s;
            s = grid[j - 2][i] + grid[j - 1][i] + grid[j][i];
            if(s > result) result = s;
        }
    }
    cout << result;
    return 0;
}
