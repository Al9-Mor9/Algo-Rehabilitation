#include <iostream>
#include <queue>
using namespace std;

const int MAXN = 100000;

int N, M, num;
int dataStructureType[MAXN];
deque<int> deq;

int main(){
    scanf("%d", &N);

    //A
    for (int i = 0; i < N; i++){
        scanf("%d", &dataStructureType[i]);
    }

    //B
    for (int i = 0; i < N; i++){
        scanf("%d", &num);
        if (!dataStructureType[i]) deq.push_back(num);
    }

    //M
    scanf("%d", &M);
    for (int i = 0; i < M; i++){
        scanf("%d", &num);
        deq.push_front(num);
        printf("%d ", deq.back());
        deq.pop_back();
    }
}
