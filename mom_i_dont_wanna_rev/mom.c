#include <stdio.h>

int main(int argc, char * argv[]){
    printf("What is the flag?\n");

    char flag[14];

    scanf("%s", flag);

    int isflag = 1;

    if (flag[6] != 0x7b){
        isflag = 0;
    }
    if (flag[12] != 0x7d){
        isflag = 0;
    }
    if (flag[9] != 0x6d){
        isflag = 0;
    }
    if (flag[10] != 0x6d){
        isflag = 0;
    }
    if (flag[7] != 0x6d){
        isflag = 0;
    }
    if (flag[4] != 0x74){
        isflag = 0;
    }
    if (flag[9] != 0x6d){
        isflag = 0;
    }
    if (flag[10] != 0x6d){
        isflag = 0;
    }
    if (flag[7] != 0x6d){
        isflag = 0;
    }
    if (flag[3] != 0x63){
        isflag = 0;
    }
    if (flag[5] != 0x66){
        isflag = 0;
    }
    if (flag[1] != 0x79){
        isflag = 0;
    }
    if (flag[2] != 0x75){
        isflag = 0;
    }
    if (flag[8] != 0x75){
        isflag = 0;
    }
    if (flag[9] != 0x6d){
        isflag = 0;
    }
    if (flag[0] != 0x62){
        isflag = 0;
    }
    if (flag[10] != 0x6d){
        isflag = 0;
    }
    if (flag[7] != 0x6d){
        isflag = 0;
    }
    if (flag[11] != 0x79){
        isflag = 0;
    }
    


    if (isflag == 1){
        printf("You got it!\n");
    } else {
        printf("you failed. do better next time\n");
    }
}