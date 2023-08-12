#include <algorithm>
#include <iostream>
using namespace std;

int main() {
	int N, start, count = 1;

	scanf("%d", &N);

	pair<int, int> *meeting = new pair<int, int>[N];


	for (int i = 0; i < N; i++) {
		scanf("%d %d", &meeting[i].second, &meeting[i].first);
	}

	sort(meeting, meeting + N);

	start = meeting[0].first;

	for (int i = 1; i < N; i++) {
		if (meeting[i].second >= start) { start = meeting[i].first; count++; }
	}

	printf("%d", count);
	
}
