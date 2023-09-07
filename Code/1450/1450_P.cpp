#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define ll long long
const int MAXN = 30;//N은 최대 30

int N, C, weight;
int stuff[MAXN];
vector<ll> startToMid;
vector<ll> midToEnd; 

int main(){
    scanf("%d%d", &N, &C);

    for (int i = 0; i < N; i++) scanf("%d", &stuff[i]);
    
    //N이 최대 30이므로 가능한 경우의 수는 최대 2^30 = 1073741824
    //naive하게 모든 경우를 다 확인하면 10초 가량 걸림


    //반반 나누는 경우
    //2^15 * 2 = 32768 * 2= 65536번 계산함 (1 ~ 반, 반 ~끝)
    //O(log(N/2) ^ 2)
    int half = N / 2;

    for (int i = 0; i < (1 << half); i++){
        ll sum = 0;
        for (int b = 0; b < half; b++){
            if (!((1 << b) & i)) continue;
            sum += stuff[b];
        }
        startToMid.push_back(sum);
    }

    for (int i = 0; i < (1 << (N- half)); i++){
        ll sum = 0;
        for (int b = 0; b < (N - half); b++){
            if (!((1 << b) & i)) continue;
            sum += stuff[half + b];
        }
        midToEnd.push_back(sum);
    }

    sort(startToMid.begin(), startToMid.end());
    sort(midToEnd.begin(), midToEnd.end());

    int ans = 0;

    for (int i = 0; i < startToMid.size(); ){
        int leftUB = upper_bound(startToMid.begin(), startToMid.end(), startToMid[i]) - startToMid.begin();
        int leftCount = leftUB - i;
        int rightCount = upper_bound(midToEnd.begin(), midToEnd.end(), C - startToMid[i]) - midToEnd.begin();
        i = leftUB; 
        ans += leftCount * rightCount; 
    }

    printf("%d", ans);

}
