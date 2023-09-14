#include <iostream>
using namespace std;

const int MAXN = 1000001;

int N, M, cmd, j, k;
int nums[MAXN];
long long tree[MAXN * 4];

void appendTree(int node, int start, int end, int idx, int val){
    if (end < idx || idx < start) return;
    tree[node] += val;

    int mid = (start + end) / 2;
    if (start != end) {
        appendTree(2 * node, start, mid, idx, val);
        appendTree(2 * node + 1, mid + 1, end, idx, val); 
    }
}

long long getSum(int node, int left, int right, int start, int end){
    if (end < left || right < start) return 0;
    if (left <= start && end <= right) return tree[node];

    int mid = (start + end) / 2;
    return getSum(node * 2, left, right, start, mid) + getSum(node * 2 + 1, left, right, mid + 1, end);
}

int main(){
    scanf("%d%d", &N, &M);

    for (int i = 0; i < M; i++){
        scanf("%d%d%d", &cmd, &j, &k);
        if (cmd){//modify
            appendTree(1, 1, N, j, -nums[j] + k);
            nums[j] = k;
        }
        else {//sum
            if (j > k) swap(j, k);
            printf("%lld\n", getSum(1, j, k, 1, N));
        }
    } 
}
