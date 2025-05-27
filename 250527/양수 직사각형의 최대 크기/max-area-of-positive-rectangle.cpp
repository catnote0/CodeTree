#include <iostream>

using namespace std;

int n, m;
int grid[20][20];
int Result = -1;
void Check(int u, int d, int l, int r) {
    for(int i = u; i <= d; i++) {
        for(int j = l; j <= r; j++) {
            if(grid[i][j] <= 0) return;
        }
    }
    if(Result < (d - u + 1) * (r - l + 1)) Result = (d - u + 1) * (r - l + 1);
}
int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    for(int i = 0; i < n; i++) {
        for(int j = i; j < n; j++) {
            for(int k = 0; k < m; k++) {
                for(int l = k; l < m; l++) {
                    Check(i, j, k, l);
                }
            }
        }
    }
    cout << Result;
    return 0;
}
