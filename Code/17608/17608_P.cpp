#include <iostream>
using namespace std;

int height[100000];

int main(){
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++){
        scanf("%d", &height[i]);
    }

    int cnt = 0;
    int max = height[N-1];
    
    for (int i = N - 2; i >= 0; i--){
        if (height[i] > max) {
            cnt++;
            max = height[i];
        }
    }
    printf("%d", cnt + 1);
}
