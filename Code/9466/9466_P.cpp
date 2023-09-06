#include <iostream>
using namespace std;

const int MAXN = 100001;

int T, n;
int groupedCnt;
int student[MAXN], visiting[MAXN];
bool visited[MAXN];

int search(int i, int depth){
    if (visited[i]) return 0;
    int ret;
    if (visiting[i]){//돌다가 이미 방금 만났던 친구를 만나면
        return depth - visiting[i];
    }
    else {
        visiting[i] = depth;
        ret = search(student[i], depth + 1);
    }
    visited[i] = true;
    return ret;
}

int main(){
    scanf("%d", &T);
    
    while (T--){
        groupedCnt = 0;
        scanf("%d", &n);
        for (int i = 1; i <= n; i++){
            visited[i] = false;
            visiting[i] = 0;
            scanf("%d", &student[i]);
        } 

        for (int i = 1; i <= n; i++){
            if (visited[i]) continue;
            groupedCnt += search(i, 0);
        }

        printf("%d\n", n - groupedCnt);
    }
}
