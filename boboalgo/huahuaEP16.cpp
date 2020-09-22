#include <iostream>
using namespace std;
int main() {
    constexpr int kRows = 2;
    constexpr int kCols = 3;
    int arr[kRows][kCols] = {{1, 2, 3}, {4, 5, 6}};
    for (int y = 0; y < kRows; ++y) {
        for (int x = 0; x < kCols; ++x) {
            cout << arr[y][x] << " ";
        }
        cout << endl;
    }
    for (int y = 0; y < kRows; ++y)
        for (int x = 0; x < kCols; ++x)
            cout << &(arr[y][x]) - &(arr[0][0]) << " ";
    return 0;
}