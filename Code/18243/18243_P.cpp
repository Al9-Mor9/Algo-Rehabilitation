#include <iostream>
using namespace std;

int N, K, A, B;
int isFriend[100][100];
int floyd[100][100];

int main(){
    scanf("%d%d", &N, &K);
    for (int i = 0; i < K; i++){
        scanf("%d%d", &A, &B);
        isFriend[A-1][B-1] = isFriend[B-1][A-1] = 1;
    }

    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            if (isFriend[i][j]) floyd[i][j] = 1;
            else floyd[i][j] = 999999;
        }
    }

    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            for (int k = 0; k < N; k++){
                if (floyd[j][i] + floyd[i][k] < floyd[j][k]) {
                    floyd[j][k] = floyd[j][i] + floyd[i][k];
                }    
            }
        }
    }

    bool smallnet = true;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            if (i != j && floyd[i][j] > 6){
                smallnet = false;
                break;
            }
        }
        if (!smallnet) break;
    }

    printf("%s", smallnet ? "Small World!" : "Big World!");
}
