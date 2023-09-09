#include <iostream>
using namespace std;

const int MAXN = 100001;

int N, M, a, b, n;
int nums[MAXN];
int tree[MAXN * 4];

int makeTree(int root, int start, int end){
	if (start == end) return tree[root] = nums[start];
	int mid = (start + end) / 2;
	return tree[root] = min(makeTree(root * 2, start, mid), makeTree(root * 2 + 1, mid + 1, end));
}

int search(int node, int left, int right, int start, int end){
    if (end < left || right < start) return 1000000000;
    if (left <= start && end <= right) return tree[node];

    int mid = (start + end) / 2;
    return min(search(node * 2, left, right, start, mid), search(node * 2 + 1, left, right, mid + 1, end));
}

int main(){
    scanf("%d%d", &N, &M);

    for (int i = 1; i <= N; i++) {
        scanf("%d", &nums[i]);
    } 

    makeTree(1, 1, N);

    for (int i = 0; i < M; i++){
        scanf("%d%d", &a, &b);
        printf("%d\n", search(1, a, b, 1, N));
    }
}
