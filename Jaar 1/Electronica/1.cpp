#include <iostream>

using std::cin;
using std::cout;

int main(){
    int m, n = 0;
    float prices[n];
    for (int i = 0; i < n ; i++){
        float temp;
        cin >> temp;
        prices[n] = temp;
    }

    cin >> m;
    int amounts[m][n];
    float total = 0;
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            int temp;
            cin >> temp;
            amounts[i][j] = temp;
            total += temp * prices[j];
        }
    }
    cout << total;

}
