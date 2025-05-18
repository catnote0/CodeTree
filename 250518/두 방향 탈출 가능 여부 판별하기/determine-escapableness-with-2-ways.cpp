#include <iostream>
using namespace std;
int n, m;
int grid[110][110];
bool visited[110][110];
void search(int x, int y) {
    if(x == n - 1 && y == m - 1) {
        printf("1");
        exit(0);
    }
    if(grid[x + 1][y] && !visited[x + 1][y]) search(x + 1, y);
    if(grid[x][y + 1] && !visited[x][y + 1]) search(x, y + 1);
    visited[x][y] = true;
}
int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }
    search(0, 0);
    printf("0");
    return 0;
}
