#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

int N, K, D, A, B, C;
vector<tuple<int, int, int>> rules;

int main(){
    scanf("%d%d%d", &N, &K, &D);

    //A : 시작, B : 끝, C : 간격
    for (int i = 0; i < K; i++){
        scanf("%d%d%d", &A, &B, &C);
        rules.emplace_back(A, B, C);
    }

    //누적합? or 이분탐색
    //일일이 다 집어 넣으면 -> 10억이므로 시간초과.
    //단조 증가 -> 이분탐색 하기 위한 조건 만족
    
    int start = 1, end = N, mid;
    int ans = 0;

    while (start <= end){
        long long cnt = 0;        
        mid = (start + end) / 2;

        for (int i = 0; i < K; i++){
            tuple<int, int, int> rule = rules[i];
            int s = get<0>(rule); 
            int e = get<1>(rule);
            int step = get<2>(rule); 

            if (s > mid) continue;//기준점 뒤에서 시작하면 셀 필요없음
            e = min(e, mid); //기준점 뒤로 넘어가는 것도 셀 필요없음 
            int add = (e - s) / step + 1;
            //printf("[%d] : %d\n", i, add);
            cnt += add;
        }

        //printf("start: %d, end : %d, mid : %d, cnt: %lld\n", start, end, mid, cnt);
        if (cnt < D) start = mid + 1;//적으면 늘림
        else {//많으면 줄임
            end = mid - 1;
            ans = mid;
        }
    }

    printf("%d\n", ans);

}
