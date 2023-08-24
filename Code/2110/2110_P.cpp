#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
	int N,C, adr, distance = 0, size;
	int left = 1, right, mid, cur, cnt, ans = 0;
	scanf("%d %d", &N, &C);
	vector<int> home;
	while (N--) {
		scanf("%d", &adr);
		home.push_back(adr);
	}
	sort(home.begin(), home.end());
	right = home.back() - home.front();
	size = home.size();

	while (left <= right) {
		mid = (left + right) / 2;
		cnt = 1;
		cur = home[0];

		for (int i = 1; i < size; i++) {
			distance = home[i] - cur;
			if (mid <= distance) {
				cnt++;
				cur = home[i];
			}
		}

		if (cnt >= C) { left = mid + 1; ans = mid; }
		else right = mid - 1;

	}

	printf("%d", ans);
}
