#include <iostream>

using namespace std;

int n;
int arr[210000];
void swap(int x, int y) {
    int tmp = arr[x];
    arr[x] = arr[y];
    arr[y] = tmp;
}
void heapify(int index) {
    if(arr[index] >= arr[index * 2] && arr[index] >= arr[index * 2 + 1]) return;
    if(arr[index * 2] < arr[index * 2 + 1]) {
        swap(index, index * 2 + 1);
        heapify(index * 2 + 1);
    }
    else {
        swap(index, index * 2);
        heapify(index * 2);
    }
}

void make_heap() {
    for(int i = n / 2; i > 0; i--) heapify(i);
}

int main() {
    cin >> n;

    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }

    make_heap();
    for(int i = n; i > 0; i--) {
        swap(1, i);
        arr[i] *= -1;
        heapify(1);
    }
    for(int i = 1; i <= n; i++) cout << -arr[i] << " ";
    return 0;
}
