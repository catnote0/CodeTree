#include <iostream>
using namespace std;
int n, Max;
int arr[110000];
int bucket[10][110000];
int main() {
    int divisor = 1;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cin >> arr[i];
        if(Max < arr[i]) Max = arr[i];
    }
    while(1) {
        for(int i = 1; i <= n; i++) {
            int num = (arr[i] / divisor) % 10;
            bucket[num][++bucket[num][0]] = arr[i];
        }
        int count = 0;
        for(int i = 0; i < 10; i++) {
            for(int j = 1; j <= bucket[i][0]; j++) arr[++count] = bucket[i][j];
            bucket[i][0] = 0;
        }
        divisor *= 10;
        if(divisor > Max) break;
    }
    for(int i = 1; i <= n; i++) cout << arr[i] << " ";
    return 0;
}
