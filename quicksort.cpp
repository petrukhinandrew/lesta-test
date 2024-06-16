#include <iostream> 
#include <vector> 
#include <utility> 

void quicksort(std::vector<int>& arr, int l, int r) {
    if (l >= r) return;
    int pivot = arr[r];
    int tmp_l = l;
    int tmp_r = r;
    r--;
    while (l <= r) {
        while (l <= r && arr[l] <= pivot) l++;
        while (l <= r && arr[r] >= pivot) r--;

        if (l < r) std::swap(arr[l], arr[r]);
    }
    std::swap(arr[tmp_r], arr[l]);
    quicksort(arr, tmp_l, l - 1);
    quicksort(arr, l + 1, tmp_r);
}

void printVector(std::vector<int>& v) {
    for (int elem : v) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::vector<std::vector<int>> testcases{
        {1, 2, 3},
        {5, 4, 3, 2, 1},
        {0},
        {5,1,4,2,3}
    };
    for (auto t : testcases) {
        std::cout << "init: ";
        printVector(t);
        quicksort(t, 0, t.size() - 1);
        std::cout << "sorted: ";
        printVector(t);
    }
    return 0;
}