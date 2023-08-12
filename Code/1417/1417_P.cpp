#include <iostream>
#include <queue>
using namespace std;

priority_queue<int> pq;

int main(){
    int N, ds, cand, cnt = 0;

    scanf("%d", &N);
    scanf("%d", &ds);

    for (int i = 1; i < N; i++){
        scanf("%d", &cand);
        pq.push(cand);
    }

    while (!pq.empty() && pq.top() >= ds){
        int top = pq.top();
        pq.pop();
        pq.push(--top);
        ds++;
        cnt++;
    }

    printf("%d", cnt);
}
