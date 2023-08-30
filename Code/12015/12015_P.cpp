#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, n;
vector<int> dp;

int main(){
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%d", &n);
		int lb = lower_bound(dp.begin(), dp.end(), n) - dp.begin();
		if (lb == dp.size()) dp.push_back(n);
		else dp[lb] = n;
	}

	printf("%ld", dp.size());
}
