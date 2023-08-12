#include <iostream>
using namespace std;

char x[5] = {0, }, y[5] = {0, }, z[5] = { 0, };
int xi, yi, zi;

int main(){
	scanf("%s%s", x, y);
	for (int i = 3; i >= 0; i--){
		if (x[i]){ 
			xi *= 10;
			xi += x[i] - '0';
		}
		if (y[i]){
			yi *= 10;
			yi += y[i] - '0';
		}	
	}
	zi = xi + yi;
	for (int i = 0; i < 4; i++){
		if (!zi) continue;
		z[i] = zi % 10 + '0';
		zi /= 10;
	}	
	printf("%d", atoi(z));

}
