#include <stdio.h>
#include <string.h>

int main(int argc, char * argv[]){
    printf("What is the flag?\n");

    char flag[31];

    scanf("%s", flag);

    int isflag = strcmp(flag, "byuctf{readmorechildrensbooks}");

    if (isflag == 0){
        printf("That is correct!\n");
    } else {
        printf("Sorry, that's not right. Try again soon!\n");
    }
}