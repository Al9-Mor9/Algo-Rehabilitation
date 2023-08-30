#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, n;
vector<int> A, B;

int main(){
    scanf("%d", &N);
    for (int i = 0; i < N; i++){
        scanf("%d", &n);
        A.push_back(n);
    }
    for (int i = 0; i < N; i++){
        scanf("%d", &n);
        B.push_back(n);
    }

    sort(A.begin(), A.end(), greater<>());
    sort(B.begin(), B.end());

    int ans = 0;
    for (int i = 0; i < N; i++){
        ans += A[i] * B[i];
    }
    
    printf("%d", ans);
}
