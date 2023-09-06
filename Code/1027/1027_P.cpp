#include <iostream>
using namespace std;

const int MAXN = 51;
int N;
int height[MAXN];

int main(){
    scanf("%d", &N);
    for (int i = 1; i <= N; i++){
        scanf("%d", &height[i]);
    }
    
    int ans = 0;

    for (int i = 1; i <= N; i++){//i번째 건물에 서서
        double slope;
        int cnt = 0;
        for (int j = 1; j < i; j++){//j번째 건물을 본다(왼쪽)
            //i번째 건물과 j번째 건물을 이어보고 -> 사이에 이것보다 기울기가 크거나 같은 게 있으면 X 
            bool canSee = true;
            int heightDiff = height[i] - height[j];
            int idxDiff = i - j;
            slope = 1.0 * heightDiff / idxDiff;

            for (int k = j + 1; k < i; k++){
                int hDiffBetween = height[i] - height[k];
                int idxDiffBetween = i - k; 
                double slopeBetween = 1.0 * hDiffBetween / idxDiffBetween;

                if (slope >= slopeBetween) {
                    canSee = false; 
                }
            }

            if (canSee) cnt++; 
        }

        for (int j = i + 1; j <= N; j++){//j번째 건물을 본다(오른쪽)
            bool canSee = true;
            int heightDiff = height[i] - height[j];
            int idxDiff = i - j;
            slope = 1.0 * heightDiff / idxDiff;

            for (int k = i + 1; k < j; k++){
                int hDiffBetween = height[i] - height[k];
                int idxDiffBetween = i - k; 
                double slopeBetween = 1.0 * hDiffBetween / idxDiffBetween;

                if (slope <= slopeBetween) {
                    canSee = false; 
                }
            }

            if (canSee) cnt++; 
        }

        ans = max(cnt, ans);
    }    
    printf("%d", ans);
}
