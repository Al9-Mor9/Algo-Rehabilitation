#include <iostream>
#include <stack>
#include <string.h>
using namespace std;

int N;
char expr[101];
int operand[26];
double ans;
stack<double> stk;

int main(){
    scanf("%d", &N);
    scanf("%s", expr);

    for (int i = 0; i < N; i++){
        scanf("%d", &operand[i]);
    }

    for (int i = 0; i < strlen(expr); i++){
        if (expr[i] >= 'A' && expr[i] <= 'Z'){
            stk.push(operand[expr[i] - 'A']);
        }
        else {
            double tmp = 0;
            double operand1 = stk.top();
            stk.pop();
            double operand2 = stk.top();
            stk.pop();
            if (expr[i] == '+'){
                tmp = operand2 + operand1;
            }
            else if (expr[i] == '-'){
                tmp = operand2 - operand1;
            }
            else if (expr[i] == '/'){
                tmp = operand2 / operand1;
            }
            else if (expr[i] == '*'){
                tmp = operand2 * operand1;
            }
            stk.push(tmp);
        }
    }
    printf("%.2lf", stk.top());
}
