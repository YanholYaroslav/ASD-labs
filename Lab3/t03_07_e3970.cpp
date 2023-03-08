#include <iostream>
using namespace std;

int bin_search(int arr[], int n, int el, int first_time){
    int amount = -1;

    int l = 0;
    int r = n - 1;
    while (l <= r){
        int m = (l + r) / 2;
        if (el == arr[m]){
            amount = m;
            if (first_time){
                r = m - 1;
            }
            else {
                l = m + 1;
            }
        }
        else if (el < arr[m]){
            r = m - 1;
        }
        else {
            l = m + 1;
        }
    }
    return amount;
}


int main(){
    int n, m;
    cin >> n;
    int col[n];
    for(int i = 0; i < n; i++){
        cin >> col[i];
    }
    cin >> m;
    int inp[m];
    for(int i = 0; i < m; i++){
        cin >> inp[i];
    }


    for(int i = 0; i < m; i++){
        int first = bin_search(col, n, inp[i], 1);
        int last = bin_search(col, n, inp[i], 0);
        if (first != -1){
            cout << last - first + 1 << "\n";
        }
        else cout << 0 << "\n";
    }
    return 0;
}
