#include <iostream>
using namespace std;
int n, m;
int grid[22][22];
int dir[8][2] = {-1, -1, -1, 0, -1, 1, 0, -1, 0, 1, 1, -1, 1, 0, 1, 1};
int main() {
    cin >> n >> m;
    for(int i = 1; i <= n; i++) for(int j = 1; j <= n; j++) cin >> grid[i][j];
    for(int i = 1; i <= m; i++) {
        for(int j = 1; j <= n * n; j++) {
            int k;
            for(k = 1; k <= n * n; k++) if(grid[(k - 1) / n + 1][(k - 1) % n + 1] == j) break;
            int x = (k - 1) / n + 1, y = (k - 1) % n + 1;
            int Max = 0, d;
            for(int k = 0; k < 8; k++) {
                if(Max < grid[x + dir[k][0]][y + dir[k][1]]) {
                    Max = grid[x + dir[k][0]][y + dir[k][1]];
                    d = k;
                }
            }
            int tmp = grid[x][y];
            grid[x][y] = grid[x + dir[d][0]][y + dir[d][1]];
            grid[x + dir[d][0]][y + dir[d][1]] = tmp;
        }
    }
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) cout << grid[i][j] << " ";
        cout << endl;
    }
    return 0;
}
