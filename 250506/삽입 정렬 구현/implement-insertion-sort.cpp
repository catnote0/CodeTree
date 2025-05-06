#include <iostream>

#define MAX_N 100

using namespace std;

int n;
int arr[MAX_N];

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    for(int i = 0; i < n; i++) {
        int num = arr[i];
        for(int j = i - 1; j >= -1; j--) {
            if(j >= 0 && arr[j] > num) arr[j + 1] = arr[j];
            else {
                arr[j + 1] = num;
                break;
            }
        }
    }
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    return 0;
}
