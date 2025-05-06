#include <iostream>

using namespace std;

int n;
int arr[100000];
void swap(int x, int y) {
    int tmp = arr[x];
    arr[x] = arr[y];
    arr[y] = tmp;
}
int partition(int start, int end) {
    int pivot = arr[end];
    int i = start - 1;
    for(int j = start; j < end; j++) if(pivot > arr[j]) swap(++i, j);
    swap(i + 1, end);
    return i + 1;
}
void quicksort(int start, int end) {
    if(end - start >= 2) {
        int pivot = partition(start, end);
        quicksort(start, pivot - 1);
        quicksort(pivot + 1, end);
    }
    else if(end - start == 1) {
        if(arr[start] > arr[end]) swap(start, end);
    }
}
int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }


    quicksort(0, n - 1);
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    return 0;
}
