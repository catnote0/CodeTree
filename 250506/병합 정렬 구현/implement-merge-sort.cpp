#include <iostream>

using namespace std;

int n;
int arr[110000];
int subarr[110000];
void merge(int start, int mid, int end) {
    int left = start, right = mid + 1;
    int cnt = 0;
    while(left <= mid && right <= end) {
        if(arr[left] < arr[right]) subarr[cnt++] = arr[left++];
        else subarr[cnt++] = arr[right++];
    }
    while(left <= mid) subarr[cnt++] = arr[left++];
    while(right <= end) subarr[cnt++] = arr[right++];
    for(int i = 0; i < cnt; i++) arr[start + i] = subarr[i];
}
void mergesort(int start, int end) {
    if(start != end) {
        mergesort(start, (start + end) / 2);
        mergesort((start + end) / 2 + 1, end);
        merge(start, (start + end) / 2, end);
    }
}
int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    mergesort(0, n - 1);
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    return 0;
}
