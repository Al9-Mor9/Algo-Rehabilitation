#include <iostream>
#include <cstring>
using namespace std;

char str[2000001];

bool aka(char *s, int l, int start){
    if (l == 1) return true; 

    for (int i = 0; i < l/2; i++){
        if (s[i + start] == s[start +  l - 1 - i]) {
            continue;
        }
        return false;
    }
    return aka(s, l/2, start) && aka(s, l/2, l-l/2);
}

int main(){
    scanf("%s", str);
    int len = strlen(str);
    if (!aka(str, len, 0)) printf("IPSELENTI");
    else printf("AKARAKA");

}
