#include <iostream>
using namespace std;

const int MAXN = 200000;
const int MAXA = 100001;

int N, K;
int arr[MAXN], cnt[MAXA];

int main(){
	scanf("%d%d", &N, &K);
	for (int i = 0; i < N; i++) scanf("%d", &arr[i]);

	int start = 0, end = 0, ans = 0;

	while (end < N){
		if (cnt[arr[end]] == K) {
			cnt[arr[start]]--;
			start++;
		}
		else {
			cnt[arr[end]]++;
			end++;
		}
		ans = max(ans, (end - start));
	}	
	printf("%d", ans);
}
