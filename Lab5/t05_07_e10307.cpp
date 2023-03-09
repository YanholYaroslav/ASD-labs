#include <iostream>
#include <vector>

using namespace std;

bool is_poss_place(int amount, vector<vector<int>>& places, int x) {
    int c = 1;
    int prev_place = places[0][0];
    for (auto seg : places) {
        for (auto i : seg) {
            if (i - prev_place >= x) {
                prev_place = i;
                c += 1;
            }
        }
    }
    return c >= amount;
}

int bin_search(int L, int R, int n, vector<vector<int>>& segs) {
    int l = 0;
    int r = R - L + 1;
    while (r - l > 1) {
        int m = l + (r - l) / 2;
        if (is_poss_place(n, segs, m)) {
            l = m;
        } else {
            r = m;
        }
    }
    return l;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> segs(m, vector<int>(2));
    for (int i = 0; i < m; i++) {
        cin >> segs[i][0] >> segs[i][1];
    }
    int res = bin_search(segs[0][0], segs[m-1][1], n, segs);
    cout << res << endl;
    return 0;
}
