#include <stdio.h>
using namespace std;

int N, num[500000], sorted[500000];	

long long bubble(int start, int end) {
	if (start == end) return 0;
	int mid = (start + end) / 2;
	long long result = bubble(start, mid) + bubble(mid + 1, end);
	
	int index = 0;
	int i = start, j = mid + 1;
	
	while (i <= mid || j <= end) {
		if (i <= mid && (j > end || num[i] <= num[j])) sorted[index++] = num[i++];
		else {
			result += (long long)(mid - i + 1);
			sorted[index++] = num[j++];
		}
	}

	for (int i = start; i<=end; i++){
		num[i] = sorted[i - start];
	}

		
	return result;
}


int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &num[i]);
	}
	printf("%lld", bubble(0, N-1));
		
}
