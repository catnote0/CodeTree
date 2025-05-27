#include <iostream>

using namespace std;

int n, m;
int grid[100][100];
int result;
int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }
    if(m == 1) {
        cout << n * 2;
        return 0;
    }
    for(int i = 0; i < n; i++) {
        int rowcombo = 1, columncombo = 1;
        bool rowhappy = false, columnhappy = false;
        for(int j = 1; j < n; j++) {
            if(grid[i][j - 1] == grid[i][j]) rowcombo++;
            else rowcombo = 1;
            if(grid[j - 1][i] == grid[j][i]) columncombo++;
            else columncombo = 1;
            if(rowcombo >= m) rowhappy = true;
            if(columncombo >= m) columnhappy = true;
        }
        if(rowhappy) result++;
        if(columnhappy) result++;
    }
    cout << result;

    return 0;
}
