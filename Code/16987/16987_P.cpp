#include <iostream>
using namespace std;

const int MAXN = 8;
int N, ans;
int s[MAXN], w[MAXN];

void breakEgg(int idx, int count){

    ans = max(ans, count);
    if (idx == N) return;
    
    if (s[idx] <= 0) {
        breakEgg(idx + 1, count);
        return;
    }

    for (int i = 0; i < N; i++){
        if (idx == i) continue;
        if (s[i] <= 0) continue;//broken

        s[i] -= w[idx];
        s[idx] -= w[i];

        if (s[idx] <= 0) count++;
        if (s[i] <= 0) count++;

        breakEgg(idx + 1, count);

        if (s[idx] <= 0) count--;
        if (s[i] <= 0) count--;
        
        s[i] += w[idx];
        s[idx] += w[i];
    }
}

int main(){
    scanf("%d", &N);
    for (int i = 0; i < N; i++){
        scanf("%d%d", &s[i], &w[i]);
    }

    breakEgg(0, 0);
    printf("%d", ans);
}
