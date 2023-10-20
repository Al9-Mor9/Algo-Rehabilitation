#include <iostream>
#include <stack>
using namespace std;

const int MAXN = 500001;

int N, tower[MAXN];
stack<int> stk;

int main(){
	scanf("%d", &N);
	
	for (int i = 1; i <= N; i++) {
		scanf("%d", &tower[i]);
		if (stk.empty()){
			printf("0 ");
			stk.push(i);
		}
		else if (tower[stk.top()] < tower[i]){
			while (!stk.empty() && tower[stk.top()] < tower[i]) stk.pop();
			printf("%d ", stk.empty() ? 0 : stk.top());
			stk.push(i);
		}
		else {
			printf("%d ", stk.top());
			stk.push(i);
		}
	}
}
