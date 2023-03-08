#include <iostream>
using namespace std;

int bin_search(int arr[], int n, int el){
    int l = 0;
    int r = n - 1;
    while (l <= r){
        int m = l + (r - l) / 2;
        if (el > arr[m]){
            l = m + 1;
        }
        else if (el < arr[m]){
            r = m - 1;
        }
        else{
            cout << "YES\n";
            return 0;
        }
    }
    cout << "NO\n";
    return 0;      
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
        bin_search(col, n, inp[i]);
    }
    return 0;
}
