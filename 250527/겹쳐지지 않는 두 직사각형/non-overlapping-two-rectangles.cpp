#include <iostream>

using namespace std;

int n, m;
int grid[5][5];
bool check[5][5];
int Result = -0x7FFFFFF;
void Check(int l1, int r1, int u1, int d1, int l2, int r2, int u2, int d2) {
    int Sum = 0;
    for(int i = 0; i < 5; i++) for(int j = 0; j < 5; j++) check[i][j] = false;
    for(int i = l1; i <= r1; i++) {
        for(int j = u1; j <= d1; j++) {
            Sum += grid[i][j];
            check[i][j] = true;
        }
    }
    for(int i = l2; i <= r2; i++) {
        for(int j = u2; j <= d2; j++) {
            Sum += grid[i][j];
            if(check[i][j]) return;
        }
    }
    if(Result < Sum) Result = Sum;
}
int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }
    for(int l1 = 0; l1 < n; l1++) {
        for(int r1 = l1; r1 < n; r1++) {
            for(int u1 = 0; u1 < n; u1++) {
                for(int d1 = u1; d1 < n; d1++) {
                    for(int l2 = 0; l2 < n; l2++) {
                        for(int r2 = l2; r2 < n; r2++) {
                            for(int u2 = 0; u2 < n; u2++) {
                                for(int d2 = u2; d2 < n; d2++) {
                                    Check(l1, r1, u1, d1, l2, r2, u2, d2);
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    cout << Result;
    return 0;
}
